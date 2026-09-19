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
    
    [Parameter(Mandatory = $true)]
    [string]$ProjectId,

    [ValidateSet('up -d', 'down', 'pull', 'restart')]
    [string]$Action = 'up -d',

    [switch]$DryRun,

    [string]$Domain = "https://secrets.sythsaz.ca"
)

$ErrorActionPreference = 'Stop'

if ($Stack -eq "dell-server/security") {
    Write-Host "Routing Root of Trust stack (security) to SOPS deployment pipeline..." -ForegroundColor Magenta
    & (Join-Path $PSScriptRoot "deploy-remote-sops.ps1") -Stack $Stack -Action $Action -DryRun:$DryRun
    return
}

$remoteUser = "hassio"
$remoteHost = "10.0.20.221"
$remoteBaseDir = "/home/hassio/docker"
$sshTarget = "${remoteUser}@${remoteHost}"
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"

$sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=5", $sshTarget)

if ($Action -match "down") {
    if (-not $DryRun -and -not $PSCmdlet.ShouldProcess($Stack, "Execute destructive action: $Action")) {
        Write-Host "Destructive action aborted." -ForegroundColor Red
        return
    }
}

$stackParts = $Stack -split "[/\\]"
$domainPart = $stackParts[0]
$service = $stackParts[1]
$localStackPath = Join-Path (Join-Path $PSScriptRoot "..") "stacks\$domainPart\$service"
$remoteStackPath = "$remoteBaseDir/$domainPart/$service"
$composeFile = Join-Path $localStackPath "compose.yaml"

if (-not (Test-Path $composeFile)) {
    throw "Stack compose file not found at $composeFile"
}

Write-Host "Verifying remote Docker daemon and Compose V2 plugin on $remoteHost..."
ssh @sshArgs "docker info >/dev/null 2>&1 && docker compose version >/dev/null 2>&1"
if ($LASTEXITCODE -ne 0) { throw "Docker or Compose V2 not available on remote host." }

Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Starting deployment of $Stack (Action: $Action)"

$infisicalPath = "/$service"
$isHomeAssistant = $false
if ($service -eq "home-assistant") {
    $infisicalPath = "/infrastructure/home-assistant"
    $isHomeAssistant = $true
}

Write-Host "Preparing remote directory..."
ssh @sshArgs "mkdir -p `"$remoteStackPath`""

Write-Host "Copying files via SCP..."
$configDir = Join-Path $localStackPath "config"
if (Test-Path $configDir) {
    scp -i $sshKey -r "$configDir" "${sshTarget}:${remoteStackPath}/"
}
scp -i $sshKey "$composeFile" "${sshTarget}:${remoteStackPath}/"

if ($DryRun) {
    Write-Host "DRY RUN: Skipping execution on remote host." -ForegroundColor Yellow
    return
}

Write-Host "Executing deployment via Infisical Zero-Trust Agent on remote host..." -ForegroundColor Cyan

$remoteCmd = @()
$remoteCmd += "export INFISICAL_DOMAIN=`"$Domain`""
$remoteCmd += "if [ ! -f ~/.infisical-machine.env ]; then echo `"[!] Error: ~/.infisical-machine.env not found on remote host. Please create it with INFISICAL_UNIVERSAL_AUTH_CLIENT_ID and INFISICAL_UNIVERSAL_AUTH_CLIENT_SECRET.`"; exit 1; fi"
$remoteCmd += "chmod 600 ~/.infisical-machine.env"
$remoteCmd += "cd `"$remoteStackPath`""
$remoteCmd += "source ~/.infisical-machine.env"
$remoteCmd += "export INFISICAL_TOKEN=`$(infisical login --method=universal-auth --silent --plain)"

if ($isHomeAssistant) {
    Write-Host "Handling Home Assistant special secrets.yaml render..." -ForegroundColor Magenta
    $remoteCmd += "mkdir -p config"
    $remoteCmd += "infisical export --projectId `"$ProjectId`" --env prod --path /infrastructure/home-assistant --format yaml > config/secrets.yaml"
    $remoteCmd += "chmod 600 config/secrets.yaml"
}

if ($Action -eq "up -d") {
    $remoteCmd += "infisical run --projectId `"$ProjectId`" --env prod --path `"$infisicalPath`" -- docker compose pull"
    $remoteCmd += "infisical run --projectId `"$ProjectId`" --env prod --path `"$infisicalPath`" -- docker compose up -d"
} else {
    $remoteCmd += "infisical run --projectId `"$ProjectId`" --env prod --path `"$infisicalPath`" -- docker compose $Action"
}

$remoteCmdString = $remoteCmd -join " && "

ssh @sshArgs "$remoteCmdString"
if ($LASTEXITCODE -ne 0) { throw "Execution failed with exit code $LASTEXITCODE" }

Write-Host "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Deployment complete." -ForegroundColor Green

