# opencode-setup

A reusable **OpenCode orchestration baseline** you can copy into any repository.

It provides a two-lane workflow (`standard` and `auto`) with delegation-first execution, plus a bootstrap path that generates repo-specific docs.

## What this repo includes

- `.opencode/opencode.json` — agent registry, permissions, and defaults
- `AGENTS.md` — portable execution policy (workflow, risk gates, done criteria)
- `ARCHITECTURE.md` — repository map and boundaries (repo-specific)
- `RUNBOOK.md` — executable command reference (repo-specific)
- `BOOTSTRAP.md` — one-shot prompt for initializing a copied setup
- `.opencode/agents/` — primary orchestrators and specialist subagents
  - primary: `standard`, `auto`
  - standard specialists: `standard-plan`, `standard-build`, `standard-devops`, `standard-docs-writer`
  - auto specialists: `auto-plan`, `auto-build`, `auto-devops`, `auto-docs-writer`
  - shared specialists: `explore`, `code-reviewer`, `security-auditor`, `performance-analyzer`
- `.opencode/skills/` — bundled, loadable skills (`repo-bootstrap`)

## Lane model (core workflow)

Both lanes are **delegation-first**: primary orchestrators do not directly edit files or run state-changing commands. They route execution to specialist subagents.

### `standard` lane (default)

- Confirmation-oriented orchestration
- Delegates executable work to `standard-*` specialists
- Explicitly confirms plan/approach before implementation for non-trivial tasks

### `auto` lane

- Auto-lane orchestration
- Delegates executable work to `auto-*` specialists
- Requires plan + open Q&A + explicit user approval before writable delegation

## Delegation flow (non-trivial task)

Typical flow is:

1. `explore` to map files and context
2. lane planner (`standard-plan` or `auto-plan`) to produce execution plan
3. lane builder (`standard-build` or `auto-build`) to implement
4. `code-reviewer` for a review pass

Additional specialists (docs, devops, security, performance) are invoked when the task scope requires them.

## Permission and safety model (high level)

- Primary orchestrators (`standard`, `auto`) are configured as orchestration-only (no direct write/edit/bash execution).
- Both lanes require planning with open questions resolved and explicit user approval before writable delegation.
- Write/command execution happens in subagents with scoped permissions.
- Baseline command guardrails in `.opencode/opencode.json` deny clearly dangerous operations (for example force-reset or recursive destructive deletes).
- Both lanes enforce stop-and-confirm for high-risk changes such as:
  - security/auth model changes
  - billing/payment or funds-flow changes
  - destructive/irreversible operations
  - external API contract breaks

## Skill discovery (zero config)

- OpenCode discovers skills by convention from `.opencode/skills/<skill-name>/SKILL.md`.
- No `.opencode/opencode.json` setting is needed for a skills directory path.
- Run `python3 verify-opencode-setup.py` after copying to validate required paths.

## How to use this in another repo

1. Copy these files/folders into the target repo root:
   - `.opencode/opencode.json`
   - `AGENTS.md`
   - `.opencode/agents/`
   - `.opencode/skills/`
2. Run the prompt in `BOOTSTRAP.md` to generate/update repo-specific docs:
   - `ARCHITECTURE.md`
   - `RUNBOOK.md`
   - `.opencode/skills/` (add/remove skills relevant to the repo)
3. Keep `AGENTS.md` mostly portable and policy-focused.
4. Adjust `.opencode/opencode.json`:
   - set your preferred `default_agent` (`standard` or `auto`)
   - tune permission rules for your environment
   - keep delegation boundaries intact unless you intentionally want direct execution in primaries
5. Reload/restart OpenCode so agent/skill config is re-read.
6. Run `python3 verify-opencode-setup.py` to confirm setup integrity.

## Notes

- Current default agent in this repo is `standard`.
- The included `repo-bootstrap` skill is intended to reduce manual customization after copy.
