# Test Fixing Workflow

Use when tests fail locally or in CI.

## Process

1. Read the failing test name and exact failure output.
2. Determine whether the test, fixture, environment, or production code is wrong.
3. Prefer fixing production code when the test captures intended behavior.
4. Update tests only when the requirement changed or the test is invalid.
5. Run the narrow failing test.
6. Run broader validation for the touched scope.

Report what failed, root cause, changed files, and validation.
