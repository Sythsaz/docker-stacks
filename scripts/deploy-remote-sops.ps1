<#
.SYNOPSIS
    Deploys compose stacks to the Dell server.
.DESCRIPTION
    Decrypts SOPS secrets, SCPs compose and secrets to the remote server, and executes docker compose.
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-09-07
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)]
    # Enforce strict <domain>/<service> naming convention and support Windows tab-completion slashes
    [ValidatePattern('^[a-zA-Z0-9_-]+[/\\][a-zA-Z0-9_-]+$')]
    [string]$Stack,

    [ValidateSet('up -d', 'down', 'pull', 'restart')]
    [string]$Action = 'up -d',

    [switch]$DryRun,

    [switch]$ForceRecreate,

    [switch]$MonitorLogs
)

$ErrorActionPreference = 'Stop'
$encFiles = $null  # Initialize to prevent scoping errors in the finally block

$remoteUser = "hassio"
$remoteHost = "10.0.20.221"
$remoteBaseDir = "/home/hassio/docker"
$sshTarget = "${remoteUser}@${remoteHost}"
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"

# Enforce SOPS age private key binding for the current session
$sopsKey = "$env:USERPROFILE\.config\sops\age\keys.txt"
if (-not (Test-Path $sopsKey)) {
    throw "SOPS private key missing at $sopsKey. Run bootstrap-sops.ps1."
}
$env:SOPS_AGE_KEY_FILE = $sopsKey

# Enforce explicit identity file, strict host key checking, and fail-fast timeouts
$sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=10", "-o", "ServerAliveInterval=15", "-o", "ServerAliveCountMax=3", "-n", $sshTarget)

# Destructive operation safeguard
if ($Action -match "down") {
    if (-not $DryRun -and -not $PSCmdlet.ShouldProcess($Stack, "Execute destructive action: $Action")) {
        Write-Host "Destructive action aborted." -ForegroundColor Red
        return
    }
}

# Isolate path formatting: strictly OS-native for local, forward-slash for remote
$remoteStack = $Stack -replace '\\', '/'
$remoteStackDir = "$remoteBaseDir/$remoteStack"

$localStack = $Stack -replace '/', '\'
$localStackDir = "$env:USERPROFILE\Docker\stacks\$localStack"

if (-not (Test-Path "$localStackDir\compose.yaml")) {
    throw "compose.yaml not found in $localStackDir"
}

# Mitigate predictable temp directory attacks by utilizing a GUID
$safeStackName = $Stack -replace '[/\\]', '-'
$tempDir = Join-Path ([System.IO.Path]::GetTempPath()) "docker-deploy-$safeStackName-$([guid]::NewGuid().ToString().Substring(0,8))"

# Fail-fast: Validate remote Docker daemon connectivity and Compose V2 presence
Write-Host "Verifying remote Docker daemon and Compose V2 plugin on $remoteHost..."
if (-not $DryRun) {
    ssh @sshArgs "docker info >/dev/null 2>&1 && docker compose version >/dev/null 2>&1"
    if ($LASTEXITCODE -ne 0) {
        throw "Pre-flight failed on $remoteHost. Verify Docker is running, the user has socket access, and the Compose V2 plugin is installed."
    }
}

Write-Host "[$(Get-Date -f 'yyyy-MM-dd HH:mm:ss')] Starting deployment of $remoteStack (Action: $Action)" -ForegroundColor Cyan

