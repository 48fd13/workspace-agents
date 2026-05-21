# Validation Runbook

Use the smallest relevant validation set for the touched scope.

Common safe validation commands are allowlisted for `general`, including:

- package tests/lint/typecheck/build commands
- Python test/compile/check commands
- Go, Rust, Java, and Make verification commands
- `python3 verify-opencode-setup.py` for this repository

If no validation command is known, explain what was checked manually and what remains unverified.
