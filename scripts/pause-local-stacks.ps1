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
    Critical   = @("infrastructure")
    Monitoring = @("monitoring")
    Streaming  = @("streaming")
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

$logFile = "D:\_Consolidation_Manifests\Logs\Docker_Stack_Mode.log"
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
function Write-ModeLog {
    param([string]$Message)
    try {
        $parent = Split-Path $logFile -Parent
        if ($parent -and -not (Test-Path -LiteralPath $parent)) {
            New-Item -Path $parent -ItemType Directory -Force | Out-Null
        }
        [System.IO.File]::AppendAllText($logFile, "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] $Message`r`n", $utf8NoBom)
    } catch {}
}

& docker info 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "[SKIP] Local Docker daemon is not running; mode [$Mode] no-op." -ForegroundColor Yellow
    Write-ModeLog "[SKIP] Local Docker daemon offline; mode [$Mode] no-op."
    return
}

foreach ($stack in $toPause) {
    $composeFile = Join-Path $baseDir "$stack\compose.yaml"
    if (Test-Path $composeFile) {
        $running = @(& docker compose -f $composeFile ps --status running -q 2>$null | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
        if ($running.Count -gt 0 -and $PSCmdlet.ShouldProcess($stack, "Pause")) {
            Write-Host "  ⏸  Pausing: $stack" -ForegroundColor Yellow
            & docker compose -f $composeFile pause 2>&1
            if ($LASTEXITCODE -ne 0) { throw "Failed pausing stack $stack (exit $LASTEXITCODE)" }
        }
    }
}

foreach ($stack in $toResume) {
    $composeFile = Join-Path $baseDir "$stack\compose.yaml"
    if (Test-Path $composeFile) {
        $paused = @(& docker compose -f $composeFile ps --status paused -q 2>$null | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
        if ($paused.Count -gt 0 -and $PSCmdlet.ShouldProcess($stack, "Resume")) {
            Write-Host "  ▶  Resuming: $stack" -ForegroundColor Green
            & docker compose -f $composeFile unpause 2>&1
            if ($LASTEXITCODE -ne 0) { throw "Failed unpausing stack $stack (exit $LASTEXITCODE)" }
        }
    }
}

Write-ModeLog "[MODE_CHANGE] Local Docker stack mode adjusted to: $Mode"

Write-Host "
Mode [$Mode] applied." -ForegroundColor Cyan
