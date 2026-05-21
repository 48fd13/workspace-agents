# Safety Rules

Stop and ask before:

- destructive or irreversible operations
- installs or dependency mutations
- push, publish, deploy, release, or external mutation
- Docker/Kubernetes/Helm/Terraform/shared infrastructure mutation
- security/auth model changes or secret handling
- billing, payments, or funds-flow changes
- external API contract breaks
- irreversible data operations

Do not hardcode secrets or credentials.

Do not commit unless the user explicitly asks.

Prefer the smallest reversible local change that satisfies the request.
