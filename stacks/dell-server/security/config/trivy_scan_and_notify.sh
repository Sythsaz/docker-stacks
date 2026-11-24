#!/bin/bash
# Trivy Security Scanner & Discord Notifier
# This script is designed to run securely via a Docker Socket Proxy.
# It pulls the Webhook URL natively injected by Infisical.

DOCKER_HOST_API="http://monitoring-socket-proxy:2375"
WEBHOOK_URL="${DISCORD_WEBHOOK_URL}"

echo "[$(date -Iseconds)] Starting Trivy scan of running containers..."

# Clean up old reports so patched containers don't leave ghost files behind
rm -f /report/*_trivy-report.html

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
    
    # Wipe the /tmp named volume to ensure old scratch files (e.g. from massive PyTorch layers) don't bloat the disk
    rm -rf /tmp/*
    
    # Point Trivy's Docker client to the socket proxy
    export DOCKER_HOST="tcp://monitoring-socket-proxy:2375"
    
    echo "Scanning $image for vulnerabilities..."
    rm -f /tmp/result.json
    trivy image --quiet --ignore-unfixed --ignorefile /.trivyignore --severity HIGH,CRITICAL --scanners vuln --format json -o /tmp/result.json "$image"
    
    # Check if results exist and parse
    if [ -f /tmp/result.json ]; then
        VULN_COUNT=$(jq '[.Results[]? | .Vulnerabilities[]?] | length' /tmp/result.json)
        
        if [ "$VULN_COUNT" -gt 0 ]; then
            TOTAL_VULNS=$((TOTAL_VULNS + VULN_COUNT))
            
            # Extract summary (top 5 unique vulnerabilities)
            SUMMARY=$(jq -r '[.Results[]? | .Vulnerabilities[]? | "- \(.VulnerabilityID) (\(.Severity)): \(.PkgName)"] | unique | .[0:5] | join("\n")' /tmp/result.json)
            
            REPORT_PAYLOAD="${REPORT_PAYLOAD}\n**${image}** has ${VULN_COUNT} actionable vulnerabilities:\n${SUMMARY}\n"

            # Generate HTML report ONLY for vulnerable images
            # Replace both '/' and ':' with '_' for safe web/windows file names
            SAFE_IMAGE_NAME=$(echo "$image" | tr ':/' '_')
            echo "Generating HTML report for vulnerable image: $image..."
            
            # Note: The @/contrib path is explicitly absolute to ensure the docker image finds it
            trivy image --quiet \
              --ignore-unfixed \
              --ignorefile /.trivyignore \
              --severity HIGH,CRITICAL \
              --scanners vuln \
              --format template \
              --template "@/contrib/html.tpl" \
              -o "/report/${SAFE_IMAGE_NAME}_trivy-report.html" \
              "$image"
              
            echo "HTML report generated."
        else
            echo "Zero actionable vulnerabilities. Skipping HTML generation."
        fi
    fi
    
    # Clear the fanal analysis cache for this image to prevent the tmpfs from filling up over many images.
    # We do NOT use --all because we want to keep the downloaded vulnerability DB.
    trivy clean --scan-cache
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