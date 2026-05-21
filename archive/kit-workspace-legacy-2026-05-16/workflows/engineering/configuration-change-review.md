# Configuration Change Review

Use for app config, environment variables, feature flags, IaC variables, runtime settings, and config defaults.

Check:

- environment-specific behavior
- secrets vs non-secret config
- safe defaults and missing-value behavior
- rollout/rollback plan
- config drift and naming consistency
- validation command or startup check
- docs/runbook updates

Flag any config that can change production behavior.
