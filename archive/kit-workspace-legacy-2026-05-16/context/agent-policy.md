# Agent Policy Context

This repository intentionally avoids agentic routing as the normal workflow.

Active behavior:

- one active primary agent: `general`
- no default delegation to lanes, executors, or specialists
- workflows and checklists replace agent chains
- skills provide reusable task knowledge on demand
- outputs are saved as files when durable state is useful

Retired prompts remain in `.opencode/agents/` as disabled reference material during migration.
