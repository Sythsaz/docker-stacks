# 🐋 DOCKER MANAGEMENT RULES

> **Scope**: Governs ALL Docker operations across the entire ecosystem — local Docker Desktop
> on `DESKTOP-U5E7NRV`, remote Docker Engine on `debian-dell` (10.0.1.221), and cross-machine
> MCP relay to Stream PC (`DESKTOP-3PNV5BO`) and Laptop (`LAPTOP`).
>
> **Authority**: This file is the single source of truth for Docker governance. Every agent
> (`@homelab`, `@ide`, `@stream`, `@vault`, `@web`, `@life`) MUST comply.
>
> **Portainer Integration**: Portainer's stack editor is the **primary UI** for managing
> Dell server stacks. Git serves as the **sync, backup, and audit trail**. Changes made in
> Portainer MUST be pulled back to this repo. Changes made in Git MUST be deployed via
> `scripts/deploy-remote.ps1` or synced to Portainer.

---

## §1 — DIRECTORY STRUCTURE & NAMING

### 1.1 Folder-Per-Stack Layout
```
stacks/
├── <domain>/
│   └── <service>/
│       ├── compose.yaml        # Compose Specification (no version: directive)
│       ├── (Legacy) secrets/   # Deprecated, all secrets injected via Infisical
│       │   └── *.enc           # Safe to commit — encrypted at rest
│       └── data/               # Bind mount target — NEVER committed
```

### 1.2 Stack Domains
| Domain | Purpose | Location |
|--------|---------|----------|
| `infrastructure/` | Reverse proxy, socket-proxy, Cloudflare Tunnel | Local + Remote |
| `monitoring/` | Dozzle, WUD, Autoheal, cAdvisor, Prometheus | Local + Remote |
| `home-automation/` | Home Assistant, MQTT, Zigbee2MQTT, ESPHome, Node-RED | Remote (Dell) |
| `streaming/` | Streamer.bot relays, OBS WebSocket bridges | Local |
| `backups/` | Offen/Restic backup orchestration | Local + Remote |
| `dell-server/` | Mirrors all remote Dell server stacks | Remote (Dell) |

### 1.3 Naming Conventions
- **Compose files**: `compose.yaml` — never `docker-compose.yml` or `docker-compose.yaml`
- **No `version:` directive** — Compose Specification (2024+) parses automatically
- **Extension fields**: Use `x-` prefixed YAML anchors for DRY configuration
- **Container naming**: `<domain>-<service>-<instance>` (e.g., `web-wordpress-1`)

### 1.4 Storage Policy
- **Primary storage**: `C:\Users\ashto\Docker\` (SSD) — all compose files, scripts, templates
- **Backup storage**: `D:\Docker\Backups\` (8TB HDD) — volume backups only
- **Symlinks**: `D:\Docker\MCP` → `C:\Users\ashto\Docker\stacks\` for MCP config compatibility
- **NEVER** store active databases or high-IOPS volumes on `D:\` (ASMedia controller instability)

---

## §2 — SECURITY HARDENING (MANDATORY)

Every container — local and remote — MUST apply these hardening measures.
No exceptions without a documented justification comment in the compose file.

### 2.1 Mandatory Service Security Template
```yaml
services:
  any-service:
    # ── IDENTITY ──────────────────────────────────────────────
    user: "1000:1000"                    # Non-root. Match host UID:GID.

    # ── PRIVILEGE ESCALATION PREVENTION ───────────────────────
    security_opt:
      - no-new-privileges:true           # Blocks setuid/setgid binaries
      - seccomp=unconfined               # REMOVE this line; use default seccomp
    # Docker's default seccomp profile blocks 44+ dangerous syscalls.
    # Only override with a CUSTOM profile if the app explicitly requires it.

    # ── CAPABILITY REDUCTION ──────────────────────────────────
    cap_drop:
      - ALL                              # Drop ALL 38 Linux capabilities
    cap_add: []
    # cap_add:
    #   - NET_BIND_SERVICE               # ONLY if binding ports < 1024 inside container
    #   - CHOWN                          # ONLY if container must chown files at startup
    # EVERY cap_add MUST have an inline comment justifying WHY.

    # ── FILESYSTEM HARDENING ──────────────────────────────────
    read_only: true                      # Root filesystem is immutable
    tmpfs:
      - /tmp:rw,noexec,nosuid,size=64m   # Writable temp with noexec
      - /run:rw,noexec,nosuid,size=16m   # Runtime dir

    # ── RESOURCE ISOLATION ────────────────────────────────────
    pids_limit: 100                      # Prevents fork bombs
    # Adjust upward ONLY for multi-process apps (e.g., PHP-FPM) with justification

    # ── RESTART POLICY ────────────────────────────────────────
    restart: unless-stopped
