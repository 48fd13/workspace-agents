# Infrastructure Change Plan

Use before cloud, infrastructure, IaC, environment, networking, deployment, or managed-service changes that can affect runtime behavior.

Use `_workspace/runbooks/cloud-change-safety.md`.

## Process

1. State the intended infrastructure outcome.
2. Identify affected environments, services, accounts/projects, regions, and resources.
3. Separate code/config changes from external mutations.
4. Identify blast radius, reversibility, rollout, validation, and rollback.
5. Review cost, security, availability, and operational impact.
6. Ask before any real mutation such as apply, deploy, publish, or remote API change.

This is planning/review only unless the user explicitly approves execution.
