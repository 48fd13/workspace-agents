# Feature Implementation Workflow

Use for normal feature work where the desired behavior is reasonably clear.

## Process

1. Restate the feature in one sentence.
2. Identify the smallest useful behavior slice.
3. Inspect only relevant files and existing patterns.
4. Choose the simplest implementation path.
5. Add or update tests when the behavior is testable.
6. Implement the feature.
7. Run the smallest relevant validation set.
8. Summarize behavior changed, files changed, validation, and follow-ups.

Escalate to `technical-design-review` or `backend-service-design` if the feature changes service boundaries, data ownership, API contracts, auth, deployment, or infrastructure.
