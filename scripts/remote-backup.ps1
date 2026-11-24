<#
.SYNOPSIS
    Remote backup orchestration with high-security constraints.
.DESCRIPTION
    Integrates with the fleet's zero-knowledge age backup pipelines (dell-nightly-backup.sh / ha-pos-nightly-backup.sh)
    by default, or performs legacy local EFS-encrypted SCP dumps when -UseLegacyLocalScp is specified.
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-11-21
#>
[CmdletBinding()]
param(
    [string]$Stack = "all",
    [ValidateSet('dell-server', 'homeassistant-pos', 'Justice')]
    [string]$Target = 'dell-server',
    [switch]$UseLegacyLocalScp
)

$ErrorActionPreference = 'Stop'

if ($Target -eq 'Justice') {
    $sshTarget = "jusparr@100.79.211.101"
}
elseif ($Target -eq 'homeassistant-pos') {
    $sshTarget = "hassio@10.0.20.222"
}
else {
    $sshTarget = "hassio@10.0.20.221"
}

$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"
$sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=10", $sshTarget)

if (-not $UseLegacyLocalScp -and $Target -in @('dell-server', 'homeassistant-pos')) {
    $remoteScript = if ($Target -eq 'dell-server') {
        "/home/hassio/.local/bin/dell-nightly-backup.sh"
    } else {
        "/home/hassio/.local/bin/ha-pos-nightly-backup.sh"
    }
    $remoteLog = if ($Target -eq 'dell-server') {
        "/home/hassio/.local/share/fleet/dell-nightly-backup.log"
    } else {
        "/home/hassio/.local/share/fleet/hapos-nightly-backup.log"
    }

    Write-Host "Triggering zero-knowledge age backup on $Target ($sshTarget) -> $remoteScript..." -ForegroundColor Cyan
    & ssh @sshArgs "$remoteScript && echo '--- LOG TAIL ---' && tail -n 10 $remoteLog"
    if ($LASTEXITCODE -ne 0) {
        throw "Remote zero-knowledge backup failed on $Target with exit code $LASTEXITCODE"
    }
    try {
        $bkpLogFile = "D:\_Consolidation_Manifests\Logs\Docker_Remote_Backup.log"
        $bkpLogDir = Split-Path $bkpLogFile -Parent
        if (-not (Test-Path -LiteralPath $bkpLogDir)) { New-Item -Path $bkpLogDir -ItemType Directory -Force | Out-Null }
        [System.IO.File]::AppendAllText($bkpLogFile, "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] [AGE_BACKUP_OK] Target=$Target RemoteScript=$remoteScript`r`n", [System.Text.UTF8Encoding]::new($false))
    } catch {}
    Write-Host "[OK] Remote zero-knowledge backup completed on $Target." -ForegroundColor Green
    return
}

if (-not $UseLegacyLocalScp -and $Target -eq 'Justice') {
    Write-Host "Running non-destructive remote stack & container check on Justice ($sshTarget)..." -ForegroundColor Cyan
    & ssh @sshArgs "cd /home/jusparr/docker/stacks && ls -d */ && docker ps --format '{{.Names}}|{{.Status}}'"
    if ($LASTEXITCODE -ne 0) {
        throw "Remote check failed on Justice with exit code $LASTEXITCODE"
    }
    try {
        $bkpLogFile = "D:\_Consolidation_Manifests\Logs\Docker_Remote_Backup.log"
        $bkpLogDir = Split-Path $bkpLogFile -Parent
        if (-not (Test-Path -LiteralPath $bkpLogDir)) { New-Item -Path $bkpLogDir -ItemType Directory -Force | Out-Null }
        [System.IO.File]::AppendAllText($bkpLogFile, "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] [JUSTICE_REMOTE_CHECK_OK] Target=Justice`r`n", [System.Text.UTF8Encoding]::new($false))
    } catch {}
    Write-Host "[OK] Justice remote stack inspection complete (pass -UseLegacyLocalScp to dump/fetch EFS backups)." -ForegroundColor Green
    return
}

$dateStr = (Get-Date).ToString("yyyy-MM-dd")
$localBackupDir = "D:\Docker\Backups\$dateStr"
$remoteBackupDir = "/tmp/docker_backups_$dateStr"

Write-Host "Starting Secure Legacy SCP Remote Backup for $Target ($dateStr)..." -ForegroundColor Cyan

