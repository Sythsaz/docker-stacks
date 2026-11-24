<#
.SYNOPSIS
    Monitors logs for remote Docker compose stacks.
.DESCRIPTION
    Tails and follows real-time logs for a specific remote stack over SSH.
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-09-24
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[a-zA-Z0-9_-]+[/\\][a-zA-Z0-9_-]+$')]
    [string]$Stack,

    [Parameter(Mandatory = $false)]
    [string]$Service,

    [int]$Tail = 100,

    [switch]$NoFollow,

    [switch]$NewWindow
)

$ErrorActionPreference = 'Stop'

$stackParts = $Stack -split "[/\\]"
$domainPart = $stackParts[0]
$serviceName = $stackParts[1]

if ($domainPart -eq "Justice") {
    $remoteUser = "jusparr"
    $remoteHost = "100.79.211.101"
    $remoteBaseDir = "/home/jusparr/docker/stacks"
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
    $remoteUser = "hassio"
    $remoteHost = "10.0.20.221"
    $remoteBaseDir = "/home/hassio/docker"
}
$sshTarget = "${remoteUser}@${remoteHost}"
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"

$remoteStack = $Stack -replace '\\', '/'
$remoteStackDir = "$remoteBaseDir/$remoteStack"

$followArg = if ($NoFollow) { "" } else { "-f" }
$tailArg = if ($Tail -gt 0) { "--tail $Tail" } else { "" }
$serviceArg = if ([string]::IsNullOrWhiteSpace($Service)) { "" } else { $Service }

$sshCmd = "cd $remoteStackDir && docker compose logs $followArg $tailArg $serviceArg"

if ($NewWindow) {
    Write-Host "[SPAWNING] Launching log stream for $Stack in a new window..." -ForegroundColor Cyan
    $innerScript = "ssh -i '$sshKey' -o 'BatchMode=yes' -o 'StrictHostKeyChecking=yes' -t '$sshTarget' `"$sshCmd`"; Write-Host '`n[Disconnected]'; Read-Host 'Press Enter to close'"
    $encodedCmd = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($innerScript))
    Start-Process powershell -ArgumentList "-NoProfile", "-EncodedCommand", $encodedCmd
}
else {
    Write-Host "[STARTING] Streaming logs for $Stack ($remoteHost)..." -ForegroundColor Cyan
    Write-Host "Press Ctrl+C to stop following.`n" -ForegroundColor Yellow
    ssh -i $sshKey -o "BatchMode=yes" -o "StrictHostKeyChecking=yes" -t $sshTarget "$sshCmd"
}
