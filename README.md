# Homelab Infrastructure (Zero-Trust Architecture)

[![Built with AI](https://img.shields.io/badge/Built_with-AI-blueviolet?style=for-the-badge)](https://github.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![CI/CD Secret Scanner](https://img.shields.io/github/actions/workflow/status/Sythsaz/docker-stacks/security.yml?label=Secret%20Scan&style=for-the-badge)](https://github.com/Sythsaz/docker-stacks/actions)

This repository manages the Docker infrastructure for my homelab using centralized configuration, GitOps principles, and **Infisical** for Zero-Trust secret injection.

> **Note:** This entire repository architecture, including the automated deployment pipelines and zero-trust security integrations, was constructed through AI Pair Programming.

## 🚀 Architecture Highlights

- **Infisical Zero-Trust:** Absolutely no `.env` files or hardcoded secrets exist on the host machine or in this repository. Secrets are injected at runtime via the Infisical CLI directly into Docker processes and `secrets.yaml` files.
- **GitOps Deployment:** Remote deployment is handled instantly via `deploy-remote.ps1`, which pipes configurations over SSH and natively triggers Infisical secret pulls.
- **Root of Trust:** The `dell-server/security` stack hosts the self-hosted Infisical instance and Authentik, serving as the cryptographic backbone for the rest of the lab.

## 📂 Directory Structure

- `stacks/`: Contains Docker Compose stacks organized by node and application.
- `scripts/`: PowerShell automation scripts.
  - `deploy-remote.ps1`: Primary deployment engine. SSHs into the server, executes Infisical rendering, and spins up stacks.
  - `remote-health.ps1`: Diagnostic tool for checking stack status.
- `.github/`: CI/CD pipelines (Dependabot for Python dependencies, Gitleaks for secret scanning).
- `RULES.md`: Core system guidelines for AI agents interacting with this repository.

## 🛠️ Security Philosophy

- **Zero-Knowledge Commits:** Protected by a local `infisical scan --staged` git pre-commit hook, backed up by a GitHub Actions Gitleaks CI pipeline.
- **Least Privilege:** Containers run as non-root with dropped capabilities wherever possible.
- **No Local State:** Passwords are never written to disk permanently. Even complex configurations (like Home Assistant's `secrets.yaml`) are rendered strictly at deploy-time by Infisical and locked down with `chmod 600`.
