# TDD Workflow

Use for features or bug fixes where tests can define behavior before implementation.

## Process

1. Define the smallest behavior slice.
2. Write or update a failing test that captures expected behavior.
3. Run the focused test and confirm the failure is meaningful.
4. Implement the smallest change to pass.
5. Run the focused test again.
6. Refactor only if needed and keep tests green.
7. Run broader validation for the touched scope.

Do not write implementation first unless the user explicitly chooses a non-TDD approach.
