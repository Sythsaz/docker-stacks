#!/bin/bash
HA_BACKUP_DIR="/home/hassio/home_assistant/ha_config/backups"
ARCHIVE_DIR="/mnt/externals/SB/HA_Backups"

mkdir -p "$ARCHIVE_DIR/weekly" "$ARCHIVE_DIR/monthly"

LATEST_BACKUP=$(ls -t "$HA_BACKUP_DIR"/*.tar 2>/dev/null | head -n 1)

if [ -z "$LATEST_BACKUP" ]; then
    echo "No Home Assistant backups found."
    exit 1
fi

if [ "$1" == "weekly" ]; then
    cp "$LATEST_BACKUP" "$ARCHIVE_DIR/weekly/$(date +%F)_weekly.tar"
    # Prune keeping exactly 8 weekly backups (2 months)
    ls -t "$ARCHIVE_DIR/weekly"/*_weekly.tar 2>/dev/null | tail -n +9 | xargs -r rm -f --
fi

if [ "$1" == "monthly" ]; then
    cp "$LATEST_BACKUP" "$ARCHIVE_DIR/monthly/$(date +%F)_monthly.tar"
    # Prune keeping exactly 9 monthly backups (rest of the year)
    ls -t "$ARCHIVE_DIR/monthly"/*_monthly.tar 2>/dev/null | tail -n +10 | xargs -r rm -f --
fi

# Mirror the local archive directory to Google Drive
rclone sync "$ARCHIVE_DIR" gdrive:HA_Archives --fast-list --config /home/hassio/.config/rclone/rclone.conf
