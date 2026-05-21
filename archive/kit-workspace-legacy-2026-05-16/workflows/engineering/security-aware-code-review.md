# Security-Aware Code Review

Use for normal engineering review when security matters but the task is not a formal security audit.

Use `_workspace/runbooks/secure-engineering-checklist.md`.

Check auth/authz, input validation, injection paths, SSRF/path traversal, secrets exposure, sensitive logging, unsafe deserialization, tenant boundaries, and dependency risk.

Report concrete risks with file/line and smallest safe fix.
