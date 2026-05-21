# Routing Table

| User request | Workflow | Required files |
|---|---|---|
| Small local code/config/doc change | `_workspace/workflows/minor-change/WORKFLOW.md` | `AGENTS.md`, target files |
| Non-trivial local change | `_workspace/workflows/code-change/WORKFLOW.md` | `AGENTS.md`, `_workspace/runbooks/validation.md` |
| Implement a normal feature | `_workspace/workflows/development/feature-implementation.md` | requirements, relevant repo files, `_workspace/runbooks/validation.md` |
| Fix a normal bug | `_workspace/workflows/development/bug-fix.md` | reproduction/error, relevant repo files, `_workspace/runbooks/validation.md` |
| Refactor without behavior change | `_workspace/workflows/development/refactor.md` | target files, `_workspace/runbooks/validation.md` |
| Add or improve tests | `_workspace/workflows/development/test-addition.md` | target behavior/files, `_workspace/runbooks/validation.md` |
| Review a technical design | `_workspace/workflows/engineering/technical-design-review.md` | design/spec/context |
| Design a backend service | `_workspace/workflows/engineering/backend-service-design.md` | requirements, service context |
| Review an API contract change | `_workspace/workflows/engineering/api-contract-change.md` | `_workspace/runbooks/api-contract-checklist.md`, API spec/routes |
| Review a database migration | `_workspace/workflows/engineering/database-migration-review.md` | `_workspace/runbooks/database-migration-safety.md`, migration files |
| Review config/env changes | `_workspace/workflows/engineering/configuration-change-review.md` | target config/env/IaC files |
| Review dependency upgrade | `_workspace/workflows/engineering/dependency-upgrade-review.md` | `_workspace/runbooks/dependency-upgrade-safety.md`, manifests/lockfiles |
| Review CI/CD pipeline changes | `_workspace/workflows/engineering/ci-cd-pipeline-review.md` | CI/CD files |
| Review Terraform/IaC change | `_workspace/workflows/engineering/terraform-change-review.md` | `_workspace/runbooks/terraform-plan-reading.md`, Terraform files/plan |
| Review containerization changes | `_workspace/workflows/engineering/containerization-review.md` | `_workspace/runbooks/docker-container-safety.md`, Docker/container files |
| Review Kubernetes manifests | `_workspace/workflows/engineering/kubernetes-manifest-review.md` | `_workspace/runbooks/kubernetes-manifest-checklist.md`, manifests/values |
| Plan a cloud/infrastructure change | `_workspace/workflows/cloud-devops/infrastructure-change-plan.md` | `_workspace/runbooks/cloud-change-safety.md`, IaC/config/context |
| Provision or modify an environment | `_workspace/workflows/cloud-devops/environment-provisioning.md` | `_workspace/runbooks/environment-provisioning.md`, target environment context |
| Review IAM/permissions change | `_workspace/workflows/cloud-devops/iam-permissions-review.md` | `_workspace/runbooks/iam-permissions-checklist.md`, IAM/policy files |
| Review DNS/TLS/networking change | `_workspace/workflows/cloud-devops/network-dns-tls-review.md` | `_workspace/runbooks/network-dns-tls-checklist.md`, network/DNS/TLS config |
| Review deployment strategy | `_workspace/workflows/cloud-devops/deployment-strategy-review.md` | `_workspace/runbooks/deployment-strategy-checklist.md`, app/deploy context |
| Review managed cloud service integration | `_workspace/workflows/cloud-devops/managed-service-integration.md` | `_workspace/runbooks/managed-service-integration.md`, service/config context |
| Review observability instrumentation | `_workspace/workflows/engineering/observability-instrumentation-review.md` | `_workspace/runbooks/observability-instrumentation.md`, service code/config |
| Security-aware engineering review | `_workspace/workflows/engineering/security-aware-code-review.md` | `_workspace/runbooks/secure-engineering-checklist.md`, target files/diff |
| Review performance/scalability | `_workspace/workflows/engineering/performance-scalability-review.md` | target files/diff |
| Review jobs/queues/workers | `_workspace/workflows/engineering/background-job-queue-review.md` | queue/job/worker code/config |
| Review resilience/error handling | `_workspace/workflows/engineering/error-handling-resilience-review.md` | `_workspace/runbooks/backend-resilience-patterns.md`, target files/diff |
| Documentation change | `_workspace/workflows/documentation/WORKFLOW.md` | `_workspace/context/documentation-standards.md` |
| Review code or diff | `_workspace/workflows/review/code-review.md` | target files or diff |
| Security review | `_workspace/workflows/review/security-review.md` | target files or diff |
| Session handoff | `_workspace/workflows/session-handoff/WORKFLOW.md` | current task context |
| Multi-step task needing staged review between steps | pipeline in `_workspace/pipelines/` | pipeline `CONTEXT.md`, stage `CONTEXT.md` |
| General Q&A | no workflow required | read only needed files |
