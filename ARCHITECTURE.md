# Architecture

This file is repository-specific and should be generated/updated during bootstrap.

## Repository Map

- Add top-level directories and their responsibilities.

## Boundaries

- Define ownership and coupling boundaries between apps/libs/services.

## Key Flows

- Document important runtime and data flows.

## Critical Contracts

- List external APIs, schemas, and shared interfaces that should not be changed casually.
- OpenCode config lives in `.opencode/opencode.json`; prompt paths are relative to `.opencode` and use `{file:agents/...}`. Active default workflow agents are `general`, `standard`, `standard-executor`, `auto`, and `auto-executor` (with `explore` as a read-only helper). Optional manual specialists (`code-reviewer`, `security-auditor`, `performance-analyzer`) are taggable for explicit findings-only review and are not in automatic delegation paths. Bash permissions use explicit deny/ask guards, read-only allowlists for exploration/status, and automatic validation allowlists only for `auto-executor`.
