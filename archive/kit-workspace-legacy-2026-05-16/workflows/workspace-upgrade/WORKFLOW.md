# Workspace Upgrade Workflow

Use when updating an existing project's folder-workflow system from this kit.

## Required context

- source kit version and `CHANGELOG.md`
- target project's `AGENTS.md`
- target project's `_workspace/map/routing-table.md` if present

## Process

1. Inspect the target workspace layout.
2. Identify local customizations before overwriting anything.
3. Compare map, workflow, runbook, context, template, and skill files.
4. Preserve project-specific routing and context.
5. Add missing generic workflows/runbooks/templates only when useful.
6. Update version notes or handoff output if the target tracks them.
7. Run `scripts/verify-workspace.py <target>` from this kit when available.

Ask before overwriting customized files.