```

### 2.2 Docker Socket Protection
- **NEVER** mount `/var/run/docker.sock` directly into any container
- **ALL** socket consumers (Portainer, Dozzle, WUD, Traefik) MUST use a socket proxy:
  ```yaml
  socket-proxy:
    image: wollomatic/socket-proxy:1
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    read_only: true
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      # Principle of least privilege: allowlist ONLY required endpoints
      ALLOW_START: "0"
      ALLOW_STOP: "0"
      ALLOW_RESTARTS: "0"
      LOG_LEVEL: "warn"
    networks:
      - socket-proxy
    # This container is the ONLY one that touches the Docker socket.
  ```

### 2.3 Port Binding Rules
```yaml
ports:
  # DEFAULT: Bind to localhost ONLY — accessible via reverse proxy or SSH tunnel
  - "127.0.0.1:8080:80"

  # LAN-FACING: Requires inline justification comment
  # JUSTIFICATION: Home Assistant requires LAN discovery for SSDP/HomeKit
  - "8123:8123"

  # PROHIBITED: Never bind 0.0.0.0 without firewall rule
  # - "8080:80"  # ❌ NEVER — exposes to all interfaces including WAN
```

### 2.4 Network Isolation
- Every stack gets its own user-defined bridge network
- Cross-stack communication via explicit external networks ONLY
- `network_mode: host` requires a justification block:
  ```yaml
  # ══════════════════════════════════════════════════════════
  # HOST NETWORK JUSTIFICATION:
  # Service: Home Assistant
  # Reason: Requires raw L2 access for mDNS discovery, SSDP,
  #         HomeKit, and Thread border router communication.
  # Mitigations: Container runs on dedicated IoT VLAN interface.
  #              OPNsense firewall restricts ingress to IoT subnet only.
  # Reviewed: 2026-09-07
  # ══════════════════════════════════════════════════════════
  network_mode: host
  ```

### 2.5 Image Supply Chain Security
- **Docker Content Trust (DCT)**: Enable signature verification for all image pulls:
  ```powershell
  # Set in environment or daemon config
  $env:DOCKER_CONTENT_TRUST = 1
  ```
- **Container Scanning**: Run `docker scout cves <image>` before deploying any new image
- **SBOM Generation**: Maintain Software Bill of Materials for production images:
  ```bash
  docker scout sbom <image> --format spdx-json > sbom.json
  ```

### 2.6 Runtime Security Monitoring
- Deploy container-level intrusion detection via `falcosecurity/falco` on the Dell server
- Monitor for: unauthorized process execution, unexpected network connections,
  file integrity violations, privilege escalation attempts
- Falco alerts route to Discord webhook (same channel as WUD notifications)

---

## §3 — SECRETS & CREDENTIALS (Infisical Zero-Trust)

### 3.1 Encryption Standard
- **Backend**: Self-hosted Infisical (`secrets.sythsaz.ca`)
- **Key storage**: Infisical manages secrets natively. No GPG or Age keys are stored on the local workstation.
- **Exception (Root of Trust)**: The `dell-server/security` stack (which hosts Infisical) is the ONLY stack that uses SOPS (`.enc`) files for its initial database bootstrap.

### 3.2 Secret Lifecycle
```text
Create (Web UI) → Commit (Code) → Deploy (infisical run) → Inject (Runtime Memory)
```

1. **Create**: Add the secret to the appropriate project/environment in the Infisical Web UI.
2. **Commit**: Reference the secret via standard `$${SECRET_NAME}` interpolation in `compose.yaml`.
3. **Deploy**: `scripts/deploy-remote.ps1` executes `infisical run -- docker compose up -d` on the remote server.
4. **Inject**: The Infisical CLI natively injects the secrets as environment variables directly into the container's memory upon startup.
5. **Scan**: The `infisical scan` pre-commit hook ensures no plaintext secrets are ever pushed.

### 3.3 Compose Secrets Pattern
```yaml
services:
  app:
    environment:
      # Inject directly using standard Docker variable interpolation
      DB_PASSWORD: $${DB_PASSWORD}
      STRIPE_SECRET_KEY: $${STRIPE_SECRET_KEY}
