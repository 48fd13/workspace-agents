# Skill Security Audit Runbook

Review third-party skills before importing.

Check for:

- command execution
- network calls
- package installation
- credential access
- file deletion or broad mutation
- hidden exfiltration paths
- prompt injection instructions
- overbroad permissions
- unsafe defaults

Decision labels:

- `accept`: safe as-is
- `adapt`: convert into local workflow/runbook and remove risky parts
- `reject`: too risky or irrelevant
