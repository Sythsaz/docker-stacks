# Homelab Docker Management Workspace

This workspace manages the Docker infrastructure for the homelab using centralized configuration, GitOps principles, and SOPS for secret management.

## Machine Topology

The homelab Docker infrastructure is distributed across several nodes:
- **DESKTOP-U5E7NRV**: Local Docker Desktop environment.
- **debian-dell**: Remote Docker host.
- **Stream PC + Laptop MCP**: Relay nodes for cross-device management.

## Directory Structure

- `stacks/`: Contains Docker Compose stacks organized by application/service.
  - `stacks/<stack_name>/compose.yaml`: The main deployment file.
  - `stacks/<stack_name>/secrets/`: Encrypted `.enc` files and template files for SOPS.
- `templates/`: Base templates and examples for creating secure Compose files and secrets.
- `scripts/`: PowerShell scripts for deployment, management, and Vault operations.
- `RULES.md`: Core system and security rules (see `RULES.md`).

## Quick-Start Guide

1. **Bootstrap SOPS**: Run `scripts/bootstrap-sops.ps1` to generate age keys and populate `.sops.yaml`.
2. **Create a Stack**: Copy `templates/service-template.yaml` to `stacks/my-app/compose.yaml` and customize.
3. **Manage Secrets**: Copy `templates/sops-secret-template.yaml` to `stacks/my-app/secrets/my-secret.yaml`, fill it, and encrypt it using SOPS.
4. **Deploy**: Use your preferred deployment script or Portainer to pull from Git and decrypt the `.enc` files locally.

## Security Philosophy

- **Least Privilege**: Containers drop all capabilities, run as non-root, and have read-only filesystems by default.
- **Secret Management**: All sensitive data is encrypted at rest using SOPS + age and only decrypted as `.txt` files at deployment time.
- **Resource Constraints**: CPU, memory, and PIDs are limited to prevent resource starvation and fork bombs.
- **GitOps First**: Git is the single source of truth for all configurations and encrypted secrets.

## Operations and Integration

- **Portainer**: Used as the primary UI and stack editor. Git serves as the sync and backup mechanism for stack configurations managed in Portainer.
- **Agent Delegation**: System agents are configured to automate routine tasks across the homelab. **Note: ALL agents need review for Docker rule compliance** before making automated changes.
