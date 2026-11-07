<#
.SYNOPSIS
    Deploys compose stacks to the Dell server using Infisical Zero-Trust Machine Identities.
.DESCRIPTION
    Validates syntax, SCPs compose files, requests an ephemeral token, and injects secrets natively into Docker memory.
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-09-17
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-zA-Z0-9_-]+[/\\][a-zA-Z0-9_-]+$')]
    [string]$Stack,
    
    [Parameter(Mandatory = $false)]
    [string]$ProjectId,

    [ValidateSet('Auto', 'Infisical', 'Standard')]
    [string]$DeploymentMode = 'Auto',

    [ValidateSet('up -d', 'down', 'pull', 'restart')]
    [string]$Action = 'up -d',

    [switch]$DryRun,

    [switch]$ForceRecreate,

    [string]$Domain = "https://secrets.sythsaz.ca",

    [switch]$MonitorLogs
)

$ErrorActionPreference = 'Stop'

if ($Stack -eq "dell-server/security") {
    Write-Host "Routing Root of Trust stack (security) to SOPS deployment pipeline..." -ForegroundColor Magenta
    & (Join-Path $PSScriptRoot "deploy-remote-sops.ps1") -Stack $Stack -Action $Action -DryRun:$DryRun -MonitorLogs:$MonitorLogs -ForceRecreate:$ForceRecreate
    return
}

$stackParts = $Stack -split "[/\\]"
$domainPart = $stackParts[0]
$service = $stackParts[1]

if ($DeploymentMode -eq 'Auto') {
    $DeploymentMode = 'Infisical'
}

if ($domainPart -eq "Justice") {
    $remoteUser = "jusparr"
    $remoteHost = "100.79.211.101"
    $remoteBaseDir = "/home/jusparr/docker/stacks"
    if ([string]::IsNullOrWhiteSpace($ProjectId)) {
        $ProjectId = "ed163e38-c457-4f41-a802-43febf927983"
    }
}
elseif ($domainPart -eq "homeassistant-pos") {
    $remoteUser = "hassio"
    $remoteHost = "homeassistant-pos"
    $remoteBaseDir = "/home/hassio/docker"
}
elseif ($domainPart -eq "dell-server") {
    $remoteUser = "hassio"
    $remoteHost = "10.0.20.221"
    $remoteBaseDir = "/home/hassio/docker"
}
else {
    throw "Unknown stack domain '$domainPart'. Expected 'Justice', 'homeassistant-pos', or 'dell-server'."
}

if ($DeploymentMode -eq 'Infisical' -and [string]::IsNullOrWhiteSpace($ProjectId)) {
    throw "Error: -ProjectId is required for all Infisical-managed stacks ($domainPart). Use -DeploymentMode Standard if deploying without Infisical."
}

$sshTarget = "${remoteUser}@${remoteHost}"
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"

$sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=10", "-o", "ServerAliveInterval=15", "-o", "ServerAliveCountMax=3", "-n", $sshTarget)

if ($Action -match "down") {
    if (-not $DryRun -and -not $PSCmdlet.ShouldProcess($Stack, "Execute destructive action: $Action")) {
        Write-Host "Destructive action aborted." -ForegroundColor Red
        return
    }
}

$localStackPath = Join-Path (Join-Path $PSScriptRoot "..") "stacks\$domainPart\$service"
$remoteStackPath = "$remoteBaseDir/$domainPart/$service"
$composeFile = Join-Path $localStackPath "compose.yaml"

if (-not (Test-Path $composeFile)) {
    throw "Stack compose file not found at $composeFile"
}

Write-Host "Verifying remote Docker daemon and Compose V2 plugin on $remoteHost..."
if (-not $DryRun) {
    ssh @sshArgs "docker info >/dev/null 2>&1 && docker compose version >/dev/null 2>&1"
    if ($LASTEXITCODE -ne 0) { throw "Docker or Compose V2 not available on remote host." }
}

Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Starting deployment of $Stack (Action: $Action)"

$infisicalPath = "/$service"
$isHomeAssistant = $false
$haSecretsPath = ""
if ($service -eq "home-assistant") {
    if ($domainPart -eq "Justice") {
        $haSecretsPath = "/home-assistant/secrets"
    }
    else {
        $haSecretsPath = "/infrastructure/home-assistant/secrets"
    }
    $isHomeAssistant = $true
}

# Parse compose.yaml for explicit container_name entries and service names to prevent container name conflicts
$composeLines = Get-Content -Path $composeFile
$explicitContainerNames = @()
$serviceNames = @()
$inServicesBlock = $false