```

### 3.4 Secret Classification
| Tier | Examples | Policy |
|------|----------|--------|
| **Tier 0 — Critical** | Stripe keys, DB root passwords, SSH keys | Infisical-managed, never in logs, rotate quarterly |
| **Tier 1 — Sensitive** | API tokens, MQTT passwords, webhook secrets | Infisical-managed, rotate annually |
| **Tier 2 — Internal** | Service ports, timezone, feature flags | May be hardcoded or managed in Infisical |

### 3.5 Anti-Patterns (STRICTLY PROHIBITED)
- ❌ Hardcoding plaintext passwords directly into `compose.yaml`.
- ❌ Secrets passed via Dockerfile `ARG` (baked into layer history permanently).
- ❌ Committing `.env` files to git.
- ❌ Using legacy `secrets:` blocks or `_FILE` suffixes (except for the Root of Trust stack).
- ❌ Logging secret values in any output, audit log, or vault note.

---

## §4 — IMAGE MANAGEMENT

### 4.1 Version Pinning Policy
| Service Type | Pinning Requirement | Example |
|-------------|---------------------|---------|
| **Databases** | Pin to minor + patch | `postgres:16.4-alpine` |
| **Payment/Auth** | Pin to SHA256 digest | `image: repo/app@sha256:abc123...` |
| **Core Infrastructure** | Pin to minor | `traefik:3.2` |
| **Monitoring/Tools** | Pin to minor | `dozzle/dozzle:8.8` |
| **Dev/Scratch** | Minor acceptable | `node:20-slim` |

- **NEVER** use `:latest` for any stateful or infrastructure service
- **ALWAYS** include a comment above `image:` documenting update cadence:
  ```yaml
  # Source: https://hub.docker.com/_/postgres
  # Update cadence: Security patches within 48h, minor versions monthly
  # Last reviewed: 2026-09-07
  image: postgres:16.4-alpine
  ```

### 4.2 Update Strategy — What's Up Docker (WUD)
WUD monitors all registries and applies tiered update automation:

| Tier | Trigger | Action | Services |
|------|---------|--------|----------|
| **Tier 0** | Any version change | **Alert only** (Discord) — manual review, staged rollback plan | Home Assistant, MariaDB, Redis, Stripe, Frigate, EMQX |
| **Tier 1** | Patch version change | **Auto-update** | Dozzle, cAdvisor, Traefik, Grafana, WUD itself |
| **Tier 1** | Minor/major change | **Alert only** | Same as above |
| **Tier 2** | Any version change | **Auto-update** | Speedtest trackers, dev tools, scratch containers |

WUD configuration via labels:
```yaml
labels:
  # Tier 0: Alert only
  - "wud.tag.include=^\\d+\\.\\d+\\.\\d+$$"
  - "wud.watch=true"
  - "wud.trigger.type=discord"

  # Tier 1: Auto-update patches
  - "wud.tag.include=^\\d+\\.\\d+\\.\\d+$$"
  - "wud.watch=true"
  - "wud.update=true"
  - "wud.update.type=patch"
```

### 4.3 Pre-Deployment Scanning
Before deploying ANY new image or version:
```bash
# Vulnerability scan
docker scout cves <image>:<tag> --only-severity critical,high

# If critical CVEs found: DO NOT DEPLOY. Wait for patch or find alternative.
```

---

## §5 — RESOURCE LIMITS (LOAD-BEARING)

> **Hardware Context**: `DESKTOP-U5E7NRV` — Intel i5-3570K (4 cores), 24GB RAM,
> AMD RX 570, ASMedia 106x SATA on D:\ (unstable under load).
> WSL2 capped at 8GB via `.wslconfig`. A documented system crash occurred on
> 2026-06-10 when Docker + gaming saturated RAM and triggered the faulty SATA controller.

### 5.1 Local Container Budget
| Resource | Total Budget | Rationale |
|----------|-------------|-----------|
| **Memory** | ≤ 8GB total | WSL2 cap = 8GB; reserves 16GB for Windows + OBS + IDE |
| **CPU** | ≤ 3.0 cores | Reserves 1 core for Windows scheduler |
| **Disk I/O** | SSD only for active volumes | D:\ HDD reserved for cold backups only |

### 5.2 Per-Service Caps
```yaml
# EVERY service MUST include resource limits. No exceptions.
deploy:
  resources:
    limits:
      memory: 1024M       # Hard cap — OOM kill above this
      cpus: '1.0'         # Hard cap — throttled above this
    reservations:
      memory: 256M        # Guaranteed minimum
      cpus: '0.25'        # Guaranteed minimum
