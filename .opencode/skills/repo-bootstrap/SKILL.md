---
name: repo-bootstrap
description: Use when initializing, installing, bootstrapping, or aligning the OpenCode/Claude folder-workflow system in a repository.
---

# repo-bootstrap

Use this skill when the user asks to initialize, install, bootstrap, or align the OpenCode workflow in a repository.

## Goal

Set up a repository so the folder-workflow system is usable immediately with minimal manual customization.

## What to produce

Create or update these files:

- `AGENTS.md` (portable policy only; avoid repo-specific placeholders)
- `_workspace/` (map, workflows, runbooks, context, outputs)
- `ARCHITECTURE.md` (repo map, boundaries, key components, ownership)
- `.opencode/skills/` (skill folders and routing aligned to this repo)

Also verify `.opencode/opencode.json`:

- All referenced agent prompt files exist.
- `default_agent` is standalone `general`.
- Agentic lane/executor/specialist routing is disabled unless the user intentionally reintroduces it.
- Permission guardrails include destructive-operation denies.
- Required active agent is standalone `general`; workflows/checklists replace lane and specialist agents.

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
