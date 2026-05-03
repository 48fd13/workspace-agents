# opencode-setup

A reusable **OpenCode orchestration baseline** you can copy into any repository.

It provides a default safe standalone `general` agent, optional explicit `standard` and `auto` lanes that delegate executable work to lane executors, plus a bootstrap path that generates repo-specific docs.

## What this repo includes

- `.opencode/opencode.json` — agent registry, permissions, and defaults
- `AGENTS.md` — portable execution policy (workflow, risk gates, done criteria)
- `ARCHITECTURE.md` — repository map and boundaries (repo-specific)
- `RUNBOOK.md` — executable command reference (repo-specific)
- `BOOTSTRAP.md` — one-shot prompt for initializing a copied setup
- `.opencode/agents/` — primary orchestrators and specialist subagents
  - primary: `general`, `standard`, `auto`
  - executors: `standard-executor`, `auto-executor`
  - read-only helper: `explore`
  - optional manual specialists: `code-reviewer`, `security-auditor`, `performance-analyzer`
- `.opencode/skills/` — bundled, loadable skills (`repo-bootstrap`)

## Lane model (core workflow)

Default usage starts with `general`, which can answer, explore, plan, edit/write local files, and validate directly. `standard` and `auto` remain **delegation-first** optional lanes: their primaries plan and converse only, then route execution to executor subagents.

### `general` default

- Q&A, exploration, planning, local code/docs/config edits, writing, tests, and validation
- Direct local implementation for normal safe work; for non-trivial/risky/ambiguous work, explain plan/assumptions and ask before proceeding
- May suggest `standard` or `auto` as optional explicit lanes, but does not require routing for normal work

### `standard` lane

- Confirmation-oriented planning
- Delegates approved code/docs/config/tests/local operations/validation work to `standard-executor`
- Explicitly confirms plan/approach before implementation for non-trivial tasks

### `auto` lane

- Auto-lane planning
- Delegates Tier 1/Tier 2 local reversible scoped work to `auto-executor`
- Uses safe local validation/status commands without asking where configured
- Stops for shared infra/deploy/publish/push/terraform/cluster mutations and routes to standard confirmation

## Default flow (non-trivial task)

Typical flow is:

1. `general` inspects context directly, optionally using read-only `explore`
2. `general` produces and displays a risk-tiered plan/assumptions when work is non-trivial, risky, or ambiguous
3. User accepts the plan when required
4. `general` performs scoped code/docs/config/tests/local operations/validation work directly

If the user explicitly chooses `standard` or `auto`, that lane's executor (`standard-executor` or `auto-executor`) performs the scoped implementation after the lane's required planning/acceptance.

Docs-writing and local operations responsibilities are merged into executors. Code review, security audit, and performance analysis are not automatic default workflow steps; the optional specialists can be tagged explicitly for manual findings-only review.

## Permission and safety model (high level)

- `general` is configured for safe standalone local execution, including write/edit tools and focused validation allowlists.
- `standard` and `auto` primaries are configured as planning-only: no direct write/edit execution, with automatic bash limited to configured read-only exploration/status patterns and explicit read-only compound status combos.
- Primary `standard` and `auto` agents assign risk tiers before implementation.
- `standard` is confirmation-oriented; `auto` may proceed for clear Tier 1/Tier 2 local reversible edits.
- Validation bash is automatic only for `general` and `auto-executor`; `standard-executor`, planning primaries, and explore do not get automatic test/lint/build/typecheck commands.
- Optional manual specialists are read-only/findings-only and are not wired into primary default delegation paths.
- Write/command execution happens in `general` or in explicit lane subagents with scoped permissions, with fallback ask for commands not explicitly allowed or denied.
- Broad compound, pipe, redirection, command substitution, `xargs`, and `tee` shell forms remain ask-gated unless a specific harmless read-only status combo is allowlisted before the broad guard.
- Baseline command guardrails in `.opencode/opencode.json` deny clearly dangerous operations (for example force-reset or recursive destructive deletes).
- Both lanes enforce stop-and-confirm for high-risk changes such as:
  - security/auth model changes
  - billing/payment or funds-flow changes
  - destructive/irreversible operations
  - external API contract breaks
  - shared/prod infra, deploy, publish, push, cluster, or terraform mutations

## Skill discovery (zero config)

- OpenCode discovers skills by convention from `.opencode/skills/<skill-name>/SKILL.md`.
- No `.opencode/opencode.json` setting is needed for a skills directory path.
- Run `python3 verify-opencode-setup.py` after copying to validate required paths.

## How to use this in another repo

1. Copy these files/folders into the target repo root:
   - `.opencode/opencode.json`
   - `AGENTS.md`
   - `verify-opencode-setup.py`
   - `.opencode/agents/`
   - `.opencode/skills/`
2. Run the prompt in `BOOTSTRAP.md` to generate/update repo-specific docs:
   - `ARCHITECTURE.md`
   - `RUNBOOK.md`
   - `.opencode/skills/` (add/remove skills relevant to the repo)
3. Keep `AGENTS.md` mostly portable and policy-focused.
4. Adjust `.opencode/opencode.json`:
   - keep `default_agent` as `general`; the verifier expects this standalone default, so switch lanes explicitly only when desired
   - tune permission rules for your environment
   - keep delegation boundaries intact; `general` executes directly, while `standard`/`auto` delegate to their executors
5. Reload/restart OpenCode so agent/skill config is re-read.
6. Run `python3 verify-opencode-setup.py` to confirm setup integrity.

## Notes

- Current default agent in this repo is `general`.
- The included `repo-bootstrap` skill is intended to reduce manual customization after copy.
