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
    # Enforce strict <domain>/<service> naming convention and support Windows tab-completion slashes[cite: 1]
    [ValidatePattern('^[a-zA-Z0-9_-]+[/\\][a-zA-Z0-9_-]+$')]
    [string]$Stack,

    [ValidateSet('up -d', 'down', 'pull', 'restart')]
    [string]$Action = 'up -d',

    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

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
$sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=5", $sshTarget)

# Destructive operation safeguard
if ($Action -match "down") {
    if (-not $DryRun -and -not $PSCmdlet.ShouldProcess($Stack, "Execute destructive action: $Action")) {
        Write-Host "Destructive action aborted." -ForegroundColor Red
        return
    }
}

# Isolate path formatting: strictly OS-native for local, forward-slash for remote[cite: 1]
$remoteStack = $Stack -replace '\\', '/'
$remoteStackDir = "$remoteBaseDir/$remoteStack"

$localStack = $Stack -replace '/', '\'
$localStackDir = "$env:USERPROFILE\Docker\stacks\$localStack"

if (-not (Test-Path "$localStackDir\compose.yaml")) {
    throw "compose.yaml not found in $localStackDir"
}

# Fail-fast: Validate remote Docker daemon connectivity and Compose V2 presence
Write-Host "Verifying remote Docker daemon and Compose V2 plugin on $remoteHost..."
if (-not $DryRun) {
    ssh $sshArgs "docker info >/dev/null 2>&1 && docker compose version >/dev/null 2>&1"
    if ($LASTEXITCODE -ne 0) {
        throw "Pre-flight failed on $remoteHost. Verify Docker is running, the user has socket access, and the Compose V2 plugin is installed."
    }
}

Write-Host "[$(Get-Date -f 'yyyy-MM-dd HH:mm:ss')] Starting deployment of $remoteStack (Action: $Action)" -ForegroundColor Cyan

