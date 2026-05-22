# Folder Workflow Kit

A reusable **AI folder-workflow kit** you can copy into any repository.

It keeps OpenCode as the runtime and permission layer, while moving workflow control into folders, Markdown runbooks, checklists, staged outputs, and skills. The active default is a single `general` agent.

## Attribution

This kit is inspired by **Model Workspace Protocol (MWP)** from Jake Van Clief and David McDermott: <https://github.com/RinDig/Model-Workspace-Protocol-MWP>.

MWP's core idea is that folder structure, Markdown context files, stage contracts, and plain-text outputs can orchestrate sequential human-reviewed AI workflows without a heavyweight multi-agent framework. This kit adapts that idea for OpenCode/Claude, machine-level routing, reusable templates, and vault/project workflows.

## What this repo includes

- `.opencode/opencode.json` — single-agent runtime config, permissions, and defaults
- `AGENTS.md` — portable execution policy, folder workflow rules, risk gates, done criteria
- `CLAUDE.md` — Claude Code pointer that routes to `AGENTS.md`
- `docs/` — framework concepts, template selection, kit maintenance, and migration notes
- `templates/` — bootstrap templates: `minimal`, `work`, `personal`
- `templates/pipeline/` — strict MWP-style staged pipeline template
- `docs/artifacts/` — canonical artifact skeletons (copied into workspace templates)
- `scripts/init-workspace.py` — initialize a directory from a template
- `scripts/verify-workspace.py` — verify any folder-workflow workspace
- `.opencode/AGENTS.md` — global OpenCode instruction file linked by `setup.sh`
- `docs/workflow-kit-bootstrap.md` — cross-tool procedure for creating or repairing the kit/control-plane layer
- `ARCHITECTURE.md` — repository map and boundaries
- `.opencode/agents/` — active `general` prompt only
- `.opencode/skills/` — bundled, loadable skills (`repo-bootstrap`, `workflow-kit-bootstrap`)
- `.opencode/config/` — source config and permission profiles used to generate `opencode.json`
- `.opencode/scripts/` — config generation helpers

## Folder workflow model

Default usage starts with `general`, which reads local `AGENTS.md`, uses a local `_workspace/` when present, otherwise reads the relevant docs/templates/scripts/config files, performs scoped local work, validates, and writes durable handoff artifacts when useful.

There are no default delegation lanes. Former lane/specialist prompts are archived under `archive/retired-agents/`; their useful logic is represented as workflows and checklists.

Typical flow:

1. Read `AGENTS.md`.
2. Use root `/Users/spider/workspace/_workspace/` for machine-level routing when needed.
3. Select the relevant docs, templates, scripts, skills, or config files.
4. Read only the required runbook/context/skill files.
5. Produce a plan or proceed directly for small safe work.
6. Execute within permission and safety gates.
7. Save cross-workspace outputs under `/Users/spider/workspace/_workspace/outputs/` when useful.

## Permission and safety model (high level)

- `general` is configured for safe standalone local execution, including write/edit tools and focused validation allowlists.
- Agent delegation is disabled for the active workflow.
- Review/security/performance work uses checklist/workflow files in target workspaces, not specialist agents.
- Write/command execution happens in `general` with fallback ask for commands not explicitly allowed or denied.
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

## Global OpenCode setup

Install this repo's OpenCode config into your user config with symlinks:

```sh
cd ~/workspace/workflow-kit && ./setup.sh
```

To target a different config directory:

```sh
OPENCODE_CONFIG_DIR=/path/to/opencode ./setup.sh
```

The setup script links the selected `.opencode` entries (`opencode.json`,
`agents/`, `skills/`, `config/`, and `scripts/`) plus the global OpenCode
`AGENTS.md` from `.opencode/AGENTS.md`. It backs up conflicting
destination files or directories before replacing them with symlinks.

Restart OpenCode after running setup.

## Initialize a workspace in another directory

Use a template instead of copying the whole kit manually:

```sh
python3 scripts/init-workspace.py --template minimal /path/to/project
python3 scripts/init-workspace.py --template work /path/to/project
python3 scripts/init-workspace.py --template personal /path/to/vault
python3 scripts/init-workspace.py --template pipeline /path/to/pipeline-workspace
```

Templates:

- `minimal`: smallest useful `AGENTS.md` + `_workspace/`
- `work`: coding/docs/review/validation/handoff workflows
- `personal`: learning, notes, source processing, and writing polish workflows
- `pipeline`: strict MWP-style sequential stage pipeline with `CONTEXT.md`, `stages/`, `references/`, and `output/`; it does not include `AGENTS.md` or `CLAUDE.md`

Verify a target workspace:

```sh
python3 scripts/verify-workspace.py /path/to/project
```

## How to use this in another repo

1. Initialize a template with `scripts/init-workspace.py`.
2. Optionally copy `.opencode/` if the project should carry its own OpenCode runtime config.
3. Run the `repo-bootstrap` skill to generate/update repo-specific docs:
    - `ARCHITECTURE.md`
    - folder workflows/runbooks/context files relevant to the repo
    - `.opencode/skills/` (add/remove skills relevant to the repo)
4. Keep `AGENTS.md` mostly portable and policy-focused.
5. Adjust `.opencode/opencode.json` if copied:
    - keep `default_agent` as `general`
    - tune permission rules for your environment
    - keep agent delegation disabled unless you intentionally reintroduce it
6. Reload/restart OpenCode so agent/skill config is re-read.
7. Run `python3 scripts/verify-workspace.py <target>` to confirm workspace integrity.

## Notes

- Current active agent in this repo is `general`.
- `repo-bootstrap` initializes target repos/folders; `workflow-kit-bootstrap` points OpenCode to the cross-tool kit bootstrap runbook.
