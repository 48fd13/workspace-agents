# Routing Table

Use this table to choose the workflow before reading more files.

| User request | Workflow | Required files |
|---|---|---|
| Clarify a vague request before work | `_workspace/workflows/requirements-clarity/WORKFLOW.md` | `AGENTS.md`, `_workspace/context/engineering-principles.md` |
| Create an implementation plan | `_workspace/workflows/implementation-plan/WORKFLOW.md` | `AGENTS.md`, relevant repo files |
| Record a technical decision | `_workspace/workflows/decision-record/WORKFLOW.md` | `AGENTS.md`, relevant context |
| Review a technical design | `_workspace/workflows/engineering/technical-design-review.md` | design/spec/context |
| Design a backend service | `_workspace/workflows/engineering/backend-service-design.md` | requirements, existing service context |
| Review an API contract change | `_workspace/workflows/engineering/api-contract-change.md` | `_workspace/runbooks/api-contract-checklist.md`, API spec/routes |
| Review a database migration | `_workspace/workflows/engineering/database-migration-review.md` | `_workspace/runbooks/database-migration-safety.md`, migration files |
| Review config/env changes | `_workspace/workflows/engineering/configuration-change-review.md` | target config/env/IaC files |
| Review dependency upgrade | `_workspace/workflows/engineering/dependency-upgrade-review.md` | `_workspace/runbooks/dependency-upgrade-safety.md`, manifests/lockfiles |
| Review CI/CD pipeline changes | `_workspace/workflows/engineering/ci-cd-pipeline-review.md` | CI/CD files, `_workspace/runbooks/validation.md` |
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
| Small local code/config/doc change | `_workspace/workflows/minor-change/WORKFLOW.md` | `AGENTS.md`, `_workspace/runbooks/validation.md` |
| Non-trivial local code/config/doc change | `_workspace/workflows/code-change/WORKFLOW.md` | `AGENTS.md`, `_workspace/runbooks/validation.md`, relevant repo files |
| Implement a normal feature | `_workspace/workflows/development/feature-implementation.md` | requirements, relevant repo files, `_workspace/runbooks/validation.md` |
| Fix a normal bug | `_workspace/workflows/development/bug-fix.md` | reproduction/error, relevant repo files, `_workspace/runbooks/validation.md` |
| Refactor without behavior change | `_workspace/workflows/development/refactor.md` | target files, `_workspace/runbooks/validation.md` |
| Add or improve tests | `_workspace/workflows/development/test-addition.md` | target behavior/files, `_workspace/runbooks/validation.md` |
| Documentation-only change | `_workspace/workflows/documentation-change/WORKFLOW.md` | `AGENTS.md`, relevant docs |
| Test-first feature or bug fix | `_workspace/workflows/tdd/WORKFLOW.md` | `_workspace/runbooks/validation.md`, relevant tests/code |
| Debug failing behavior | `_workspace/workflows/debugging/WORKFLOW.md` | `_workspace/runbooks/validation.md`, failing output/logs |
| Fix failing tests | `_workspace/workflows/test-fixing/WORKFLOW.md` | `_workspace/runbooks/validation.md`, failing tests/output |
| Create QA test plan | `_workspace/workflows/qa-test-plan/WORKFLOW.md` | relevant requirements/spec |
| Review code or a diff | `_workspace/workflows/review/code-review.md` | target files or diff |
| Security review | `_workspace/workflows/review/security-review.md` | target files or diff |
| Performance review | `_workspace/workflows/review/performance-review.md` | target files or diff |
| API design review | `_workspace/workflows/review/api-design-review.md` | API routes/spec/schema |
| Dependency review | `_workspace/workflows/review/dependency-review.md` | lockfiles/manifests |
| Generate or improve repo documentation | `_workspace/workflows/documentation/WORKFLOW.md` | `_workspace/runbooks/readme-writing.md`, relevant repo files |
| Generate codebase onboarding docs | `_workspace/workflows/codebase-onboarding/WORKFLOW.md` | `ARCHITECTURE.md`, `RUNBOOK.md`, relevant repo files |
| Create or improve a skill | `_workspace/workflows/skill-authoring/WORKFLOW.md` | `_workspace/runbooks/skill-import-checklist.md` |
| Review a skill before use | `_workspace/workflows/skill-review/WORKFLOW.md` | `_workspace/runbooks/skill-security-audit.md`, target skill |
| Create session handoff | `_workspace/workflows/session-handoff/WORKFLOW.md` | current task context |
| Run retrospective / lesson learned | `_workspace/workflows/retrospective/WORKFLOW.md` | recent changes/session notes |
| Finish branch / PR prep | `_workspace/workflows/finish-branch/WORKFLOW.md` | `_workspace/runbooks/git-commit.md`, `_workspace/runbooks/changelog.md` |
| Create release notes | `_workspace/workflows/release-notes/WORKFLOW.md` | `_workspace/runbooks/changelog.md`, git history/diff |
| Bootstrap this workflow into a repo | `_workspace/workflows/repo-bootstrap/WORKFLOW.md` | `.opencode/skills/repo-bootstrap/SKILL.md`, `_workspace/runbooks/opencode-setup.md` |
| Upgrade an existing folder-workflow workspace | `_workspace/workflows/workspace-upgrade/WORKFLOW.md` | source kit `CHANGELOG.md`, target `_workspace/` |
| OpenCode config generation | `_workspace/runbooks/config-generation.md` | `.opencode/config/README.md` |
| Initialize a workspace from a template | `scripts/init-workspace.py` | `templates/`, target directory |
| Verify a folder-workflow workspace | `scripts/verify-workspace.py` | target directory |
| General Q&A / explanation | no workflow required | read only files needed to answer |

If no route fits, ask one short clarifying question or proceed with the closest safe workflow and state the assumption.
