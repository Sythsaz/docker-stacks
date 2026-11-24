#!/usr/bin/env bash
set -euo pipefail
# update package lists
/usr/bin/apt-get update -qq 2>&1 >/dev/null
# list upgradable packages (simulate upgrade and extract package names/versions)
UP=$(/usr/bin/apt-get -s dist-upgrade | awk '/^Inst/ { sub(/^Inst /, ""); print }')
if [ -z "$UP" ]; then
  echo "NO_UPDATES"
else
  echo "UPDATES_AVAILABLE"
  echo "$UP"
fi