# Background Job / Queue Review

Use for workers, queues, schedulers, async jobs, event handlers, and cron-like tasks.

Check:

- idempotency and deduplication
- retry policy and backoff
- dead-letter / poison message handling
- ordering and concurrency assumptions
- visibility timeout / lease behavior
- backpressure and rate limits
- observability and replay strategy
- cleanup or compensation on partial failure