```

| Service Type | Memory Limit | CPU Limit |
|-------------|-------------|-----------|
| Databases (MariaDB, PostgreSQL, Redis) | 2048M | 1.0 |
| Application services (HA, WordPress, Node-RED) | 1024M | 1.0 |
| Monitoring/utilities (Dozzle, cAdvisor, WUD) | 512M | 0.5 |
| Background workers (backup, DIUN) | 256M | 0.25 |

### 5.3 Gaming/Streaming Mode
When gaming or streaming on `DESKTOP-U5E7NRV`, non-essential local containers
MUST be paused to prevent resource contention:
```powershell
# Enter gaming mode — pauses all non-essential local stacks
.\scripts\pause-local-stacks.ps1 -Mode gaming

# Enter streaming mode — keeps streaming stack, pauses rest
.\scripts\pause-local-stacks.ps1 -Mode streaming

# Resume normal operation
.\scripts\pause-local-stacks.ps1 -Mode normal
```

### 5.4 Dell Server Resource Policy
- The Dell server has dedicated resources — no WSL2/gaming contention
- Resource limits still MANDATORY to prevent runaway containers
- Individual limits set per the Dell server's hardware capacity
- Monitor via cAdvisor + Prometheus + Grafana stack

---

## §6 — HEALTH CHECKS (MANDATORY)

### 6.1 Every Service Gets a Health Check
Docker's default `status: running` only verifies PID 1 is alive — not that
the application is functional. Health checks are MANDATORY.

```yaml
# ── PROTOCOL-SPECIFIC HEALTH CHECK EXAMPLES ──────────────
# HTTP service
healthcheck:
  test: ["CMD", "curl", "-fsS", "http://localhost:8080/health"]
  interval: 15s
  timeout: 3s
  retries: 3
  start_period: 15s

# PostgreSQL
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
  interval: 10s
  timeout: 5s
  retries: 5
  start_period: 30s

# MariaDB / MySQL
healthcheck:
  test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
  interval: 10s
  timeout: 5s
  retries: 5
  start_period: 30s

# Redis
healthcheck:
  test: ["CMD", "redis-cli", "ping"]
  interval: 10s
  timeout: 3s
  retries: 3
  start_period: 10s

# MQTT (EMQX)
healthcheck:
  test: ["CMD", "emqx", "ctl", "status"]
  interval: 15s
  timeout: 5s
  retries: 3
  start_period: 30s
```

### 6.2 Dependency Ordering
```yaml
services:
  app:
    depends_on:
      db:
        condition: service_healthy     # Wait for DB to be READY, not just RUNNING
      redis:
        condition: service_healthy
```

### 6.3 Auto-Remediation
Deploy `willfarrell/autoheal` in every monitoring stack:
```yaml
autoheal:
  image: willfarrell/autoheal:latest
  restart: unless-stopped
  environment:
    AUTOHEAL_CONTAINER_LABEL: autoheal
    AUTOHEAL_INTERVAL: 30
    AUTOHEAL_START_PERIOD: 60
  volumes:
    - /var/run/docker.sock:/var/run/docker.sock:ro
  # NOTE: This is the ONE exception to the socket proxy rule.
  # Autoheal requires direct socket access to restart containers.
  # It is a trusted, minimal, read-heavy container.
  # JUSTIFICATION: Autoheal needs docker.sock to issue restart commands.
  # The socket-proxy would need ALLOW_RESTARTS=1 which defeats its purpose.
```

Target containers opt-in via label: `labels: [autoheal=true]`

---

## §7 — LOGGING

### 7.1 Global Defaults
Applied via YAML anchors in every compose file AND as daemon-level safety net:

```yaml
# In compose files:
x-logging: &default-logging
  logging:
    driver: "json-file"
    options:
      max-size: "50m"
      max-file: "3"
      tag: "{{.Name}}/{{.ID}}"     # Structured log tags for aggregation

