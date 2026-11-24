#!/usr/bin/env bash
set -euo pipefail
# update package lists
/usr/bin/apt-get update -qq 2>&1 >/dev/null
# perform upgrade non-interactively
/usr/bin/apt-get upgrade -y -qq
# optional: clean up
/usr/bin/apt-get autoremove -y -qq
/usr/bin/apt-get autoclean -qq
echo "UPGRADE_COMPLETE"