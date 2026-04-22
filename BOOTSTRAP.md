# Bootstrap Prompt

Use this prompt in a new repository after copying this setup:

```text
Initialize this repository for the OpenCode workflow.

1) Inspect the repo and infer:
- top-level layout and boundaries
- main apps/libs/services and ownership boundaries
- setup/dev/lint/test/build/release commands
- deployment and operational surfaces

2) Create or update:
- AGENTS.md (portable workflow policy only)
- ARCHITECTURE.md (repo map and key flows)
- RUNBOOK.md (validated commands and procedures)
- .opencode/skills/ (add/update skill folders for this repository)
- .opencode/opencode.json alignment (agent prompts, permissions, default lane)
- lane policy alignment: both lanes require planning + open Q&A + explicit approval before writable delegation

3) Enforce risk gates for:
- security/auth and secrets
- billing/payments/funds flow
- destructive or irreversible operations
- external API contract breaks

4) Report back:
- inferred vs assumed items
- missing inputs requiring human confirmation
- files changed

5) Verify setup:
- run `python3 verify-opencode-setup.py`
```
