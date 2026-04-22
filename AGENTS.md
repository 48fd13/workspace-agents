## Agent Guide

## Precedence

1. Runtime/platform instructions (system/developer/tooling)
2. `AGENTS.md`
3. Task-specific user requests

If instructions conflict, follow the highest priority and call out the conflict.

## Core Principles

- Be delegation-first and use specialist agents when they improve quality or speed.
- Plan before coding for non-trivial work.
- Make the smallest change that satisfies the request.
- Follow repository conventions and existing patterns.
- Surface assumptions and trade-offs explicitly.
- If docs and code differ, trust code and report the mismatch.

## Lane Model

- `standard` lane: confirmation-oriented for non-trivial choices.
- `auto` lane: delegation-first orchestration with mandatory planning, open Q&A, and explicit approval before writable delegation.
- In both lanes, primary orchestrators should remain orchestration-only and delegate executable work to specialists.

## Default Delivery Flow (Non-Trivial Work)

1. Explore current code and context.
2. Produce an execution plan.
3. Implement via the appropriate build specialist.
4. Run review and consistency checks when relevant.
5. Validate with the smallest useful set of build/lint/test commands.

Use judgment for read-only trivial tasks and skip unnecessary steps.

## Stop-And-Confirm Cases

- Security/auth model changes or secret handling
- Billing/payment or funds-flow changes
- Data-loss risk (destructive/irreversible operations)
- External API contract breaks
- Shared infrastructure changes outside local/dev scope

Proceed autonomously for low-risk details that do not change agreed behavior.

## Done Criteria

- Changed code builds for the touched scope.
- Formatting/lint passes for the touched scope.
- Tests for changed behavior pass, or tests are added when missing.
- Contract/config/schema changes are documented.
- Any deviation from plan is explained in handoff.

## Command Policy

- Prefer repository-local scripts and workspace tooling.
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