# Apply to every service:
services:
  any-service:
    <<: *default-logging
```

### 7.2 Daemon-Level Safety Net
Configured in `daemon.json` — catches containers that forget to set logging:
```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "50m",
    "max-file": "3"
  }
}
```

### 7.3 Centralized Viewing
- **Local**: Dozzle for real-time container log streaming
- **Remote**: Dozzle multi-host mode connecting to Dell server via socket-proxy
- **Aggregation (future)**: Grafana Loki + Alloy for long-term log search and correlation

### 7.4 Sensitive Log Scrubbing
- Container logs MUST NOT contain Tier 0 or Tier 1 secrets
- Applications should use environment variables like `LOG_LEVEL=warn` in production
- Database query logging MUST be disabled in production containers

---

## §8 — BACKUP & RECOVERY

### 8.1 What Gets Backed Up
| Layer | Method | Target | Frequency |
|-------|--------|--------|-----------|
| **Compose configs** | Git commit + push | GitHub/remote | Every change |
| **Encrypted secrets** | Infisical Vault | secrets.sythsaz.ca | Upon creation |
| **Database dumps** | `scripts/remote-backup.ps1` | `D:\Docker\Backups\` | Daily |
| **Named volumes** | `offen/docker-volume-backup` | `D:\Docker\Backups\` | Daily |
| **Container images** | Registry (Docker Hub/GHCR) | N/A — re-pullable | N/A |

### 8.2 Database Dump Protocol
**NEVER** copy raw database files from a running container. Always use dump utilities:
```bash
# MariaDB
docker exec mariadb mysqldump --all-databases --single-transaction | gzip > backup.sql.gz

# PostgreSQL
docker exec postgres pg_dumpall -U postgres | gzip > backup.sql.gz

# Redis
docker exec redis redis-cli BGSAVE
# Then copy /data/dump.rdb

# SQLite (Home Assistant)
docker exec homeassistant sqlite3 /config/home-assistant_v2.db ".backup /tmp/ha_backup.db"
```

### 8.3 Retention Policy (3-2-1 Rule)
- **3 copies**: Live data + local backup (D:\) + offsite
- **2 media types**: SSD (live) + HDD (D:\Docker\Backups\)
- **1 offsite**: Configurable (Backblaze B2, Cloudflare R2, or remote server)

Retention schedule:
```
Keep 7 daily | 4 weekly | 6 monthly
```

### 8.4 Restore Drills
- **Monthly**: Pick one random service, restore from backup to a test container
- **Quarterly**: Full disaster recovery simulation — rebuild from Git + backups
- A backup that has never been tested is not a backup

---

## §9 — NETWORKING

### 9.1 Network Architecture
```
                    ┌─────────────────────────────────┐
                    │         OPNsense Firewall        │
                    │    WAN ←→ VLANs ←→ LAN Rules     │
                    └──────┬──────────────┬────────────┘
                           │              │
                    ┌──────▼──────┐ ┌─────▼──────────┐
                    │  LAN / VLAN │ │   IoT VLAN     │
                    │  10.0.1.x   │ │   10.0.20.x    │
                    └──────┬──────┘ └─────┬──────────┘
                           │              │
                    ┌──────▼──────────────▼────────────┐
                    │        Dell Server (Docker)       │
                    │                                   │
                    │  proxy-net (external bridge)       │
                    │  ├── Traefik/Caddy (ingress)      │
                    │  └── WordPress (frontend only)    │
                    │                                   │
                    │  ha-net (internal bridge)          │
                    │  ├── Home Assistant                │
                    │  ├── MQTT/EMQX                    │
                    │  ├── Zigbee2MQTT                  │
                    │  └── Node-RED                     │
                    │                                   │
                    │  db-net (internal bridge)          │
                    │  ├── MariaDB                      │
                    │  └── Redis                        │
                    │                                   │
                    │  media-net (internal bridge)       │
                    │  ├── Plex                          │
                    │  ├── Frigate NVR                   │
                    │  └── MediaMTX                     │
                    └───────────────────────────────────┘
