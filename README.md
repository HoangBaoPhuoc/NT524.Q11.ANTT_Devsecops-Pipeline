# Defense-in-Depth Approaches for Secure DevSecOps CI/CD Pipelines: Automated Vulnerability Mitigation, Supply Chain Integrity, and Policy-Driven Enforcement

---

## 📌 Overview

This repository demonstrates an end-to-end **secure CI/CD pipeline** designed with a **Defense-in-Depth** approach.  
The pipeline integrates **7 security layers** to ensure early detection, automated gating, and runtime protection.

It is intended for **academic research** and **practical training** in **DevSecOps, Cloud Security, and Secure Software Supply Chain**.

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/HoangBaoPhuoc/NT524.Q11.ANTT_Devsecops-Pipeline.git
cd NT524.Q11.ANTT_Devsecops-Pipeline

# Build sample application
docker build -t myapp:latest ./app

# Run locally
docker run -p 8080:8080 myapp:latest
```

---

## 🏗️ Architect

The pipeline is organized into modular layers:

- Application Layer → app/ (sample web app, Dockerfile, dependencies)
- Infrastructure Layer → terraform/, ansible/, k8s/ (IaC and deployment)
- Security Controls → .github/workflows/, policies/, scripts/
- Documentation & Reports → docs/, reports/, dashboards/

👉 Detailed design and diagrams are available in docs/ARCHITECTURE.md

---

## Security Layers

1. Pre-commit Hooks - Local development security
2. SAST & SCA - Static analysis & dependency scanning
3. IaC Security - Infrastructure as Code validation
4. Container Security - Image scanning & signing
5. DAST - Dynamic application testing
6. Policy Gating - Deployment validation
7. Runtime Security - Production monitoring

---

## Development Workflow

- Developer creates a feature branch and commits code.
- Pre-commit hooks run locally to catch early issues.
- Code is pushed → GitHub Actions CI/CD workflows trigger.
- Pipeline executes multi-stage scans (SAST, SCA, IaC, container).
- Security gates enforce blocking thresholds (e.g., no Critical/High CVEs).
- Deployment to staging with DAST and policy checks.
- If passed, deployment to production with image signing and runtime monitoring.

👉 Step-by-step guide available in docs/RUNBOOK.md
