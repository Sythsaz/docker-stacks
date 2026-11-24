<#
.SYNOPSIS
    Visually diffs compiled local vs remote Docker compose stacks using VS Code.
    Sanitizes absolute path expansions, cross-OS line endings, and path separators
    to eliminate all false-positive drift.
.EXAMPLE
    .\scripts\compare-stacks.ps1 -Stack "all"
#>
[CmdletBinding()]
param(
    [string[]]$Stack = @('all')
)

$ErrorActionPreference = 'Stop'

# Domain-to-host mapping matching deploy-remote.ps1
$localBase = "$env:USERPROFILE\Docker\stacks"
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"
$domainMap = @{
    "dell-server"       = @{ User = "hassio";  Host = "10.0.20.221";    RemoteBase = "/home/hassio/docker" }
    "homeassistant-pos" = @{ User = "hassio";  Host = "10.0.20.222";    RemoteBase = "/home/hassio/docker" }
    "Justice"           = @{ User = "jusparr"; Host = "100.79.211.101"; RemoteBase = "/home/jusparr/docker/stacks" }
}

# Map SOPS Age key to the correct infrastructure path
$env:SOPS_AGE_KEY_FILE = "$env:USERPROFILE\.config\sops\age\keys.txt"

# Clean temp directory to prevent indefinite clutter accumulation
$diffTempDir = Join-Path ([System.IO.Path]::GetTempPath()) "docker-diffs"
if (Test-Path $diffTempDir) { Remove-Item -Path "$diffTempDir\*" -Recurse -Force -ErrorAction SilentlyContinue }
else { New-Item -ItemType Directory -Path $diffTempDir -Force | Out-Null }

# Ensure BOM-less UTF-8 encoding for Linux compatibility in VS Code
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$targetStacks = @()
if ($Stack -contains 'all') {
    foreach ($dom in @("dell-server", "homeassistant-pos", "Justice")) {
        $domPath = Join-Path $localBase $dom
        if (Test-Path $domPath) {
            $targetStacks += Get-ChildItem -Path $domPath -Directory | ForEach-Object { "$dom/$($_.Name)" }
        }
    }
}
else {
    $targetStacks = $Stack
}

