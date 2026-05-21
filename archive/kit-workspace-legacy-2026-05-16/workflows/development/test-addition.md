# Test Addition Workflow

Use when adding, improving, or organizing tests without intentionally changing production behavior.

## Process

1. Identify the behavior, edge case, or regression to cover.
2. Inspect existing test style and helpers.
3. Add the smallest useful test.
4. Prefer meaningful assertions over snapshot/noise tests.
5. Keep fixtures focused and readable.
6. Run the focused test.
7. Run broader validation when the touched scope warrants it.
8. Summarize coverage added and validation.

If production code must change to make the test pass, switch to `bug-fix` or `feature-implementation`.
