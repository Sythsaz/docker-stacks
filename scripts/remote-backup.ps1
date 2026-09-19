<#
.SYNOPSIS
    Remote backup orchestration with high-security constraints.
.DESCRIPTION
    Executes database dumps on the Dell server and SCPs them locally.
    Implements forensic remote wiping, EFS encryption, and VaultOp logging.
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-09-11
#>
[CmdletBinding()]
param(
    [string]$Stack = "all"
)

$ErrorActionPreference = 'Stop'

$sshTarget = "hassio@10.0.20.221"
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"
$sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=5", $sshTarget)

$dateStr = (Get-Date).ToString("yyyy-MM-dd")
$localBackupDir = "D:\Docker\Backups\$dateStr"
$remoteBackupDir = "/tmp/docker_backups_$dateStr"

Write-Host "Starting Secure Remote Backup ($dateStr)..." -ForegroundColor Cyan

try {
    New-Item -ItemType Directory -Force -Path $localBackupDir | Out-Null
    ssh @sshArgs "mkdir -p $remoteBackupDir && chmod 700 $remoteBackupDir"

    Write-Host "Executing database dumps..."
    
    # Define known database containers and their dump commands
    # Security Note: Uses $(cat /run/secrets/...) because _FILE environment variables 
    # do NOT populate the raw password variables inside the container environment.
    $dbTasks = @(
        @{ Name="traccar-db"; Cmd="mysqldump -u root -p$$(cat /run/secrets/traccar_db_root) --all-databases | gzip" }
        @{ Name="web-db-1"; Cmd="mysqldump -u root -p$$(cat /run/secrets/mysql_root_password) --all-databases | gzip" }
        @{ Name="authentik-db"; Cmd="pg_dumpall -U authentik | gzip" }
        @{ Name="homeassistant-db"; Cmd="pg_dumpall -U homeassistant | gzip" }
    )
    
    foreach ($db in $dbTasks) {
        $check = ssh @sshArgs "docker ps -q -f name=^$($db.Name)$"
        if (-not [string]::IsNullOrWhiteSpace($check)) {
            Write-Host "  Dumping $($db.Name)..."
            # Execute dump directly into the remote secure directory
            ssh @sshArgs "docker exec $($db.Name) sh -c '$($db.Cmd)' > $remoteBackupDir/$($db.Name)_$dateStr.sql.gz"
        }
    }

    # Safe SQLite Online Backup for Vaultwarden
    $vwCheck = ssh @sshArgs "docker ps -q -f name=vaultwarden"
    if (-not [string]::IsNullOrWhiteSpace($vwCheck)) {
        Write-Host "  Saving vaultwarden (SQLite + Attachments)..."
        # Uses SQLite online backup API to ensure zero corruption while running
        ssh @sshArgs "docker exec -i `$vwCheck sh -c 'sqlite3 /data/db.sqlite3 `".backup /tmp/db-backup.sqlite3`"'"
        ssh @sshArgs "docker cp `$vwCheck:/tmp/db-backup.sqlite3 $remoteBackupDir/vaultwarden_$dateStr.sqlite3"
        # Also backup the attachments and RSA keys directly from the host mount
        ssh @sshArgs "tar -czf $remoteBackupDir/vaultwarden_data_$dateStr.tar.gz -C /home/hassio/vaultwarden attachments sends rsa_key* config.json 2>/dev/null"
    }

    # Redis instances
    $redisContainers = @("authentik-redis", "web-redis-1")
    foreach ($redis in $redisContainers) {
        $check = ssh @sshArgs "docker ps -q -f name=^$redis$"
        if (-not [string]::IsNullOrWhiteSpace($check)) {
            Write-Host "  Saving $redis..."
            ssh @sshArgs "docker exec $redis redis-cli BGSAVE"
            Start-Sleep -Seconds 5
            ssh @sshArgs "docker cp $redis:/data/dump.rdb $remoteBackupDir/$redis_$dateStr.rdb"
        }
    }

    Write-Host "Downloading backups via SCP..."
    scp -i $sshKey -o "BatchMode=yes" -o "StrictHostKeyChecking=yes" -o "ConnectTimeout=5" -r "${sshTarget}:/*" "$localBackupDir/"

    Write-Host "Applying EFS Hardware/OS-level encryption to local backup..."
    cipher.exe /e /a /s:"$localBackupDir" | Out-Null
    
    $files = Get-ChildItem -Path $localBackupDir
    $totalSize = ($files | Measure-Object -Property Length -Sum).Sum / 1MB
    Write-Host "Local Backup completed & encrypted. Size: $([math]::Round($totalSize, 2)) MB." -ForegroundColor Green

    Write-Host "Pushing offsite backup to Google Drive via rclone..."
    # Execute rclone on the Debian host. Assumes a configured remote named 'gdrive'.
    try {
        ssh @sshArgs "rclone sync $remoteBackupDir gdrive:DockerBackups/$dateStr"
        Write-Host "Offsite sync to Google Drive complete." -ForegroundColor Green
    } catch {
        Write-Host "Warning: Rclone sync to Google Drive failed or 'gdrive' remote not configured." -ForegroundColor Yellow
    }

    Write-Host "Forensically wiping remote backup temporary files..."
    # Use shred or dd to zero-fill files before rm
    ssh @sshArgs "find $remoteBackupDir -type f -exec shred -u -z {} \+ 2>/dev/null || (find $remoteBackupDir -type f -exec sh -c 'dd if=/dev/zero of=$$1 bs=1M count=$$(du -m $$1 | cut -f1) 2>/dev/null; rm -f $$1' _ {} \;) ; rm -rf $remoteBackupDir"

    # Dispatch audit log via VaultOp.ps1
    $vaultOp = "C:\Users\ashto\Docker\scripts\VaultOp.ps1"
    if (Test-Path $vaultOp) {
        $vaultOpAcl = Get-Acl $vaultOp
        $isSafe = $true
        $currentUserSid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
        $allowedSids = @('S-1-5-18', 'S-1-5-32-544', $currentUserSid)
        
        foreach ($rule in $vaultOpAcl.Access) {
            if ($rule.FileSystemRights -match "Write|Modify|FullControl") {
                try {
                    $ruleSid = $rule.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value
                    if ($ruleSid -notin $allowedSids) { $isSafe = $false; break }
                }
                catch { $isSafe = $false; break }
            }
        }
        
        if (-not $isSafe) {
            Write-Host "CRITICAL SECURITY WARNING: VaultOp.ps1 is writable by unauthorized users! Execution blocked." -ForegroundColor Red
        }
        else {
            try {
                $processArgs = "-ExecutionPolicy Bypass -Command "& '$vaultOp' -Action 'Remote Backup' -Details 'Database backups fetched and EFS encrypted. Size: $([math]::Round($totalSize, 2)) MB'""
                Start-Process -FilePath "powershell.exe" -ArgumentList $processArgs -NoNewWindow -Wait
            }
            catch { Write-Host "Warning: VaultOp logging failed." -ForegroundColor Yellow }
        }
    }

} catch {
    Write-Error "Backup encountered an error: $_"
}