foreach ($s in $targetStacks) {
    $domainPart = ($s -split '[/\\]')[0]
    if (-not $domainMap.ContainsKey($domainPart)) {
        Write-Host "[SKIP] Unknown domain '$domainPart' for stack $s" -ForegroundColor Yellow
        continue
    }
    $targetInfo = $domainMap[$domainPart]
    $remoteUser = $targetInfo.User
    $remoteHost = $targetInfo.Host
    $remoteBase = $targetInfo.RemoteBase
    $sshArgs = @("-q", "-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=5", "${remoteUser}@${remoteHost}")

    # Initialize paths BEFORE the compilation logic
    $localDir = Join-Path $localBase ($s -replace '/', '\')
    $remoteDir = "$remoteBase/$s"
    
    if (-not (Test-Path "$localDir\compose.yaml")) {
        Write-Host "[SKIP] Local compose.yaml not found for $s" -ForegroundColor Yellow
        continue
    }

    if ($s -eq "dell-server/security") {
        Write-Host "Compiling SOPS-encrypted Root of Trust: $s" -ForegroundColor Magenta
        
        $serviceName = ($s -split '[/\\]')[-1]
        $secTemp = Join-Path $diffTempDir $serviceName
        New-Item -ItemType Directory -Path $secTemp -Force | Out-Null
        Copy-Item -Path "$localDir\*" -Destination $secTemp -Recurse -Force

        $encFiles = Get-ChildItem -Path "$localDir\secrets" -Filter "*.enc"
        New-Item -ItemType Directory -Path "$secTemp\secrets" -Force | Out-Null
        
        # Decrypt locally
        foreach ($file in $encFiles) {
            $decName = $file.Name -replace '\.enc$', ''
            sops --decrypt --output "$secTemp\secrets\$decName" "$($file.FullName)"
        }

        # Rewrite local compose to mount decrypted secrets
        $composeContent = (Get-Content "$secTemp\compose.yaml" -Raw -Encoding UTF8) -replace '/dev/shm/([a-zA-Z0-9_.-]+)', './secrets/$1'
        [System.IO.File]::WriteAllText("$secTemp\compose.yaml", $composeContent, $utf8NoBom)
        
        $localConfig = (docker compose -f "$secTemp\compose.yaml" config 2>$null) -join "`n"

        # Transfer to remote RAM disk for compilation (bypasses persistent storage)
        # Wrapped in try/finally to guarantee secret cleanup from /dev/shm on error
        $remoteSecretNames = @()
        try {
            foreach ($file in $encFiles) {
                $decName = $file.Name -replace '\.enc$', ''
                $remoteSecretNames += $decName
                # Stream via CMD stdin with install -m 600 to avoid SCP umask race and PS line-endings
                $localPath = "$secTemp\secrets\$decName"
                cmd.exe /c "ssh -i `"$sshKey`" -o BatchMode=yes -o StrictHostKeyChecking=yes -q ${remoteUser}@${remoteHost} install -m 600 /dev/stdin /dev/shm/$decName < `"$localPath`""
            }

            $remoteConfig = (ssh @sshArgs "cd $remoteDir && docker compose config 2>/dev/null") -join "`n"
        }
        finally {
            # Guaranteed remote RAM disk cleanup — runs even on SSH/Docker errors
            foreach ($decName in $remoteSecretNames) {
                ssh @sshArgs "rm -f /dev/shm/$decName" 2>$null
            }
            # Guaranteed local temp cleanup
            if (Test-Path $secTemp) {
                Remove-Item -Path $secTemp -Recurse -Force -ErrorAction SilentlyContinue
            }
        }

        if ([string]::IsNullOrWhiteSpace($localConfig) -or [string]::IsNullOrWhiteSpace($remoteConfig)) {
            Write-Host "  [ERROR] Compilation failed for $s." -ForegroundColor Red
            continue
        }

        # Normalize local secret paths to match remote /dev/shm standard for diffing
        $secTempFwd = ($secTemp -replace '\\', '/') + "/"
        $secRegex = [regex]::Escape($secTempFwd + "secrets/")
        $localConfig = $localConfig -replace "(?i)$secRegex", "/dev/shm/"
        
        # Override $localDir temporarily so Step 2 sanitization works seamlessly
        $localDir = $secTemp
    } 
    else {
        Write-Host "Compiling and evaluating drift for: $s" -ForegroundColor Cyan
        
        $localConfig = (docker compose -f "$localDir\compose.yaml" config 2>$null) -join "`n"
        $remoteConfig = (ssh @sshArgs "cd $remoteDir && docker compose config 2>/dev/null") -join "`n"
        
        if ([string]::IsNullOrWhiteSpace($localConfig)) {
            Write-Host "  [ERROR] Local compilation failed for $s. Check syntax." -ForegroundColor Red
            continue
        }
        if ([string]::IsNullOrWhiteSpace($remoteConfig)) {
            Write-Host "  [ERROR] Remote compilation failed or stack does not exist on Dell server for $s" -ForegroundColor Red
            continue
        }
    }

    # 2. Sanitize absolute paths to relative paths FIRST
    $localDirRegex = [regex]::Escape($localDir) + "[/\\]"
    $localConfig = $localConfig -replace "(?i)$localDirRegex", "./"
    
    $remoteRegex = [regex]::Escape("$remoteDir/")
    $remoteConfig = $remoteConfig -replace "(?i)$remoteRegex", "./"

    # 3. Normalize remaining Windows backslashes to forward slashes ONLY in paths.
    # By targeting backslashes preceded by "./", we safely preserve regex labels like \d
    $localConfig = [regex]::Replace($localConfig, '(?<=\./[^\s""]*)\\', '/')

    # Normalize line endings and whitespace to prevent false-positive cross-platform drift
    $normLocal = ($localConfig -replace "`r", "").Trim()
    $normRemote = ($remoteConfig -replace "`r", "").Trim()

    # 4. Compare strictly. Only launch VS Code if drift is detected.
    if ($normLocal -ceq $normRemote) {
        Write-Host "  [SYNCED] No configuration drift detected." -ForegroundColor DarkGreen
    }
    else {
        Write-Host "  [DRIFT DETECTED] Launching VS Code..." -ForegroundColor Yellow
        $safeName = $s -replace '[/\\]', '-'
        $localTemp = Join-Path $diffTempDir "local_$safeName.yaml"
        $remoteTemp = Join-Path $diffTempDir "remote_$safeName.yaml"

        [System.IO.File]::WriteAllText($localTemp, $localConfig, $utf8NoBom)
        [System.IO.File]::WriteAllText($remoteTemp, $remoteConfig, $utf8NoBom)

        code --diff $localTemp $remoteTemp
    }
}

Write-Host "`n[COMPLETE] Drift evaluation finished." -ForegroundColor Green