try {
    New-Item -ItemType Directory -Force -Path $localBackupDir | Out-Null
    & ssh @sshArgs "mkdir -p $remoteBackupDir && chmod 700 $remoteBackupDir"

    Write-Host "Executing database dumps..."

    # Security Note: Infisical injects secrets directly into runtime memory.
    # We reference native environment variables inside the container rather than legacy /run/secrets mounts.
    $dbTasks = @(
        @{ Name = "traccar-db"; Cmd = 'DB_PW=${MARIADB_ROOT_PASSWORD:-$MYSQL_ROOT_PASSWORD}; (MYSQL_PWD="$DB_PW" mariadb-dump -u root --all-databases --single-transaction 2>/dev/null || MYSQL_PWD="$DB_PW" mysqldump -u root --all-databases --single-transaction) | gzip' }
        @{ Name = "web-db-1"; Cmd = '(MYSQL_PWD="$MYSQL_ROOT_PASSWORD" mysqldump -u root --all-databases --single-transaction --quick 2>/dev/null || MYSQL_PWD="$MYSQL_PASSWORD" mysqldump -u "${MYSQL_USER:-wordpress}" "${MYSQL_DATABASE:-wordpress}" --single-transaction --quick --no-tablespaces) | gzip' }
        @{ Name = "infrastructure-authentik-db-1"; Cmd = 'pg_dumpall -U "${POSTGRES_USER:-authentik}" | gzip' }
        @{ Name = "infisical-db"; Cmd = 'pg_dumpall -U "${POSTGRES_USER:-infisical}" | gzip' }
        @{ Name = "homeassistant-db"; Cmd = 'pg_dumpall -U "${POSTGRES_USER:-hassio}" | gzip' }
    )

    foreach ($db in $dbTasks) {
        $check = & ssh @sshArgs "docker ps -q -f name=^$($db.Name)$"
        if (-not [string]::IsNullOrWhiteSpace($check)) {
            Write-Host "  Dumping $($db.Name)..."
            & ssh @sshArgs "docker exec $($db.Name) sh -c '$($db.Cmd)' > $remoteBackupDir/$($db.Name)_$dateStr.sql.gz"
        }
    }

    # Safe SQLite Online Backup for Vaultwarden on host mount
    $vwCheck = & ssh @sshArgs "docker ps -q -f name=^infrastructure-vaultwarden-1$"
    if (-not [string]::IsNullOrWhiteSpace($vwCheck)) {
        Write-Host "  Saving vaultwarden (SQLite + Attachments)..."
        & ssh @sshArgs "if [ -f /home/hassio/vaultwarden/db.sqlite3 ] && command -v sqlite3 >/dev/null 2>&1; then sqlite3 -readonly /home/hassio/vaultwarden/db.sqlite3 `".backup $remoteBackupDir/vaultwarden_$dateStr.sqlite3`"; fi"
        & ssh @sshArgs "tar -czf $remoteBackupDir/vaultwarden_data_$dateStr.tar.gz -C /home/hassio/vaultwarden attachments sends rsa_key* config.json 2>/dev/null || true"
    }

    # Redis instances
    $redisContainers = @("infrastructure-authentik-redis-1", "web-redis-1", "infisical-redis")
    foreach ($redis in $redisContainers) {
        $check = & ssh @sshArgs "docker ps -q -f name=^$redis$"
        if (-not [string]::IsNullOrWhiteSpace($check)) {
            Write-Host "  Saving $redis..."
            & ssh @sshArgs "docker exec $redis redis-cli BGSAVE"
            Start-Sleep -Seconds 5
            & ssh @sshArgs "docker cp ${redis}:/data/dump.rdb $remoteBackupDir/${redis}_${dateStr}.rdb 2>/dev/null || true"
        }
    }

    Write-Host "Downloading backups via SCP..."
    $hasRemoteFiles = & ssh @sshArgs "ls -A $remoteBackupDir 2>/dev/null | head -n 1"
    if (-not [string]::IsNullOrWhiteSpace($hasRemoteFiles)) {
        & scp -i $sshKey -o "BatchMode=yes" -o "StrictHostKeyChecking=yes" -o "ConnectTimeout=5" -r "${sshTarget}:${remoteBackupDir}/*" "$localBackupDir/"
    } else {
        Write-Host "  No remote dump files produced on $Target." -ForegroundColor Yellow
    }

    Write-Host "Applying EFS Hardware/OS-level encryption to local backup..."
    & cipher.exe /e /a /s:"$localBackupDir" | Out-Null

    $files = Get-ChildItem -Path $localBackupDir
    $totalSize = ($files | Measure-Object -Property Length -Sum).Sum / 1MB
    Write-Host "Local Backup completed & encrypted. Size: $([math]::Round($totalSize, 2)) MB." -ForegroundColor Green

    Write-Host "Pushing encrypted offsite backup to Google Drive via rclone (gdrive_crypt)..."
    try {
        & ssh @sshArgs "if rclone listremotes 2>/dev/null | grep -qx 'gdrive_crypt:'; then rclone sync $remoteBackupDir gdrive_crypt:DockerBackups/$dateStr; else echo 'gdrive_crypt not configured on remote host'; fi"
        Write-Host "Offsite sync step complete." -ForegroundColor Green
    }
    catch {
        Write-Host "Warning: Rclone sync to Google Drive failed or 'gdrive_crypt' remote not configured." -ForegroundColor Yellow
    }

    Write-Host "Forensically wiping remote backup temporary files..."
    & ssh @sshArgs "find $remoteBackupDir -type f -exec shred -u -z {} \+ 2>/dev/null || (find $remoteBackupDir -type f -exec sh -c 'dd if=/dev/zero of=`$1 bs=1M count=`$(du -m `$1 | cut -f1) 2>/dev/null; rm -f `$1' _ {} \;) ; rm -rf $remoteBackupDir"

    try {
        $bkpLogFile = "D:\_Consolidation_Manifests\Logs\Docker_Remote_Backup.log"
        $bkpLogDir = Split-Path $bkpLogFile -Parent
        if (-not (Test-Path -LiteralPath $bkpLogDir)) { New-Item -Path $bkpLogDir -ItemType Directory -Force | Out-Null }
        [System.IO.File]::AppendAllText(
            $bkpLogFile,
            "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] [LEGACY_SCP_BACKUP_OK] Target=$Target SizeMB=$([math]::Round($totalSize, 2))`r`n",
            [System.Text.UTF8Encoding]::new($false)
        )
    } catch {
        Write-Host "Warning: Backup log write failed: $($_.Exception.Message)" -ForegroundColor Yellow
    }

}
catch {
    Write-Error "Backup encountered an error: $_"
}