foreach ($line in $composeLines) {
    if ($line -match '^\s*container_name:\s*[''"]?([a-zA-Z0-9_.-]+)[''"]?\s*$') {
        $explicitContainerNames += $Matches[1]
    }
    if ($line -match '^services:\s*$') {
        $inServicesBlock = $true
        continue
    }
    if ($inServicesBlock -and $line -match '^[a-zA-Z0-9_-]+:') {
        $inServicesBlock = $false
        continue
    }
    if ($inServicesBlock -and $line -match '^\s{2}([a-zA-Z0-9_-]+):\s*$') {
        $serviceNames += $Matches[1]
    }
}

$conflictNames = @($explicitContainerNames)
foreach ($svc in $serviceNames) {
    $conflictNames += "${service}-${svc}-1"
    $conflictNames += "${service}_${svc}_1"
    if ($svc -notin @('db', 'redis')) {
        $conflictNames += $svc
        $conflictNames += "docker-${svc}-1"
        $conflictNames += "docker_${svc}_1"
    }
}
$conflictNames = @($conflictNames | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | Select-Object -Unique)
$nonGenericServices = @($serviceNames | Where-Object { $_ -notin @('db', 'redis') } | Select-Object -Unique)

$conflictCleanupCmds = @()
if ($conflictNames.Count -gt 0) {
    $cnameList = $conflictNames -join " "
    $conflictCleanupCmds += "for cname in $cnameList; do if [ -n `"`$(docker ps -a --filter name=^/`${cname}`$ -q)`" ] && [ -z `"`$(docker ps -a --filter name=^/`${cname}`$ --filter label=com.docker.compose.project=$service -q)`" ]; then echo `"Removing conflicting container: `$cname`" && docker rm -f `"`$cname`"; fi; done"
}
if ($nonGenericServices.Count -gt 0) {
    $svcList = $nonGenericServices -join " "
    $conflictCleanupCmds += "for svc in $svcList; do for cid in `$(docker ps -a --filter label=com.docker.compose.service=`${svc} -q); do if [ -z `"`$(docker ps -a --filter id=`${cid} --filter label=com.docker.compose.project=$service -q)`" ]; then echo `"Removing legacy container (`$cid) for service: `$svc`" && docker rm -f `"`$cid`"; fi; done; done"
}
if ($domainPart -eq "Justice") {
    if ($service -eq "home-assistant") {
        $conflictCleanupCmds += "if [ -n `"`$(docker ps -a --filter name=^/emqx`$ -q)`" ]; then echo `"Removing legacy EMQX broker to free port 1883...`" && docker rm -f emqx; fi"
    }
    elseif ($service -eq "observability") {
        $conflictCleanupCmds += "for cname in ha-watchtower-1 ha-scrutiny-1; do if [ -n `"`$(docker ps -a --filter name=^/`${cname}`$ -q)`" ]; then echo `"Removing legacy container: `$cname`" && docker rm -f `"`$cname`"; fi; done"
    }
    elseif ($service -eq "media") {
        $conflictCleanupCmds += "for cname in ha-aircast-1 mediamtx; do if [ -n `"`$(docker ps -a --filter name=^/`${cname}`$ -q)`" ] && [ -z `"`$(docker ps -a --filter name=^/`${cname}`$ --filter label=com.docker.compose.project=media -q)`" ]; then echo `"Removing legacy container: `$cname`" && docker rm -f `"`$cname`"; fi; done"
    }
    elseif ($service -eq "mcp") {
        $conflictCleanupCmds += "for cname in ha-mcp docker-mcp-gateway; do if [ -n `"`$(docker ps -a --filter name=^/`${cname}`$ -q)`" ] && [ -z `"`$(docker ps -a --filter name=^/`${cname}`$ --filter label=com.docker.compose.project=mcp -q)`" ]; then echo `"Removing legacy container: `$cname`" && docker rm -f `"`$cname`"; fi; done"
    }
}

$stackItems = Get-ChildItem -Path $localStackPath | Where-Object { $_.Name -ne "secrets" -and $_.Name -ne ".env" }

$hashExports = @()
if ($stackItems.Count -gt 0) {
    $configFiles = Get-ChildItem -Path $localStackPath -File -Recurse | Where-Object { 
        $_.FullName -notmatch '[\\/]secrets[\\/]' -and 
        $_.Name -ne ".env" -and 
        $_.Name -notmatch '^docker-compose' -and 
        $_.Name -notmatch '^compose\.y' 
    } | Sort-Object FullName

    $hashString = ""
    foreach ($file in $configFiles) {
        $hashString += (Get-FileHash $file.FullName -Algorithm MD5).Hash
    }

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
}