# Mitigate predictable temp directory attacks by utilizing a GUID
$tempDir = Join-Path ([System.IO.Path]::GetTempPath()) "docker-deploy-$stackName-$([guid]::NewGuid().ToString().Substring(0,8))"

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
    # Explicitly exclude local 'data' mounts and raw 'secrets' to prevent raw .enc leakage[cite: 1].
    Get-ChildItem -Path $localStackDir -Force | Where-Object { $_.Name -notin @('data', 'secrets') } | Copy-Item -Destination $tempDir -Recurse -Force
    
    $secretsDir = "$localStackDir\secrets"
    if (Test-Path $secretsDir) {
        New-Item -ItemType Directory -Path "$tempDir\secrets" -Force | Out-Null
        $encFiles = Get-ChildItem -Path $secretsDir -Filter "*.enc"
        
        foreach ($file in $encFiles) {
            $decryptedName = $file.Name -replace '\.enc$', ''
            $decryptedPath = "$tempDir\secrets\$decryptedName"
            
            Write-Host "Decrypting secret: $($file.Name) -> $decryptedName"
            if ($file.Length -eq 0) {
                throw "Corrupt encrypted secret: $($file.FullName) is 0 bytes. Check Git history for failed encryptions."
            }
            
            # Remove the if (-not $DryRun) condition here. 
            # We MUST decrypt locally to assemble a complete temp directory for syntax validation.
            
            # Security: Decrypt locally, transfer via SCP over SSH
            # Utilize SOPS native --output flag to prevent PowerShell UTF-16LE BOM encoding corruption on Linux
            sops --decrypt --output "$decryptedPath" "$($file.FullName)"
            
            # Enforce strict exit code validation on decryption
            if ($LASTEXITCODE -ne 0) { 
                throw "SOPS decryption failed for $($file.Name). Verify your age key is loaded." 
            }
        }
    }

    # Fail-fast: Validate Compose syntax AFTER decryption using the assembled temp directory
    Write-Host "Validating assembled compose specification syntax..."
    docker compose -f "$tempDir\compose.yaml" config -q
    if ($LASTEXITCODE -ne 0) {
        throw "Assembled compose validation failed. Check syntax in $localStackDir\compose.yaml or verify all mapped secrets decrypted successfully."
    }
    
    # Defense-in-depth: Force recursive EFS application to catch files that bypassed inheritance during copy/decryption
    cipher.exe /e /a /s:"$tempDir" | Out-Null
    
    Write-Host "Preparing remote directory..."
    if (-not $DryRun) {
        # Dynamically append .env purge command if it was removed locally to prevent configuration drift
        $staleEnvPurge = if (-not (Test-Path "$localStackDir\.env")) { "rm -f `"$remoteStackDir/.env`" && " } else { "" }
        
        # Purge legacy compose files to enforce canonical naming rules, plus stale secrets/directories[cite: 1]
        ssh $sshArgs "$staleEnvPurge rm -f `"$remoteStackDir/docker-compose.yml`" `"$remoteStackDir/docker-compose.yaml`" && rm -rf `"$remoteStackDir/secrets`" && mkdir -p `"$remoteStackDir/secrets`" `"$remoteStackDir/data`" && chmod 700 `"$remoteStackDir/secrets`""
        
        # Enforce exit code validation to prevent SCP failure cascade
        if ($LASTEXITCODE -ne 0) { throw "Remote directory preparation failed with exit code $LASTEXITCODE" }
    }
    else {
        $staleEnvPurge = if (-not (Test-Path "$localStackDir\.env")) { "rm -f `"$remoteStackDir/.env`" && " } else { "" }
        Write-Host "[DRY-RUN] Would execute: ssh -i $sshKey -o BatchMode=yes -o StrictHostKeyChecking=yes $sshTarget `"$staleEnvPurge rm -rf \"$remoteStackDir/secrets\" && mkdir -p \"$remoteStackDir/secrets\" \"$remoteStackDir/data\" && chmod 700 \"$remoteStackDir/secrets\"`"" -ForegroundColor Yellow
    }

    Write-Host "Copying files via SCP..."
    if (-not $DryRun) {
        # Using '.' copies the contents of the directory without wildcard translation issues
        # Enforce strict host key checking and timeouts on SCP to prevent MITM and hangs
        scp -i $sshKey -o "BatchMode=yes" -o "StrictHostKeyChecking=yes" -o "ConnectTimeout=5" -r "$tempDir/." "${sshTarget}:${remoteStackDir}/"
        # Enforce exit code validation to prevent SCP failure cascade
        if ($LASTEXITCODE -ne 0) { throw "SCP transfer failed with exit code $LASTEXITCODE" }
        
        # Ensure secrets are group/world readable so dropped-privilege containers (uid 999) can read them
        ssh $sshArgs "chmod 644 '$remoteStackDir/secrets/'* 2>/dev/null || true"
        
        # Enforce 600 permissions on all transferred remote secrets and .env files[cite: 1]
        ssh $sshArgs "if [ -f `"$remoteStackDir/.env`" ]; then chmod 600 `"$remoteStackDir/.env`"; fi && if [ -d `"$remoteStackDir/secrets`" ]; then find `"$remoteStackDir/secrets`" -type f -exec chmod 600 {} +; fi"
    }
    else {
        Write-Host "[DRY-RUN] Would execute: scp -i $sshKey -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=5 -r `"$tempDir/.`" `"${sshTarget}:${remoteStackDir}/`"" -ForegroundColor Yellow
    }

    Write-Host "Executing docker compose $Action on remote host..."
    if (-not $DryRun) {
        # Utilize native Compose V2 arguments for atomic pulls and thorough orphan cleanup[cite: 1]
        $actionCmd = switch ($Action) {
            'up -d' { "up -d --pull always --remove-orphans" }
            'down' { "down --remove-orphans" }
            Default { $Action }
        }
        
        ssh $sshArgs "cd `"$remoteStackDir`" && docker compose -f compose.yaml $actionCmd"
        if ($LASTEXITCODE -ne 0) { throw "SSH execution failed with exit code $LASTEXITCODE" }

    }
    else {
        $actionCmd = switch ($Action) {
            'up -d' { "up -d --pull always --remove-orphans" }
            'down' { "down --remove-orphans" }
            Default { $Action }
        }
        Write-Host "[DRY-RUN] Would execute: ssh -i $sshKey -o BatchMode=yes -o StrictHostKeyChecking=yes $sshTarget `"cd \"$remoteStackDir\" && docker compose -f compose.yaml $actionCmd`"" -ForegroundColor Yellow
    }

    Write-Host "[$(Get-Date -f 'yyyy-MM-dd HH:mm:ss')] Deployment complete." -ForegroundColor Green
}
finally {
    if (Test-Path $tempDir) {
        Write-Host "Securely wiping decrypted temp files at $tempDir..."
        # Forensic cleanup: Zero out plaintext files before deletion to prevent disk recovery.
        # -Force is mandatory to ensure hidden files like .env are not skipped[cite: 1].
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