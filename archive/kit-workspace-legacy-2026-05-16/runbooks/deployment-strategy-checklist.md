# Deployment Strategy Checklist

Review:

- deployment type: rolling, blue/green, canary, recreate, manual
- compatibility between old and new app versions
- database migration ordering
- config/secret/feature-flag ordering
- health checks and readiness gates
- smoke tests and validation
- rollback and data compatibility
- user-visible behavior and downtime expectations
