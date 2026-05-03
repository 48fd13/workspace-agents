## Agent Guide

## Precedence

1. Runtime/platform instructions (system/developer/tooling)
2. `AGENTS.md`
3. Task-specific user requests

If instructions conflict, follow the highest priority and call out the conflict.

## Core Principles

- Keep the default `general` agent safely executable for local work; keep `standard` and `auto` as explicit optional planning lanes.
- Execute non-trivial or risky work only after explaining the plan/assumptions and receiving required confirmation.
- Make the smallest change that satisfies the request.
- Follow repository conventions and existing patterns.
- Surface assumptions and trade-offs explicitly.
- If docs and code differ, trust code and report the mismatch.

## Lane Model

- `general`: default safe standalone agent for Q&A, exploration, planning, local code/docs/config edits, writing, tests, and validation. It executes normal local work directly within safety gates and may use `explore` for read-only search-heavy orientation.
- `standard`: primary conversational/planning lane. It plans directly with the user and delegates approved executable work to `standard-executor`.
- `auto`: primary conversational/planning lane. It plans directly with the user and delegates eligible work to `auto-executor` under the rules below.
- `standard` and `auto` remain explicit optional lanes; use them only when the user chooses that workflow.
- Executors handle lane-specific code, docs, config, tests, local operations, and validation within risk gates.
- Optional manual specialists (`code-reviewer`, `security-auditor`, `performance-analyzer`) may be tagged explicitly by the user for read-only, findings-only analysis. They are not automatic and are not part of the default delivery flow.

## Default Delivery Flow (Non-Trivial Work)

1. `general` explores current code and context as needed.
2. For small, clear, local, reversible tasks, `general` may implement directly.
3. For non-trivial, risky, or ambiguous work, `general` explains the plan/assumptions and asks before proceeding.
4. `general` performs scoped code/docs/config/tests/local validation directly after required confirmation.
5. If the user explicitly chooses `standard` or `auto`, follow that lane's planning/delegation rules instead.

Optional specialist review/security/performance analysis is manual-only and runs only on explicit user request.

Use judgment for trivial tasks and skip unnecessary steps.

## Auto vs Standard

- `standard` always requires user approval before executable work is delegated to `standard-executor`.
- `auto` may delegate minor, obvious Tier 1 local reversible work directly to `auto-executor` when no user-facing design choice exists.
- `auto` must display a plan and receive explicit acceptance before delegating non-minor Tier 1 or Tier 2 work.
- `general` is not required to route normal implementation work to either lane.

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
- `standard` and `auto` primaries may use configured read-only/status bash for exploration, including explicit read-only compound status allowlist entries, but do not validate or run state-changing commands.
- Broad compound, pipe, redirection, command substitution, `xargs`, and `tee` shell forms remain ask-gated unless a specific read-only status pattern is allowlisted in config.
- `general` or lane executors run the smallest relevant validation set before handoff, within safety gates.
- Run the smallest relevant verification set before handoff.
- Avoid destructive commands unless explicitly required and confirmed.

## Skill Routing

Load skills proactively when the task matches.

| Task type | Skill name |
|---|---|
| Initializing this workflow in a new or existing repository (bootstrap docs/config alignment) | `repo-bootstrap` |

If a task spans multiple skill areas, load all relevant skills.

## Documentation Responsibilities

Store repository-specific details in these docs:

- `ARCHITECTURE.md`: repository layout, ownership boundaries, key modules, data/control flows.
- `RUNBOOK.md`: executable setup/dev/build/test/release commands.
- `.opencode/skills/`: active skills and loading instructions.
- `BOOTSTRAP.md`: one-shot bootstrap prompt and initialization checklist.

When architecture, commands, or routing changes, update the corresponding doc.
