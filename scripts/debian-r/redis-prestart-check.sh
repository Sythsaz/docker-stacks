#!/usr/bin/env bash
# ==============================================================================
# Redis Pre-Start Health Check & Auto-Healing Script
# Validates RDB database integrity before redis-server starts.
# Quarantines corrupt databases, manages retention, and triggers recovery alerts.
# ==============================================================================
set -uo pipefail

RDB_FILE="/var/lib/redis/dump.rdb"
FLAG_FILE="/run/redis_quarantined"
HA_WEBHOOK_URL="http://10.0.20.23:8123/api/webhook/fleet_alert"

if [ ! -f "$RDB_FILE" ]; then
    exit 0
fi

if ! redis-check-rdb "$RDB_FILE" >/dev/null 2>&1; then
    TIMESTAMP=$(date +%s)
    QUARANTINE_FILE="/var/lib/redis/dump.rdb.corrupt.${TIMESTAMP}"
    echo "[!] Redis RDB corruption detected at $RDB_FILE! Quarantining to $QUARANTINE_FILE..." >&2
    logger -t redis-prestart-check -p user.err "Redis RDB corruption detected at $RDB_FILE. Quarantining to $QUARANTINE_FILE."
    
    mv "$RDB_FILE" "$QUARANTINE_FILE"
    chown redis:redis "$QUARANTINE_FILE" 2>/dev/null || true
    rm -f /var/lib/redis/temp-*.rdb 2>/dev/null || true

    # Keep at most latest 3 corrupt dump archives to prevent storage exhaustion
    ls -t /var/lib/redis/dump.rdb.corrupt.* 2>/dev/null | tail -n +4 | xargs -r rm -f 2>/dev/null || true

    # Flag for post-start confirmation
    touch "$FLAG_FILE" 2>/dev/null || true

    # Dispatch Fleet Alert to Home Assistant (fail-open if HA is unreachable)
    PAYLOAD="{\"severity\":\"CRITICAL\",\"hostname\":\"debian-r\",\"metric\":\"redis_rdb_corrupt\",\"message\":\"Corrupted dump.rdb quarantined to $(basename "$QUARANTINE_FILE"). Redis database auto-reset and starting cleanly.\"}"
    curl -s --connect-timeout 4 --max-time 8 -X POST -H "Content-Type: application/json" -d "$PAYLOAD" "$HA_WEBHOOK_URL" 2>/dev/null || true
    echo "[+] Quarantine complete. Redis will start with an empty database." >&2
fi

exit 0
