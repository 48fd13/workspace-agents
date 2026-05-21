# Bug Fix Workflow

Use for normal bugs with a known symptom, failing test, error, or reproduction.

## Process

1. Capture observed behavior, expected behavior, and reproduction/failure output.
2. Locate the smallest relevant code path.
3. Form one concrete hypothesis at a time.
4. Prefer adding or updating a failing test that reproduces the bug.
5. Make the smallest fix that addresses the root cause.
6. Run the focused test or reproduction.
7. Run broader validation for the touched scope.
8. Summarize root cause, fix, and validation.

Escalate to `debugging` when the cause is unknown or reproduction is unclear.
