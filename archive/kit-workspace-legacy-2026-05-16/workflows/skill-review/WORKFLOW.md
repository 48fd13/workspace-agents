# Skill Review Workflow

Use before importing or enabling a third-party skill.

## Process

1. Read `SKILL.md` frontmatter and instructions.
2. Inspect scripts and dependencies.
3. Check for external calls, secrets handling, file mutation, shell execution, and prompt injection risk.
4. Decide whether to import as-is, adapt into a local runbook, or reject.
5. Record source, license, risks, and modifications.

Use `_workspace/runbooks/skill-security-audit.md` for the checklist.
