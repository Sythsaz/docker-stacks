<#
.SYNOPSIS
    Deploys all Docker compose stacks to Justice's host (homeassistant-j / 100.79.211.101) using Infisical Zero-Trust.
.DESCRIPTION
    Executes tiered deployment in strict dependency order:
      Tier 1: Infrastructure (socket-proxy, portainer_agent)
      Tier 2: Home Assistant (HA, Mosquitto, Node-RED, ESPHome, TasmoAdmin, Piper, Whisper)
      Tier 3: MCP (ha-mcp, docker-mcp-gateway)
      Tier 4: Media (AirCast, MediaMTX)
      Tier 5: Observability (Scrutiny, WUD, Autoheal)
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-11-07
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param (
    [Parameter(Mandatory = $false)]
    [string]$ProjectId = "ed163e38-c457-4f41-a802-43febf927983",

    [switch]$ForceRecreate,
    [switch]$MonitorLogs,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$deploymentPlan = @(
    @{ Stack = "infrastructure"; Domain = "Justice"; Delay = 3; Desc = "Tier 1: Socket Proxy & Portainer Agent" },
    @{ Stack = "home-assistant"; Domain = "Justice"; Delay = 5; Desc = "Tier 2: Core Home Assistant & Mosquitto Suite" },
    @{ Stack = "mcp";            Domain = "Justice"; Delay = 3; Desc = "Tier 3: Model Context Protocol (HA-MCP & Gateway)" },
    @{ Stack = "media";          Domain = "Justice"; Delay = 2; Desc = "Tier 4: Media Stack (AirCast & MediaMTX)" },
    @{ Stack = "observability";  Domain = "Justice"; Delay = 2; Desc = "Tier 5: Observability & Autoheal (WUD, Scrutiny, Autoheal)" }
)

Write-Host "═══════════════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host " STARTING JUSTICE ZERO-TRUST DEPLOYMENT PIPELINE (Infisical: $ProjectId)" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════════════════" -ForegroundColor Cyan

foreach ($task in $deploymentPlan) {
    $stackName = $task.Stack
    $domain = $task.Domain
    Write-Host "`n[STARTING] Deploying $domain/$stackName ($($task.Desc))..." -ForegroundColor Cyan
    
    $deployArgs = @{
        Stack         = "$domain/$stackName"
        ProjectId     = $ProjectId
        Action        = "up -d"
        ForceRecreate = $ForceRecreate
        DryRun        = $DryRun
    }
    if ($MonitorLogs) {
        $deployArgs["MonitorLogs"] = $true
    }

    & (Join-Path $PSScriptRoot "deploy-remote.ps1") @deployArgs

    if (-not $DryRun) {
        Write-Host "Waiting $($task.Delay)s for health stabilization..." -ForegroundColor Yellow
        Start-Sleep -Seconds $task.Delay
    }
}

Write-Host "`n═══════════════════════════════════════════════════════════════════════" -ForegroundColor Green
Write-Host " [COMPLETE] All Justice remote stacks deployed successfully!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════════════" -ForegroundColor Green
