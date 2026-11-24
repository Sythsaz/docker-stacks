param (
    [Parameter(Mandatory = $true)]
    [string]$ProjectId,

    [switch]$ForceRecreate,
    [switch]$MonitorLogs
)

$deploymentPlan = @(
    @{ Stack = "security"; Domain = "dell-server"; Delay = 2; Desc = "Tier 1: Root of Trust (Infisical, DB, Redis)" },
    @{ Stack = "infrastructure"; Domain = "dell-server"; Delay = 2; Desc = "Tier 2: Core Networking & Reverse Proxy" },
    @{ Stack = "auth"; Domain = "dell-server"; Delay = 2; Desc = "Tier 3: Identity Provider & DB Migrations" },
    @{ Stack = "vaultwarden"; Domain = "dell-server"; Delay = 2; Desc = "Tier 4: Vaultwarden" },
    @{ Stack = "home-assistant"; Domain = "homeassistant-pos"; Delay = 2; Desc = "Tier 4: Home Assistant" },
    @{ Stack = "media"; Domain = "dell-server"; Delay = 2; Desc = "Tier 4: Media Stack" },
    @{ Stack = "mcp"; Domain = "dell-server"; Delay = 2; Desc = "Tier 4: MCP Services" },
    @{ Stack = "web"; Domain = "dell-server"; Delay = 2; Desc = "Tier 4: WordPress & Web" },
    @{ Stack = "observability"; Domain = "dell-server"; Delay = 2; Desc = "Tier 5: Monitoring & Logging" }
)

foreach ($task in $deploymentPlan) {
    $stackName = $task.Stack
    $domain = $task.Domain
    Write-Host "`n[STARTING] Deploying $domain/$stackName ($($task.Desc))..." -ForegroundColor Cyan
    
    if ($stackName -eq "security") {
        .\scripts\deploy-remote.ps1 -Stack "$domain/$stackName" -Action "up -d" -MonitorLogs:$MonitorLogs -ForceRecreate:$ForceRecreate
    }
    else {
        .\scripts\deploy-remote.ps1 -Stack "$domain/$stackName" -ProjectId $ProjectId -Action "up -d" -MonitorLogs:$MonitorLogs -ForceRecreate:$ForceRecreate
    }

    Write-Host "Waiting $($task.Delay)s for initialization..." -ForegroundColor Yellow
    Start-Sleep -Seconds $task.Delay
}

Write-Host "`n[COMPLETE] All remote stacks have been successfully deployed!" -ForegroundColor Green
