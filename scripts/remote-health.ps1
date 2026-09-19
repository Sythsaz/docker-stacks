<#
.SYNOPSIS
    Health check script for Dell server containers.
.DESCRIPTION
    SSHs to the Dell server to gather docker health, disk usage, and resource stats.
.AUTHOR
    Docker Infrastructure Specialist
.DATE
    2026-09-11
#>
[CmdletBinding()]
param(
    [switch]$VerboseOutput,
    [switch]$Json
)

$ErrorActionPreference = 'Stop'

$sshTarget = "hassio@10.0.20.221"
$sshKey = "$env:USERPROFILE\.ssh\id_ed25519"
$sshArgs = @("-i", $sshKey, "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", "ConnectTimeout=5", $sshTarget)

$result = @{
    Containers = @()
    DiskUsage = @()
    DockerDiskUsage = @()
    Stats = @()
    HasUnhealthy = $false
}

try {
    # 1. Container Status & Health
    $psOutput = ssh @sshArgs "docker ps --format '{{.Names}}`t{{.Status}}`t{{.Health}}'"
    foreach ($line in $psOutput) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $parts = $line -split "`t"
        $name = $parts[0]
        $status = $parts[1]
        $health = if ($parts.Count -gt 2 -and -not [string]::IsNullOrWhiteSpace($parts[2])) { $parts[2] } else { "none" }
        
        $healthStatus = "unknown"
        if ($health -match "healthy") { $healthStatus = "healthy" }
        elseif ($health -match "unhealthy") { $healthStatus = "unhealthy"; $result.HasUnhealthy = $true }
        elseif ($health -eq "none") { $healthStatus = "none" }
        
        $result.Containers += [PSCustomObject]@{
            Name = $name
            Status = $status
            Health = $healthStatus
        }
    }

    # 2. Disk Usage
    $dfOutput = ssh @sshArgs "df -h / | tail -n 1"
    $dfParts = $dfOutput -split "\s+"
    $result.DiskUsage = [PSCustomObject]@{
        Filesystem = $dfParts[0]
        Size = $dfParts[1]
        Used = $dfParts[2]
        Avail = $dfParts[3]
        UsePct = $dfParts[4]
        MountedOn = $dfParts[5]
    }

    # Docker System DF
    $result.DockerDiskUsage = ssh @sshArgs "docker system df"

    # 3. Stats
    $statsOutput = ssh @sshArgs "docker stats --no-stream --format '{{.Name}}`t{{.CPUPerc}}`t{{.MemUsage}}'"
    foreach ($line in $statsOutput) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $parts = $line -split "`t"
        $result.Stats += [PSCustomObject]@{
            Name = $parts[0]
            CPU = $parts[1]
            Memory = $parts[2]
        }
    }

    if ($Json) {
        $result | ConvertTo-Json -Depth 5
    } else {
        Write-Host "=== Remote Health Report ===" -ForegroundColor Cyan
        
        Write-Host "
Container Health:" -ForegroundColor Cyan
        $result.Containers | Format-Table -AutoSize

        Write-Host "
Root Disk Usage:" -ForegroundColor Cyan
        $result.DiskUsage | Format-Table -AutoSize

        if ($VerboseOutput) {
            Write-Host "
Container Resource Usage:" -ForegroundColor Cyan
            $result.Stats | Format-Table -AutoSize
            
            Write-Host "
Docker System Disk Usage:" -ForegroundColor Cyan
            $result.DockerDiskUsage | Out-String | Write-Host
        }

        if ($result.HasUnhealthy) {
            Write-Host "
[WARNING] Unhealthy containers detected!" -ForegroundColor Red
        } else {
            Write-Host "
[OK] All containers healthy or running without healthchecks." -ForegroundColor Green
        }
    }

    # Dispatch audit log via VaultOp.ps1 using centralized variable
    $vaultOp = "C:\Users\ashto\Docker\scripts\VaultOp.ps1"
    if (Test-Path $vaultOp) {
        $vaultOpAcl = Get-Acl $vaultOp
        $isSafe = $true
        $currentUserSid = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
        $allowedSids = @('S-1-5-18', 'S-1-5-32-544', $currentUserSid)
        
        foreach ($rule in $vaultOpAcl.Access) {
            if ($rule.FileSystemRights -match "Write|Modify|FullControl") {
                try {
                    $ruleSid = $rule.IdentityReference.Translate([System.Security.Principal.SecurityIdentifier]).Value
                    if ($ruleSid -notin $allowedSids) { $isSafe = $false; break }
                }
                catch { $isSafe = $false; break }
            }
        }
        
        if (-not $isSafe) {
            Write-Host "CRITICAL SECURITY WARNING: VaultOp.ps1 is writable by unauthorized users! Execution blocked." -ForegroundColor Red
        }
        else {
            try {
                $healthLog = if ($result.HasUnhealthy) { "Remote health check completed with warnings." } else { "Remote health check passed." }
                $processArgs = "-ExecutionPolicy Bypass -Command `"& '$vaultOp' -Action 'Health Check' -Details '$healthLog'`""
                Start-Process -FilePath "powershell.exe" -ArgumentList $processArgs -NoNewWindow -Wait
            }
            catch { Write-Host "Warning: VaultOp logging failed. $($_.Exception.Message)" -ForegroundColor Yellow }
        }
    }

    if ($result.HasUnhealthy) {
        exit 1
    }

} catch {
    Write-Error "Failed to check remote health: $_"
    exit 1
}