```

### 9.2 Network Rules
- **Per-stack isolation**: Each stack creates its own bridge network
- **Internal networks**: Use `internal: true` for networks that should have no external access
- **proxy-net**: External bridge for ingress — ONLY reverse proxy + web frontends join this
- **Databases NEVER join proxy-net** — they exist solely on internal networks
- **Default bridge disabled**: `daemon.json` sets `"icc": false`

### 9.3 Ingress & Public Exposure
- Public services (WordPress, webhooks) route through:
  `Cloudflare → CF Tunnel → Traefik → Container`
- Direct port-forwarding from OPNsense WAN is PROHIBITED for Docker services
- TLS termination at Traefik with automatic Let's Encrypt certificates

### 9.4 Stripe Webhook Security
```yaml
# Stripe webhook listener MUST:
# 1. Sit behind Traefik with TLS (never direct port exposure)
# 2. Verify Stripe-Signature header cryptographically
# 3. OPNsense alias restricting source to Stripe IP ranges:
#    https://docs.stripe.com/ips
# 4. Rate limit at reverse proxy level
# 5. Log webhook events (excluding payload secrets)
```

### 9.5 Cross-VLAN Discovery
- mDNS (UDP 5353) does not traverse VLANs
- Install OPNsense `os-mdns-repeater` plugin to relay between IoT and LAN VLANs
- Do NOT use Docker `network_mode: host` just for mDNS — use the OPNsense relay

---

## §10 — MCP DOCKER INTEGRATION

### 10.1 Tool Limit Awareness
- Docker MCP Gateway exposes tools from `~/.docker/mcp/registry.yaml`
- **Hard limit**: ≤ 100 tools simultaneously (LLM context cancellation above this)
- Keep `MCP_DOCKER` toggled **OFF** by default in IDE settings
- Enable per-session when actively needed for Docker operations

### 10.2 Canonical Entrypoints
- **Local**: `C:\Users\ashto\.gemini\scripts\run_mcp_docker.ps1`
- **Remote**: `ssh hassio@10.0.1.221 "docker mcp gateway run"` (via settings.json)
- **Batch**: `C:\Users\ashto\.gemini\scripts\run_docker_mcp.bat`

### 10.3 Safety Boundaries
- `path_authority.py` blocks ALL MCP Docker writes to vault paths (ENFORCED)
- `D:\Docker\MCP` is a sandbox for MCP filesystem reads — never production data
- MCP Docker operations MUST NOT bypass Infisical injection for secrets
- Destructive MCP operations require the same user confirmation as CLI commands

---

## §11 — DELL SERVER REMOTE CONTROL (10.0.1.221)

### 11.1 Access Architecture
```
DESKTOP-U5E7NRV ──SSH──▶ hassio@10.0.1.221 ──docker──▶ Containers
                          (key-based auth)