$commonEnvCmds = @(
    'if [ -f /home/jusparr/docker/.env ]; then set -a; . /home/jusparr/docker/.env; set +a; fi',
    'if [ -f ../.env ]; then set -a; . ../.env; set +a; fi',
    'if [ -f .env ]; then set -a; . .env; set +a; fi',
    'export TZ="${TZ:-America/Edmonton}"',
    'export PUID="${PUID:-1001}"',
    'export PGID="${PGID:-${GUID:-1001}}"'
)

$remoteCmd = @()

if ($DeploymentMode -eq 'Infisical') {
    $remoteCmd += "export INFISICAL_DOMAIN=`"$Domain`""
    $remoteCmd += "if [ ! -f ~/.infisical-machine.env ]; then echo `"[!] Error: ~/.infisical-machine.env not found on remote host. Please create it with INFISICAL_UNIVERSAL_AUTH_CLIENT_ID and INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET.`"; exit 1; fi"
    $remoteCmd += "chmod 600 ~/.infisical-machine.env"
    $remoteCmd += "cd `"$remoteStackPath`""
    $remoteCmd += "rm -f docker-compose.yml docker-compose.yaml"
    $remoteCmd += "find . -type f -name `"*.sh`" -exec sed -i 's/\r`$//' {} + -exec chmod +x {} +"
    $remoteCmd += $commonEnvCmds
    $remoteCmd += "source ~/.infisical-machine.env"
    $remoteCmd += "export INFISICAL_TOKEN=`$(infisical login --domain `"`$INFISICAL_DOMAIN`" --method=universal-auth --client-id `"`$INFISICAL_UNIVERSAL_AUTH_CLIENT_ID`" --client-secret `"`$INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET`" --silent --plain)"
    if ($hashExports.Count -gt 0) {
        $remoteCmd += $hashExports
    }
    if ($isHomeAssistant) {
        $remoteCmd += "mkdir -p config/.ssh config/automations config/scripts config/pyscript config/python_scripts config/templates"
        $remoteCmd += "if [ -f config/.ssh/id_ed25519 ]; then chmod 600 config/.ssh/id_ed25519; fi"
        $remoteCmd += "if [ -d config/secrets.yaml ]; then rm -rf config/secrets.yaml; fi"
        $remoteCmd += "infisical export --domain `"`$INFISICAL_DOMAIN`" --projectId `"$ProjectId`" --env prod --path `"$haSecretsPath`" --format yaml > config/secrets.yaml"
        $remoteCmd += "chmod 600 config/secrets.yaml"
    }

    if ($Action -eq "up -d") {
        $remoteCmd += "infisical run --domain `"`$INFISICAL_DOMAIN`" --projectId `"$ProjectId`" --env prod --path `"$infisicalPath`" -- docker compose -f compose.yaml pull"
        if ($conflictCleanupCmds.Count -gt 0) {
            $remoteCmd += $conflictCleanupCmds
        }
        if ($ForceRecreate) {
            $remoteCmd += "infisical run --domain `"`$INFISICAL_DOMAIN`" --projectId `"$ProjectId`" --env prod --path `"$infisicalPath`" -- docker compose -f compose.yaml up -d --remove-orphans --force-recreate --wait"
        } else {
            $remoteCmd += "infisical run --domain `"`$INFISICAL_DOMAIN`" --projectId `"$ProjectId`" --env prod --path `"$infisicalPath`" -- docker compose -f compose.yaml up -d --remove-orphans --wait"
        }
    }
    else {
        $remoteCmd += "infisical run --domain `"`$INFISICAL_DOMAIN`" --projectId `"$ProjectId`" --env prod --path `"$infisicalPath`" -- docker compose -f compose.yaml $Action"
    }
}
else {
    $remoteCmd += "cd `"$remoteStackPath`""
    $remoteCmd += "rm -f docker-compose.yml docker-compose.yaml"
    $remoteCmd += "find . -type f -name `"*.sh`" -exec sed -i 's/\r`$//' {} + -exec chmod +x {} +"
    $remoteCmd += $commonEnvCmds
    if ($hashExports.Count -gt 0) {
        $remoteCmd += $hashExports
    }
    if ($isHomeAssistant) {
        $remoteCmd += "mkdir -p config/.ssh config/automations config/scripts config/pyscript config/python_scripts config/templates"
        $remoteCmd += "if [ -f config/.ssh/id_ed25519 ]; then chmod 600 config/.ssh/id_ed25519; fi"
        $remoteCmd += "if [ -d config/secrets.yaml ]; then rm -rf config/secrets.yaml; fi"
        # Preserve existing secrets or copy from persistent ha_config if present; ensure file exists so Docker never creates a directory mount
        $remoteCmd += "if [ -f /home/jusparr/docker/ha_config/secrets.yaml ] && [ ! -f config/secrets.yaml ]; then cp /home/jusparr/docker/ha_config/secrets.yaml config/secrets.yaml; fi"
        $remoteCmd += "if [ ! -f config/secrets.yaml ]; then touch config/secrets.yaml; fi"
        $remoteCmd += "chmod 600 config/secrets.yaml"
    }

    if ($Action -eq "up -d") {
        $remoteCmd += "docker compose -f compose.yaml pull"
        if ($conflictCleanupCmds.Count -gt 0) {
            $remoteCmd += $conflictCleanupCmds
        }
        if ($ForceRecreate) {
            $remoteCmd += "docker compose -f compose.yaml up -d --remove-orphans --force-recreate --wait"
        } else {
            $remoteCmd += "docker compose -f compose.yaml up -d --remove-orphans --wait"
        }
    }
    else {
        $remoteCmd += "docker compose -f compose.yaml $Action"
    }
}

