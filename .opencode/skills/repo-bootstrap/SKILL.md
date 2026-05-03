# repo-bootstrap

Use this skill when the user asks to initialize, install, bootstrap, or align the OpenCode workflow in a repository.

## Goal

Set up a repository so the workflow is usable immediately with minimal manual customization.

## What to produce

Create or update these files:

- `AGENTS.md` (portable policy only; avoid repo-specific placeholders)
- `ARCHITECTURE.md` (repo map, boundaries, key components, ownership)
- `RUNBOOK.md` (validated setup/dev/lint/test/build/release commands)
- `.opencode/skills/` (skill folders and routing aligned to this repo)
- `BOOTSTRAP.md` (one-shot prompt for re-running setup)

Also verify `.opencode/opencode.json`:

- All referenced agent prompt files exist.
- `default_agent` is standalone `general`; the verifier expects this default, so users should switch lanes explicitly only when desired.
- Permission guardrails include destructive-operation denies.
- Required active agents include standalone `general`, optional lane primaries `standard`/`auto`, and lane executors `standard-executor`/`auto-executor`, with `explore` available as a read-only helper.

## Execution workflow

1. Explore the repo structure and infer boundaries.
2. Discover package/tooling commands and validate the smallest relevant set.
3. Draft/update docs using inferred facts first, assumptions second.
4. If assumptions are required, call them out explicitly in a short "Assumptions" section.
5. Keep edits minimal and consistent with existing conventions.

## Guardrails

- Respect stop-and-confirm gates for security/auth, billing/funds, destructive ops, and API contract breaks.
- Do not invent commands that are not present in project tooling.
- Prefer code as source of truth when docs conflict.

## Handoff format

Return:

1. Files changed
2. What was inferred vs assumed
3. Any missing inputs needed from the user
4. Suggested next verification commands
