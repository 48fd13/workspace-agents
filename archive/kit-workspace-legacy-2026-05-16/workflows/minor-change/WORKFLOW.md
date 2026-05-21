# Minor Change Workflow

Use for small, obvious, local, reversible code/config/doc edits with no user-facing design choice.

## Required context

- `AGENTS.md`
- `_workspace/map/safety-rules.md`
- relevant target files
- `_workspace/runbooks/validation.md` when validation is applicable

## Process

1. Confirm the change is minor, local, reversible, and clearly scoped.
2. Read only the target files needed.
3. Make the smallest useful edit.
4. Run the smallest relevant validation command if available and safe.
5. Summarize changed files and validation.

Create an `_workspace/outputs/` artifact only if the change needs a durable handoff.
