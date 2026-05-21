# Repo Bootstrap Workflow

Use when installing or aligning this folder-workflow baseline in a repository.

## Required context

- `.opencode/skills/repo-bootstrap/SKILL.md`
- `_workspace/runbooks/opencode-setup.md`
- `_workspace/runbooks/config-generation.md`
- target repository structure

## Process

1. Inspect top-level layout and tooling.
2. Add or update `AGENTS.md` and `_workspace/`.
3. Keep `.opencode/opencode.json` aligned to one active `general` agent and strict permissions.
4. Add repo-specific skills only when repeated task knowledge is useful.
5. Validate the setup.

## Handoff

Return files changed, inferred facts, assumptions, missing inputs, and suggested next verification commands.
