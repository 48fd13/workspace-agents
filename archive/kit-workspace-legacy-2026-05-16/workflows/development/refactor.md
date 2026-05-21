# Refactor Workflow

Use for behavior-preserving cleanup, simplification, renaming, extraction, or structure changes.

## Process

1. State the intended refactor and the behavior that must remain unchanged.
2. Identify tests or validation that protect the behavior.
3. Keep the refactor scoped and reversible.
4. Avoid mixing refactor with feature or behavior changes.
5. Make small incremental changes.
6. Run validation before and/or after when practical.
7. Summarize what changed structurally and how behavior was protected.

If behavior changes are needed, switch to `feature-implementation` or `bug-fix`.