Stream PC ────────SSH──▶ ashto@DESKTOP-U5E7NRV ──relay──▶ Docker MCP Gateway
Laptop ───────────SSH──▶ ashto@DESKTOP-U5E7NRV ──relay──▶ Docker MCP Gateway
```

### 11.2 Source of Truth Hierarchy
1. **Portainer Stack Editor** — primary UI for real-time management
2. **Git Repository** (`stacks/dell-server/`) — audit trail, version control, disaster recovery
3. **Deploy Scripts** — bridge between Git and Dell server

**Workflow**: Edit in Portainer → test → export/sync to Git → commit.
Or: Edit in Git → `deploy-remote.ps1` → verify in Portainer.

### 11.3 Operational Scripts
| Script | Purpose |
|--------|---------|
| `scripts/deploy-remote.ps1 -Stack dell-server/web` | Deploy/update a stack |
| `scripts/remote-health.ps1` | Check all container health + resources |
| `scripts/remote-backup.ps1` | Trigger database dumps + volume backups |
| `scripts/remote-backup.ps1 -Stack dell-server/web` | Backup specific stack |

### 11.4 Remote Security Hardening
- **SSH**: Key-based auth only (`BatchMode=yes`), managed by `Sync-SshAdminKeys.ps1`
- **Socket proxy**: Deploy `wollomatic/socket-proxy` on Dell server for Portainer/Dozzle
- **Firewall**: OPNsense rules restrict SSH access to management VLAN only
- **All §2 hardening rules apply** — enforce during next maintenance window

### 11.5 Dell Server Service Inventory
| Stack | Services | Network |
|-------|----------|---------|
| `dell-server/home-assistant/` | Home Assistant, MQTT/EMQX, Zigbee2MQTT, ESPHome, Node-RED | ha-net |
| `dell-server/web/` | WordPress, MariaDB, Redis | db-net + proxy-net |
| `dell-server/media/` | Plex, Frigate NVR, MediaMTX | media-net |
| `dell-server/infrastructure/` | Portainer, Scrutiny, socket-proxy | socket-proxy-net |
| `dell-server/mcp/` | Docker MCP, HA-MCP, EMQX | mcp-net |

---

## §12 — AGENT DELEGATION

### 12.1 Docker Ownership Matrix
| Agent | Docker Responsibilities |
|-------|----------------------|
| **@homelab** | Infrastructure decisions, stack orchestration, remote deployments, health monitoring, network architecture, OPNsense Docker firewall rules |
| **@ide** | Dockerfile authoring, image builds, compose file code changes, script development, Infisical Tooling |
| **@stream** | Streaming stack configuration, OBS/Streamer.bot Docker integrations, gaming mode coordination |
| **@vault** | Log ALL Docker operations to `00 Shared Brain/Logs/` via `VaultOp.ps1`, document architecture changes |
| **@web** | WordPress container UI/theme changes (delegates cache flush to `infra_maintenance.py`) |
| **@life** | No Docker responsibilities (privacy boundary) |

### 12.2 Destructive Operation Safeguards
The following commands require **explicit user confirmation** before execution.
This integrates with the `accidental-data-loss-prevention` skill:

```
docker system prune          # Removes all unused data
docker volume prune          # DESTROYS volume data permanently
docker rm -f <container>     # Force-kills running container
docker rmi -f <image>        # Removes images (may break running containers)
docker compose down -v       # Tears down stack AND destroys volumes
docker network prune         # Removes unused networks
```

### 12.3 Agent Review Notice
> ⚠️ **ACTION REQUIRED**: All agent definitions in `C:\Users\ashto\.gemini\agents\`
> must be reviewed and updated to include Docker rule compliance. Specifically:
> - `homelab.md` — Add Docker orchestration responsibilities, reference this RULES.md
> - `ide.md` — Add Dockerfile/compose authoring rules, Infisical Tooling
> - `stream.md` — Add streaming stack management, gaming mode script
> - `vault.md` — Add Docker operation logging protocol
> - `web.md` — Add WordPress container management rules
> - `life.md` — Confirm Docker exclusion boundary
>
> Each agent update should reference `C:\Users\ashto\Docker\RULES.md` as the
> authoritative Docker governance document.

---

## §13 — APPENDIX: QUICK REFERENCE

### 13.1 Common Commands
```powershell
# Deploy a remote stack
.\scripts\deploy-remote.ps1 -Stack dell-server/web -Action "up -d"

# Check remote health
.\scripts\remote-health.ps1

# Trigger remote backup
.\scripts\remote-backup.ps1

# Enter gaming mode
.\scripts\pause-local-stacks.ps1 -Mode gaming

# Inject a new secret
infisical secrets set DB_PASSWORD="value" --env prod --path /web

# Scan an image for vulnerabilities
docker scout cves postgres:16.4-alpine --only-severity critical,high

# Configure Infisical Machine Identity
infisical login --method=universal-auth
```

### 13.2 File Locations
| What | Where |
|------|-------|
| Docker rules (this file) | `C:\Users\ashto\Docker\RULES.md` |
| Compose stacks | `C:\Users\ashto\Docker\stacks\` |
| Deploy/health/backup scripts | `C:\Users\ashto\Docker\scripts\` |
| Hardened compose template | `C:\Users\ashto\Docker\templates\service-template.yaml` |
| Infisical config | `~/.infisical.json` |
| Machine token | `~/.infisical-machine.env` |
| Docker daemon config | `C:\Users\ashto\.docker\daemon.json` |
| WSL2 resource limits | `C:\Users\ashto\.wslconfig` |
| MCP Docker entrypoint | `C:\Users\ashto\.gemini\scripts\run_mcp_docker.ps1` |
| Vault infrastructure docs | `10 Infrastructure/` (JD vault) |
| Session logs | `00 Shared Brain/Logs/YYYY-MM/` (via VaultOp.ps1) |
