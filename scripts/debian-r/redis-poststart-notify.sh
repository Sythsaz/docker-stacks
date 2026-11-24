#!/usr/bin/env bash
# ==============================================================================
# Redis Post-Start Health Confirmation & Auto-Resolution Script
# Triggered via ExecStartPost in systemd. If a pre-start quarantine occurred,
# verifies Redis is actively serving ping and dispatches a RESOLVED webhook.
# ==============================================================================
set -uo pipefail

FLAG_FILE="/run/redis_quarantined"
HA_WEBHOOK_URL="http://10.0.20.23:8123/api/webhook/fleet_alert"

if [ ! -f "$FLAG_FILE" ]; then
    exit 0
fi

# Poll redis-cli ping for up to 10 seconds
RESOLVED=0
for i in $(seq 1 10); do
    PING_RESP=$(redis-cli -h 127.0.0.1 ping 2>/dev/null || true)
    if [ "$PING_RESP" = "PONG" ]; then
        RESOLVED=1
        break
    fi
    sleep 1
done

if [ "$RESOLVED" -eq 1 ]; then
    PAYLOAD="{\"severity\":\"RESOLVED\",\"hostname\":\"debian-r\",\"metric\":\"redis_rdb_corrupt\",\"message\":\"Redis server successfully restarted, verified responsive (PONG), and operational following RDB quarantine.\"}"
    curl -s --connect-timeout 4 --max-time 8 -X POST -H "Content-Type: application/json" -d "$PAYLOAD" "$HA_WEBHOOK_URL" 2>/dev/null || true
    logger -t redis-poststart-notify -p user.info "Redis recovery verified and RESOLVED alert dispatched to Home Assistant."
    rm -f "$FLAG_FILE" 2>/dev/null || true
fi

exit 0
