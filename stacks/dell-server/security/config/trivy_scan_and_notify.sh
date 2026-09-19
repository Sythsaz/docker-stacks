#!/bin/bash
# Trivy Security Scanner & Discord Notifier
# This script is designed to run securely via a Docker Socket Proxy.
# It pulls the Webhook URL natively injected by Infisical.

DOCKER_HOST_API="http://monitoring-socket-proxy:2375"
WEBHOOK_URL="${DISCORD_WEBHOOK_URL}"

echo "[$(date -Iseconds)] Starting Trivy scan of running containers..."

# Query the Docker Socket Proxy for running containers
IMAGES=$(curl -s "${DOCKER_HOST_API}/containers/json" | jq -r '.[].Image' | sort -u)

if [ -z "$IMAGES" ]; then
    echo "No running containers found."
    exit 0
fi

TOTAL_VULNS=0
REPORT_PAYLOAD=""

for image in $IMAGES; do
    echo "Scanning $image..."
    
    # Point Trivy's Docker client to the socket proxy
    export DOCKER_HOST="tcp://monitoring-socket-proxy:2375"
    
    # Run scan, outputting JSON to a tmpfs location
    # --ignore-unfixed: removes unactionable noise (maintainer hasn't patched yet)
    # --severity HIGH,CRITICAL: focus only on high impact vulnerabilities
    # --scanners vuln: only scan for vulnerabilities to save time
    trivy image --quiet --ignore-unfixed --severity HIGH,CRITICAL --scanners vuln --format json -o /tmp/result.json "$image"
    
    # Check if results exist and parse
    if [ -f /tmp/result.json ]; then
        VULN_COUNT=$(jq '[.Results[]? | .Vulnerabilities[]?] | length' /tmp/result.json)
        
        if [ "$VULN_COUNT" -gt 0 ]; then
            TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
            
            # Extract summary (top 5 unique vulnerabilities)
            SUMMARY=$(jq -r '[.Results[]? | .Vulnerabilities[]? | "- \(.VulnerabilityID) (\(.Severity)): \(.PkgName)"] | unique | .[0:5] | join("\n")' /tmp/result.json)
            
            REPORT_PAYLOAD="${REPORT_PAYLOAD}\n**${image}** has ${VULN_COUNT} actionable vulnerabilities:\n${SUMMARY}\n"
        fi
    fi
done

if [ "$TOTAL_VULNS" -gt 0 ]; then
    echo "Found $TOTAL_VULNS actionable vulnerabilities. Compiling report..."
    
    # Construct Discord Webhook JSON payload safely
    JSON_PAYLOAD=$(jq -n --arg content "🚨 **Trivy Security Scan Alert** 🚨\nFound **${TOTAL_VULNS}** high/critical vulnerabilities with available fixes in running containers.\n${REPORT_PAYLOAD}" '{content: $content}')
    
    if [ -n "$WEBHOOK_URL" ] && [ "$WEBHOOK_URL" != "null" ]; then
        echo "Sending notification via Infisical-injected webhook..."
        curl -s -H "Content-Type: application/json" -d "$JSON_PAYLOAD" "$WEBHOOK_URL"
        echo "Webhook sent."
    else
        echo "Warning: DISCORD_WEBHOOK_URL is not set or empty. Cannot send Discord notification."
    fi
else
    echo "No actionable vulnerabilities found. Your infrastructure is secure."
fi