$remoteCmdString = $remoteCmd -join " && "

if ($DryRun) {
    Write-Host "DRY RUN: DeploymentMode = $DeploymentMode" -ForegroundColor Yellow
    Write-Host "DRY RUN: Target Host    = $sshTarget" -ForegroundColor Yellow
    Write-Host "DRY RUN: Remote Path    = $remoteStackPath" -ForegroundColor Yellow
    Write-Host "DRY RUN: Local Items    = $($stackItems.Count) item(s) would be synced" -ForegroundColor Yellow
    if ($hashExports.Count -gt 0) {
        Write-Host "DRY RUN: Config Hash    = $($hashExports -join ' ')" -ForegroundColor Yellow
    }
    Write-Host "DRY RUN: Remote Command = $remoteCmdString" -ForegroundColor Yellow
    Write-Host "DRY RUN: Skipping execution on remote host." -ForegroundColor Yellow
    return
}

Write-Host "Preparing remote directory..."
ssh @sshArgs "mkdir -p `"$remoteStackPath`""
if ($LASTEXITCODE -ne 0) { throw "Failed to create remote directory $remoteStackPath (exit code $LASTEXITCODE)" }

Write-Host "Copying files via SCP..."
if ($stackItems.Count -gt 0) {
    $scpArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=10", "-o", "ServerAliveInterval=15", "-o", "ServerAliveCountMax=3", "-r")
    $scpArgs += $stackItems | ForEach-Object { "$($_.FullName)" }
    $scpArgs += "${sshTarget}:${remoteStackPath}/"
    & scp @scpArgs
    if ($LASTEXITCODE -ne 0) { throw "SCP transfer failed with exit code $LASTEXITCODE" }
}

if ($isHomeAssistant) {
    $keyCheck = ssh @sshArgs "test -f `"${remoteStackPath}/config/.ssh/id_ed25519`" && echo 1 || echo 0"
    if ($keyCheck -ne "1") {
        Write-Host "Injecting deployment SSH key into Home Assistant container..." -ForegroundColor Magenta
        ssh @sshArgs "mkdir -p `"${remoteStackPath}/config/.ssh`""
        $scpArgsKey = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=10", "-o", "ServerAliveInterval=15", "-o", "ServerAliveCountMax=3", "-q")
        $scpArgsKey += $sshKey
        $scpArgsKey += "${sshTarget}:${remoteStackPath}/config/.ssh/id_ed25519"
        & scp @scpArgsKey
        if ($LASTEXITCODE -ne 0) { throw "SSH key injection failed with exit code $LASTEXITCODE" }
    }
}

if ($DeploymentMode -eq 'Infisical') {
    Write-Host "Executing deployment via Infisical Zero-Trust Agent on remote host..." -ForegroundColor Cyan
} else {
    Write-Host "Executing deployment via Standard Docker Compose on remote host..." -ForegroundColor Cyan
}

ssh @sshArgs "$remoteCmdString"
if ($LASTEXITCODE -ne 0) { throw "Execution failed with exit code $LASTEXITCODE" }

if ($MonitorLogs -and -not $DryRun -and ($Action -eq 'up -d' -or $Action -eq 'restart')) {
    & (Join-Path $PSScriptRoot "monitor-remote.ps1") -Stack $Stack -NewWindow
}

Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Deployment complete." -ForegroundColor Green
