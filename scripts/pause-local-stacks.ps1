<#
.SYNOPSIS
    Gaming/streaming mode — pause or resume local Docker stacks.
.DESCRIPTION
    Adjusts local Docker container states using tiered priorities
    matching RULES.md §5.3 to free resources for gaming or streaming.
.NOTES
    Reference: C:\Users\ashto\Docker\RULES.md §5.3
    Machine: DESKTOP-U5E7NRV (i5-3570K / 24GB RAM)
    Date: 2026-09-11
#>
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet('gaming', 'streaming', 'normal')]
    [string]$Mode
)

$ErrorActionPreference = 'Stop'

# ── STACK PRIORITY TIERS ─────────────────────────────────────
$tiers = @{
    Critical = @("infrastructure")
    Monitoring = @("monitoring")
    Streaming = @("streaming")
    Background = @("home-automation", "backups")
}

$baseDir = "C:\Users\ashto\Docker\stacks"
$toPause = @()
$toResume = @()

switch ($Mode) {
    'gaming' {
        Write-Host "═══════════════════════════════════════════" -ForegroundColor Red
        Write-Host "  GAMING MODE — Maximum Performance" -ForegroundColor Red
        Write-Host "  Pausing ALL local Docker stacks" -ForegroundColor Red
        Write-Host "═══════════════════════════════════════════" -ForegroundColor Red
        $toPause = $tiers.Critical + $tiers.Monitoring + $tiers.Streaming + $tiers.Background
    }
    'streaming' {
        Write-Host "═══════════════════════════════════════════" -ForegroundColor Magenta
        Write-Host "  STREAMING MODE — Streaming Priority" -ForegroundColor Magenta
        Write-Host "  Keeping streaming + infra, pausing rest" -ForegroundColor Magenta
        Write-Host "═══════════════════════════════════════════" -ForegroundColor Magenta
        $toPause = $tiers.Monitoring + $tiers.Background
        $toResume = $tiers.Critical + $tiers.Streaming
    }
    'normal' {
        Write-Host "═══════════════════════════════════════════" -ForegroundColor Green
        Write-Host "  NORMAL MODE — All Stacks Active" -ForegroundColor Green
        Write-Host "═══════════════════════════════════════════" -ForegroundColor Green
        $toResume = $tiers.Critical + $tiers.Monitoring + $tiers.Streaming + $tiers.Background
    }
}

foreach ($stack in $toPause) {
    $composeFile = Join-Path $baseDir "$stack\compose.yaml"
    if (Test-Path $composeFile) {
        if ($PSCmdlet.ShouldProcess($stack, "Pause")) {
            Write-Host "  ⏸  Pausing: $stack" -ForegroundColor Yellow
            docker compose -f $composeFile pause 2>&1
        }
    }
}

foreach ($stack in $toResume) {
    $composeFile = Join-Path $baseDir "$stack\compose.yaml"
    if (Test-Path $composeFile) {
        if ($PSCmdlet.ShouldProcess($stack, "Resume")) {
            Write-Host "  ▶  Resuming: $stack" -ForegroundColor Green
            docker compose -f $composeFile unpause 2>&1
        }
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
            $processArgs = "-ExecutionPolicy Bypass -Command "& '$vaultOp' -Action 'System Mode Changed' -Details 'Local stack mode adjusted to: $Mode'""
            Start-Process -FilePath "powershell.exe" -ArgumentList $processArgs -NoNewWindow -Wait
        }
        catch { Write-Host "Warning: VaultOp logging failed. $($_.Exception.Message)" -ForegroundColor Yellow }
    }
}

Write-Host "
Mode [$Mode] applied." -ForegroundColor Cyan