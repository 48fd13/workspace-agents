# Agent Guide

Use the local folder workflow system when present.

## Workflow order

1. Read this file.
2. Read `_workspace/map/routing-table.md`.
3. Select the active workflow.
4. Read only required workflow, runbook, context, and skill files.
5. Save durable outputs under `_workspace/outputs/` when useful.

## Durable artifact triggers

When the user asks for a handoff, plan, review, validation, or saved state, create a Markdown artifact under the matching `_workspace/outputs/` subfolder. Do not only reply in chat unless the user asks for chat-only.

After writing the artifact, reply with the file path, one-line summary, and next action.

## Workflows vs pipelines

A **workflow** is a one-shot checklist: the agent reads it, does the work, and you see the result at the end.

A **pipeline** is a multi-stage folder structure: the agent executes one stage, writes a file to that stage's `output/`, and stops. You review and optionally edit the file before telling the agent to run the next stage. Use a pipeline when the output of each step needs your judgment before the next step begins.

When the routing table points to a pipeline, read the pipeline's `CONTEXT.md` first, then the current stage's `CONTEXT.md`. Do one stage at a time. Do not proceed to the next stage without explicit user instruction.

## Safety

Ask before destructive or irreversible operations, installs, push/publish/deploy, infrastructure mutations, secrets/auth changes, billing/funds-flow changes, external API contract changes, or irreversible data operations.

Do not commit unless explicitly asked.
