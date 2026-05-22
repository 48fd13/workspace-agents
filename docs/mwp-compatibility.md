# MWP Compatibility

This kit is inspired by **Model Workspace Protocol (MWP)** from Jake Van Clief and David McDermott: <https://github.com/RinDig/Model-Workspace-Protocol-MWP>.

MWP uses folder structure, Markdown context files, stage contracts, and plain-text outputs as the control surface for sequential human-reviewed AI workflows.

This kit adapts those ideas for OpenCode/Claude and supports two operating modes.

## 1. General folder workflows

Used by `minimal`, `development`, and `personal` templates.

These are best for day-to-day development, note work, reviews, and lightweight repeatable tasks.

## 2. Strict pipeline workflows

Used by `templates/pipeline`.

These follow the paper more directly:

```text
nearest AGENTS.md / tool instructions  Layer 0
CONTEXT.md                            Layer 1
stages/*/CONTEXT.md                   Layer 2
_config/, shared/, references/        Layer 3
input/, output/                       Layer 4
```

## Name mapping

| MWP paper | This kit |
|---|---|
| `CLAUDE.md` | `AGENTS.md` canonical, `CLAUDE.md` compatibility pointer |
| `CONTEXT.md` | `CONTEXT.md` in pipeline template; `_workspace/map/routing-table.md` in general templates |
| `stages/NN_stage/CONTEXT.md` | strict pipeline stage contract |
| `references/`, `_config/`, `shared/` | Layer 3 reference material |
| `output/` | Layer 4 stage artifact and human edit surface |

## When to use strict pipeline mode

Use it for workflows that are:

- repeated
- sequential
- human-reviewed between stages
- artifact-producing
- dependent on previous stage outputs

Do not use it for simple edits, one-off bug fixes, normal Q&A, or small note cleanup.
