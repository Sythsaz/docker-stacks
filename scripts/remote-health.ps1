<#
.SYNOPSIS
    Health check script for remote Docker fleet hosts.
.DESCRIPTION
    SSHs to dell-server, homeassistant-pos, and/or Justice to gather docker health, disk usage, and resource stats.
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-11-21
#>
[CmdletBinding()]
param(
    [switch]$VerboseOutput,
    [switch]$Json,
    [ValidateSet('dell-server', 'homeassistant-pos', 'Justice', 'all')]
    [string]$Target = 'dell-server'
)

$ErrorActionPreference = 'Stop'

$targetMap = [ordered]@{
    'dell-server'       = 'hassio@10.0.20.221'
    'homeassistant-pos' = 'hassio@10.0.20.222'
    'Justice'           = 'jusparr@100.79.211.101'
}

$selectedTargets = if ($Target -eq 'all') { @($targetMap.Keys) } else { @($Target) }
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"
$allResults = [ordered]@{}
$anyUnhealthy = $false

function Invoke-HostHealthCheck {
    param([string]$HostName, [string]$SshTarget)

    $sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=5", $SshTarget)
    $result = [ordered]@{
        Target          = $HostName
        SshTarget       = $SshTarget
        Containers      = @()
        DiskUsage       = $null
        DockerDiskUsage = @()
        Stats           = @()
        HasUnhealthy    = $false
        Error           = $null
    }

    try {
        # 1. Container Status & Health (derive Health from Status because {{.Health}} is not a valid docker ps Go template field)
        $psOutput = & ssh @sshArgs "docker ps --format '{{.Names}}\t{{.Status}}'" 2>&1
        if ($LASTEXITCODE -ne 0) {
            throw ("SSH/Docker query failed: {0}" -f ($psOutput -join " "))
        }
        foreach ($line in $psOutput) {
            if ([string]::IsNullOrWhiteSpace($line)) { continue }
            $parts = $line -split "`t", 2
            $name = $parts[0]
            $status = if ($parts.Count -gt 1) { $parts[1] } else { "" }

            $healthStatus = "none"
            if ($status -match "\(unhealthy\)") {
                $healthStatus = "unhealthy"
                $result.HasUnhealthy = $true
            }
            elseif ($status -match "\(healthy\)") {
                $healthStatus = "healthy"
            }
            elseif ($status -match "\(health: starting\)") {
                $healthStatus = "starting"
            }

            $result.Containers += [PSCustomObject]@{
                Name   = $name
                Status = $status
                Health = $healthStatus
            }
        }

        # 2. Root Disk Usage
        $dfOutput = & ssh @sshArgs "df -h / | tail -n 1"
        if ($LASTEXITCODE -eq 0 -and $dfOutput) {
            $dfParts = ($dfOutput | Select-Object -Last 1).Trim() -split "\s+"
            if ($dfParts.Count -ge 6) {
                $result.DiskUsage = [PSCustomObject]@{
                    Filesystem = $dfParts[0]
                    Size       = $dfParts[1]
                    Used       = $dfParts[2]
                    Avail      = $dfParts[3]
                    UsePct     = $dfParts[4]
                    MountedOn  = $dfParts[5]
                }
            }
        }

        if ($VerboseOutput) {
            $result.DockerDiskUsage = & ssh @sshArgs "docker system df"
            $statsOutput = & ssh @sshArgs "docker stats --no-stream --format '{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}'"
            foreach ($line in $statsOutput) {
                if ([string]::IsNullOrWhiteSpace($line)) { continue }
                $parts = $line -split "`t"
                if ($parts.Count -ge 3) {
                    $result.Stats += [PSCustomObject]@{
                        Name   = $parts[0]
                        CPU    = $parts[1]
                        Memory = $parts[2]
                    }
                }
            }
        }
    }
    catch {
        $result.Error = $_.Exception.Message
        $result.HasUnhealthy = $true
    }

    return [PSCustomObject]$result
}

foreach ($t in $selectedTargets) {
    $res = Invoke-HostHealthCheck -HostName $t -SshTarget $targetMap[$t]
    $allResults[$t] = $res
    if ($res.HasUnhealthy) { $anyUnhealthy = $true }
}

if ($Json) {
    if ($Target -eq 'all') {
        $allResults | ConvertTo-Json -Depth 6
    } else {
        $allResults[$Target] | ConvertTo-Json -Depth 6
    }
}
else {
    foreach ($t in $selectedTargets) {
        $r = $allResults[$t]
        Write-Host "`n=== Remote Health Report: $t ($($r.SshTarget)) ===" -ForegroundColor Cyan
        if ($r.Error) {
            Write-Host "[ERROR] $($r.Error)" -ForegroundColor Red
            continue
        }

        Write-Host "`nContainer Health ($($r.Containers.Count) running):" -ForegroundColor Cyan
        $r.Containers | Format-Table -AutoSize

        if ($r.DiskUsage) {
            Write-Host "Root Disk Usage:" -ForegroundColor Cyan
            $r.DiskUsage | Format-Table -AutoSize
        }

        if ($VerboseOutput) {
            Write-Host "Container Resource Usage:" -ForegroundColor Cyan
            $r.Stats | Format-Table -AutoSize
            Write-Host "Docker System Disk Usage:" -ForegroundColor Cyan
            $r.DockerDiskUsage | Out-String | Write-Host
        }

        if ($r.HasUnhealthy) {
            Write-Host "[WARNING] Unhealthy containers detected on $t!" -ForegroundColor Red
        }
        else {
            Write-Host "[OK] All containers on $t healthy or running without healthchecks." -ForegroundColor Green
        }
    }
}

if ($anyUnhealthy) {
    exit 1
}
