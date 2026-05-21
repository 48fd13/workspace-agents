# Architecture

This file is repository-specific and should be generated/updated during bootstrap.

## Repository Map

- `AGENTS.md`: portable workflow policy and safety gates.
- `docs/`: framework concepts, template selection, kit maintenance, and migration notes.
- `templates/`: portable workspace templates for minimal, work, and personal setups.
- `docs/artifacts/`: canonical artifact skeletons; copied into workspace templates during init.
- `scripts/`: kit-level initialization and verification scripts.
- `.opencode/AGENTS.md`: global OpenCode instruction file linked by `setup.sh`.
- `.opencode/`: OpenCode runtime config, the active `general` prompt, skills, generated config sources, and scripts.

## Boundaries

- Workflow state belongs in target project/vault `_workspace/` folders and Markdown files, not agent delegation chains.
- OpenCode config owns permissions, model/provider settings, and the active `general` prompt.
- Claude compatibility is a pointer file (`CLAUDE.md`) that defers to `AGENTS.md`.
- Skills provide reusable task knowledge only when requested by a workflow or user request.
- Runbooks inside templates own known commands and validation procedures for target workspaces.
- Templates provide starting layouts and should stay smaller than the full kit.

## Key Flows

1. User asks for work.
2. Root `/Users/spider/workspace/_workspace/` routes to this kit when the task concerns templates, OpenCode config, skills, or framework maintenance.
3. `general` reads this repo's `AGENTS.md` and relevant `docs/`, `templates/`, `scripts/`, or `.opencode/` files.
4. `general` performs safe local work directly or asks for approval when gated.
5. `general` validates scripts/config/templates before handoff.

## Critical Contracts

- OpenCode config lives in `.opencode/opencode.json` and is generated from `.opencode/config/base.json` plus permission fragments.
- The active default workflow agent is standalone `general`; retired lane/specialist prompts are archived under `archive/retired-agents/`.
- Bash permissions use explicit deny/ask guards, read-only allowlists for exploration/status, focused validation allowlists for `general`, and ask gates for broad compound, pipe, and redirection forms.
