## Folder Workflow Kit Agent Guide

## Precedence

1. Runtime/platform instructions (system/developer/tooling)
2. `AGENTS.md`
3. Task-specific user requests

If instructions conflict, follow the highest priority and call out the conflict.

## Core Principles

- This repository is the reusable OpenCode/Claude folder-workflow kit.
- The daily machine-level router is `/Users/spider/workspace/_workspace/`, not this repo.
- Use kit docs, templates, scripts, and skills as the control surfaces when maintaining this repo.
- Keep one active executable agent: `general`.
- Do not route normal work through agent lanes, executors, or specialist agents.
- Execute non-trivial or risky work only after explaining the plan/assumptions and receiving required confirmation.
- Make the smallest change that satisfies the request.
- Follow repository conventions and existing patterns.
- Surface assumptions and trade-offs explicitly.
- If docs and code differ, trust code and report the mismatch.

## Kit Layout

- `docs/`: framework concepts, template selection, kit maintenance, migration notes.
- `templates/`: copyable project/vault workspaces and artifact templates.
- `scripts/`: workspace initialization and verification utilities.
- `.opencode/AGENTS.md`: global OpenCode instruction file (symlinked to `~/.config/opencode/AGENTS.md` by `setup.sh`).
- `.opencode/`: OpenCode runtime config, prompts, skills, generated config sources.
- `.opencode/skills/`: reusable on-demand task knowledge.

## Default Delivery Flow

1. Read this `AGENTS.md`.
2. Read only the relevant docs/templates/scripts/config files for the task.
3. Use `/Users/spider/workspace/_workspace/` for machine-level routing when the task spans folders.
4. For small, clear, local, reversible tasks, implement directly.
5. For non-trivial, risky, or ambiguous work, create/describe a plan and ask before proceeding.
6. Execute scoped local work directly in `general` within safety gates.
7. Run the smallest relevant validation set.
8. Save durable cross-workspace plans, validations, reviews, or handoffs in `/Users/spider/workspace/_workspace/outputs/` when useful.

Use judgment for trivial tasks and skip unnecessary ceremony.

## Stop-And-Confirm Cases

- Security/auth model changes or secret handling
- Billing/payment or funds-flow changes
- Data-loss risk (destructive/irreversible operations)
- External API contract breaks
- Shared infrastructure changes outside local/dev scope
- Deploy, publish, push, cluster, or terraform mutations

Proceed autonomously only for minor, obvious local reversible scoped work that does not change agreed behavior or require a user-facing design choice.

## Done Criteria

- Changed code builds for the touched scope.
- Formatting/lint passes for the touched scope.
- Tests for changed behavior pass, or tests are added when missing.
- Contract/config/schema changes are documented.
- Any deviation from plan is explained in handoff.

## Command Policy

- Prefer repository-local scripts and workspace tooling.
- `general` may use configured safe read-only/status and validation commands for local work.
- Broad compound, pipe, redirection, command substitution, `xargs`, and `tee` shell forms remain ask-gated unless a specific read-only status pattern is allowlisted in config.
- Run the smallest relevant verification set before handoff.
- Avoid destructive commands unless explicitly required and confirmed.

## Skill Routing

Load skills proactively when the task matches.

| Task type | Skill name |
|---|---|
| Creating, rebuilding, renaming, or repairing this machine-level workflow kit | `workflow-kit-bootstrap` |
| Initializing this workflow in a new or existing repository (bootstrap docs/config alignment) | `repo-bootstrap` |

If a task spans multiple skill areas, load all relevant skills.

## Documentation Responsibilities

Store repository-specific details in these docs:

- `ARCHITECTURE.md`: repository layout, ownership boundaries, key modules, data/control flows.
- `docs/`: framework concepts, maintenance notes, migration notes, and kit maintenance commands.
- `templates/`: reusable project/vault/artifact templates.
- `scripts/`: initialization and verification tools.
- `.opencode/skills/`: active skills and loading instructions.

When architecture, commands, or routing changes, update the corresponding doc.
