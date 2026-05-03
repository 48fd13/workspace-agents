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

- `general`: default read-only Q&A, exploration, triage, and routing. It does not edit or delegate writable work; only configured read-only bash/status commands are automatic.
- `standard` lane: confirmation-oriented primary that plans directly and delegates approved executable work to `standard-executor`.
- `auto` lane: primary that plans directly and delegates eligible Tier 1/Tier 2 local reversible scoped work to `auto-executor`.
- Primary agents remain conversation/planning-only and do not edit, write, validate, or run state-changing commands directly.
- Executors handle code, docs, config, tests, local operations, and validation within their lane's gates.
- Optional manual specialists (`code-reviewer`, `security-auditor`, `performance-analyzer`) may be tagged explicitly by the user for read-only findings-only analysis; they are not part of the default automatic flow.

## Default Delivery Flow (Non-Trivial Work)

1. Explore current code and context as needed.
2. The primary (`standard` or `auto`) produces a risk-tiered execution plan directly.
3. After required approval, execute via `standard-executor` or `auto-executor` as appropriate.
4. Validate with the smallest useful set of build/lint/test commands.

Optional specialist review/security/performance analysis is manual-only and runs only on explicit user request.

Use judgment for read-only trivial tasks and skip unnecessary steps.

## Stop-And-Confirm Cases

- Security/auth model changes or secret handling
- Billing/payment or funds-flow changes
- Data-loss risk (destructive/irreversible operations)
- External API contract breaks
- Shared infrastructure changes outside local/dev scope
- Deploy, publish, push, cluster, or terraform mutations

Proceed autonomously only in the auto lane for clear Tier 1/Tier 2 local reversible scoped work that does not change agreed behavior.

## Done Criteria

- Changed code builds for the touched scope.
- Formatting/lint passes for the touched scope.
- Tests for changed behavior pass, or tests are added when missing.
- Contract/config/schema changes are documented.
- Any deviation from plan is explained in handoff.

## Command Policy

- Prefer repository-local scripts and workspace tooling.
- Read-only exploration/status bash is broadly allowed where configured; validation bash is automatic only for `auto-executor`.
- `standard-executor` asks before validation or non-read bash; everything not explicitly allowed or denied is ask-gated.
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
