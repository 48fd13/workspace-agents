# Agent Guide

Use the local folder workflow system as the control plane.

## Workflow order

1. Read this file.
2. Read `_workspace/map/routing-table.md`.
3. Select the matching workflow.
4. Read only required workflow, runbook, context, and skill files.
5. For small, clear, local, reversible tasks, proceed directly.
6. For non-trivial, risky, or ambiguous work, explain the plan and ask before proceeding.
7. Save plans, validations, reviews, and handoffs under `_workspace/outputs/` when useful.

## Workflows vs pipelines

A **workflow** is a one-shot checklist: the agent reads it, does the work, and you see the result at the end.

A **pipeline** is a multi-stage folder structure: the agent executes one stage, writes a file to that stage's `output/`, and stops. You review and optionally edit the file before telling the agent to run the next stage. Use a pipeline when the output of each step needs your judgment before the next step begins.

When the routing table points to a pipeline, read the pipeline's `CONTEXT.md` first, then the current stage's `CONTEXT.md`. Do one stage at a time. Do not proceed to the next stage without explicit user instruction.

## Durable artifact triggers

Treat plans, reviews, validations, and handoffs as workflow artifacts:

- `handoff`, `handoff this`, `save state`, `preserve this`, `continue later` → `_workspace/outputs/handoffs/`
- `plan`, `write a plan` → `_workspace/outputs/plans/`
- `review`, `audit`, `assess` → `_workspace/outputs/reviews/`
- `validation`, `verify`, `check result` → `_workspace/outputs/validations/`

Do not only reply in chat unless the user asks for chat-only. After writing the artifact, reply with the file path, one-line summary, and next action.

## Safety

Ask before destructive or irreversible operations, installs, push/publish/deploy, infrastructure mutations, secrets/auth changes, billing/funds-flow changes, external API contract changes, or irreversible data operations.

Do not commit unless explicitly asked.
