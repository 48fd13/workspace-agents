# Backend Resilience Patterns

Review:

- timeouts on external calls
- bounded retries with backoff and jitter
- idempotency for retried mutations
- circuit breakers or fail-fast behavior when useful
- graceful degradation / fallback strategy
- cleanup or compensation for partial failure
- clear user-facing errors
- observability for failure paths
