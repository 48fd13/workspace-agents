# Global OpenCode Instructions

Prefer the nearest project `AGENTS.md`.

If `_workspace/map/routing-table.md` exists, use it to find the relevant workflow or pipeline.
Read only task-relevant workflow, runbook, context, and skill files.

When the routing table points to a pipeline: read the pipeline `CONTEXT.md`, then the current stage `CONTEXT.md`. Execute one stage, write output to that stage's `output/`, then stop and wait for the user before proceeding to the next stage.

Do not create `_workspace/` or project workflow files unless the user asks.

Ask before destructive, machine-wide, deploy/publish, dependency,
infrastructure, secret/auth, billing/payment, or irreversible data operations.

Do not hardcode secrets. Do not commit unless explicitly asked.