try {
    New-Item -ItemType Directory -Path $tempDir -Force | Out-Null
    
    # Enforce strict ACLs on temporary directory to prevent unauthorized read access
    $currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
    $systemSid = New-Object System.Security.Principal.SecurityIdentifier('S-1-5-18')
    $adminSid = New-Object System.Security.Principal.SecurityIdentifier('S-1-5-32-544')

    $dirAcl = Get-Acl $tempDir
    $dirAcl.SetAccessRuleProtection($true, $false)
    $dirAcl.Access | Where-Object { -not $_.IsInherited } | ForEach-Object { $dirAcl.RemoveAccessRule($_) } | Out-Null
    $inherit = [System.Security.AccessControl.InheritanceFlags]::ContainerInherit -bor [System.Security.AccessControl.InheritanceFlags]::ObjectInherit
    $propagate = [System.Security.AccessControl.PropagationFlags]::None
    $dirAcl.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule($currentUser, "FullControl", $inherit, $propagate, "Allow")))
    $dirAcl.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule($systemSid, "FullControl", $inherit, $propagate, "Allow")))
    $dirAcl.AddAccessRule((New-Object System.Security.AccessControl.FileSystemAccessRule($adminSid, "FullControl", $inherit, $propagate, "Allow")))
    Set-Acl $tempDir $dirAcl

    # Apply Windows EFS hardware/OS-level encryption to temp files at rest
    cipher.exe /e /a "$tempDir" | Out-Null
    
    # Critical: Recursively copy compose.yaml, .env, and all sidecar configuration files.
    # -Force is mandatory to ensure hidden sidecar files (e.g., .htpasswd) are included.
    # Explicitly exclude local 'data' mounts and raw 'secrets' to prevent raw .enc leakage
    Get-ChildItem -Path $localStackDir -Force | Where-Object { $_.Name -notin @('data', 'secrets') } | Copy-Item -Destination $tempDir -Recurse -Force
    
    $secretsDir = "$localStackDir\secrets"
    if (Test-Path $secretsDir) {
        New-Item -ItemType Directory -Path "$tempDir\secrets" -Force | Out-Null
        $encFiles = Get-ChildItem -Path $secretsDir -Filter "*.enc"
        
        foreach ($file in $encFiles) {
            $decryptedName = $file.Name -replace '\.enc$', ''
            $decryptedPath = "$tempDir\secrets\$decryptedName"
            
            Write-Host "Decrypting secret for local validation: $($file.Name) -> $decryptedName"
            sops --decrypt --output "$decryptedPath" "$($file.FullName)"
            if ($LASTEXITCODE -ne 0) { throw "SOPS decryption failed for $($file.Name)." }
        }

        # Temporarily rewrite /dev/shm to ./secrets using BOM-less UTF-8 to preserve Linux compatibility
        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
        $composeContent = (Get-Content "$tempDir\compose.yaml" -Raw -Encoding UTF8) -replace '/dev/shm/([a-zA-Z0-9_.-]+)', './secrets/$1'
        [System.IO.File]::WriteAllText("$tempDir\compose.yaml", $composeContent, $utf8NoBom)
    }

    Write-Host "Validating assembled compose specification syntax..."
    docker compose -f "$tempDir\compose.yaml" config -q
    if ($LASTEXITCODE -ne 0) {
        throw "Assembled compose validation failed. Check syntax in $localStackDir\compose.yaml."
    }
    
    if (Test-Path $secretsDir) {
        # Restore the production in-memory path using BOM-less UTF-8 before SCP transfer
        $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
        $composeContent = (Get-Content "$tempDir\compose.yaml" -Raw -Encoding UTF8) -replace '\./secrets/([a-zA-Z0-9_.-]+)', '/dev/shm/$1'
        [System.IO.File]::WriteAllText("$tempDir\compose.yaml", $composeContent, $utf8NoBom)
    }

    # Defense-in-depth: Force recursive EFS application
    cipher.exe /e /a /s:"$tempDir" | Out-Null
    
    Write-Host "Preparing remote directory..."
    if (-not $DryRun) {
        # Dynamically append .env purge command if it was removed locally to prevent configuration drift
        $staleEnvPurge = if (-not (Test-Path "$localStackDir\.env")) { "rm -f `"$remoteStackDir/.env`" && " } else { "" }
        
        # Purge legacy compose files and ensure remote secrets directory is NOT created
        ssh @sshArgs "$staleEnvPurge rm -f `"$remoteStackDir/docker-compose.yml`" `"$remoteStackDir/docker-compose.yaml`" && rm -f `"$remoteStackDir/secrets/*.enc`" `"$remoteStackDir/secrets/*.env`" && mkdir -p `"$remoteStackDir/data`" `"$remoteStackDir/secrets`""
        
        # Enforce exit code validation to prevent SCP failure cascade
        if ($LASTEXITCODE -ne 0) { throw "Remote directory preparation failed with exit code $LASTEXITCODE" }
    }
    else {
        $staleEnvPurge = if (-not (Test-Path "$localStackDir\.env")) { "rm -f `"$remoteStackDir/.env`" && " } else { "" }
        Write-Host "[DRY-RUN] Would execute: ssh -i $sshKey -o BatchMode=yes -o StrictHostKeyChecking=yes $sshTarget `"$staleEnvPurge rm -f \"$remoteStackDir/docker-compose.yml\" \"$remoteStackDir/docker-compose.yaml\" && rm -rf \"$remoteStackDir/secrets\" && mkdir -p \"$remoteStackDir/data\"`"" -ForegroundColor Yellow
    }

    Write-Host "Copying files via SCP..."
    if (-not $DryRun) {
        # Transfer decrypted secrets directly to the remote RAM disk (/dev/shm) first
        if (Test-Path "$tempDir\secrets") {
            $decryptedFiles = @(Get-ChildItem -Path "$tempDir\secrets" -File)
            if ($decryptedFiles.Count -gt 0) {
                Write-Host "Transferring decrypted secrets natively to remote /dev/shm memory..."
                
                # Stream each secret via CMD stdin with install -m 600 to avoid the
                # SCP umask race condition AND PowerShell line-ending corruption
                $streamSshBase = "ssh -i `"$sshKey`" -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=10 -o ServerAliveInterval=15 -o ServerAliveCountMax=3 $sshTarget"
                foreach ($secretFile in $decryptedFiles) {
                    $remoteName = $secretFile.Name
                    $localPath = $secretFile.FullName
                    Write-Host "  Streaming $remoteName -> /dev/shm/$remoteName (mode 600)"
                    cmd.exe /c "$streamSshBase install -m 600 /dev/stdin /dev/shm/$remoteName < `"$localPath`""
                    if ($LASTEXITCODE -ne 0) { throw "Secret stream transfer failed for $remoteName" }
                }
            }
            # Purge plaintext secrets locally so they are NOT caught in the main recursive SCP to the persistent disk
            Remove-Item -Path "$tempDir\secrets" -Recurse -Force
        }

        # Main stack transfer (compose file, config dirs, etc.) to the persistent disk
        # Using '.' copies the contents of the directory without wildcard translation issues
        scp -i $sshKey -o "BatchMode=yes" -o "StrictHostKeyChecking=yes" -o "ConnectTimeout=10" -o "ServerAliveInterval=15" -o "ServerAliveCountMax=3" -r "$tempDir/." "${sshTarget}:${remoteStackDir}/"
        if ($LASTEXITCODE -ne 0) { throw "Stack SCP transfer failed with exit code $LASTEXITCODE" }
        
        # Enforce 600 permissions on standard .env files
        ssh @sshArgs "if [ -f `"$remoteStackDir/.env`" ]; then chmod 600 `"$remoteStackDir/.env`"; fi"
    }
    else {
        Write-Host "[DRY-RUN] Would execute: scp -i $sshKey -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=5 -r `"$tempDir/.`" `"${sshTarget}:${remoteStackDir}/`"" -ForegroundColor Yellow
    }

    $configFiles = Get-ChildItem -Path $localStackDir -File -Recurse | Where-Object { 
        $_.FullName -notmatch '[\\/]secrets[\\/]' -and 
        $_.Name -ne ".env" -and 
        $_.Name -notmatch '^docker-compose' -and 
        $_.Name -notmatch '^compose\.y' 
    } | Sort-Object FullName

    $hashString = ""
    foreach ($file in $configFiles) {
        $hashString += (Get-FileHash $file.FullName -Algorithm MD5).Hash
    }

    $hashExports = @()
    if ($hashString) {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($hashString)
        $stream = [System.IO.MemoryStream]::new($bytes)
        $stackHash = (Get-FileHash -InputStream $stream -Algorithm MD5).Hash
        $stream.Close()
        $hashExports += "export STACK_CONFIG_HASH=`"$stackHash`""
    }
    else {
        $hashExports += "export STACK_CONFIG_HASH=`"none`""
    }

    Write-Host "Executing docker compose $Action on remote host..."
    if (-not $DryRun) {
        # Utilize native Compose V2 arguments for atomic pulls and thorough orphan cleanup
        $actionCmd = switch ($Action) {
            'up -d' { 
                if ($ForceRecreate) { "up -d --wait --pull always --remove-orphans --force-recreate" }
                else { "up -d --wait --pull always --remove-orphans" }
            }
            'down' { "down --remove-orphans" }
            Default { $Action }
        }
        
        $hashExportsStr = $hashExports -join " && "
        if ($hashExportsStr) { $hashExportsStr += " && " }

        ssh @sshArgs "cd `"$remoteStackDir`" && ${hashExportsStr}docker compose -f compose.yaml $actionCmd"
        if ($LASTEXITCODE -ne 0) { throw "SSH execution failed with exit code $LASTEXITCODE" }

    }
    else {
        $actionCmd = switch ($Action) {
            'up -d' { 
                if ($ForceRecreate) { "up -d --wait --pull always --remove-orphans --force-recreate" }
                else { "up -d --wait --pull always --remove-orphans" }
            }
            'down' { "down --remove-orphans" }
            Default { $Action }
        }
        $hashExportsStr = $hashExports -join " && "
        if ($hashExportsStr) { $hashExportsStr += " && " }
        Write-Host "[DRY-RUN] Would execute: ssh -i $sshKey -o BatchMode=yes -o StrictHostKeyChecking=yes$sshTarget `"cd \"$remoteStackDir\" && ${hashExportsStr}docker compose -f compose.yaml $actionCmd`"" -ForegroundColor Yellow
    }

    if ($MonitorLogs -and -not$DryRun -and ($Action -eq 'up -d' -or $Action -eq 'restart')) {
        & (Join-Path $PSScriptRoot "monitor-remote.ps1") -Stack $Stack -NewWindow
    }

    Write-Host "[$(Get-Date -f 'yyyy-MM-dd HH:mm:ss')] Deployment complete." -ForegroundColor Green
}
finally {
    # 1. Remote RAM Disk Cleanup: Guaranteed to execute even if Docker Compose crashes
    if ($null -ne $encFiles -and -not $DryRun) {
        Write-Host "Securely wiping decrypted secrets from remote /dev/shm memory..."
        if ($encFiles.Count -gt 0) {
            $rmCmds = $encFiles | ForEach-Object {
                $envName = $_.Name -replace '\.enc$', ''
                "rm -f /dev/shm/$envName"
            }
            $combinedRm = $rmCmds -join " ; "
            ssh @sshArgs $combinedRm 2>$null
        }
    }

    # 2. Local Forensic Temp Cleanup
    if (Test-Path $tempDir) {
        Write-Host "Securely wiping decrypted temp files at $tempDir..."
        # Forensic cleanup: Zero out plaintext files before deletion to prevent disk recovery.
        # -Force is mandatory to ensure hidden files like .env are not skipped
        Get-ChildItem -Path "$tempDir" -File -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object {
            $lockedFile = $_.FullName
            $lockedName = $_.Name
            try {
                $nullArray = New-Object byte[] $_.Length
                [System.IO.File]::WriteAllBytes($lockedFile, $nullArray)
            }
            catch {
                # $_ is the ErrorRecord here; use the pre-captured $lockedName variable
                Write-Host "Warning: Could not zero-out $lockedName. File handle may be locked by an external process." -ForegroundColor Yellow
            }
        }
        # Micro-delay to ensure file handles are released before forcefully removing the directory
        Start-Sleep -Milliseconds 100
        # Silently continue if background AV locks the empty folder to prevent a false-positive terminating error
        Remove-Item -Path $tempDir -Recurse -Force -ErrorAction SilentlyContinue
    }
}
