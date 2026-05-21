# Database Migration Safety

Review migrations for:

- backward compatibility with old and new app versions
- lock duration and table size risk
- online index creation where supported
- nullable/default/backfill ordering
- data migration retry/idempotency
- rollback or forward-fix strategy
- validation queries before and after
- backups/snapshots when risk is high

Ask before irreversible data operations.
