# Pipeline: Feature Development

A general-purpose software development pipeline. Language- and framework-agnostic. Apply to any coding task: feature, bug fix, refactor, migration, or integration.

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run `setup/questionnaire.md` to describe the task and project context |
| `status` | Scan `stages/*/output/` — report COMPLETE (has files) or PENDING per stage |

## Routing

| Task | Go to |
|------|-------|
| Understand the task | `stages/00_understand/CONTEXT.md` |
| Design the solution | `stages/01_design/CONTEXT.md` |
| Implement | `stages/02_implement/CONTEXT.md` |
| Verify | `stages/03_verify/CONTEXT.md` |
| Finalize | `stages/04_finalize/CONTEXT.md` |

## Context loading by stage

| Stage | Load | Do NOT load |
|-------|------|-------------|
| 00_understand | `input/`, `_config/` | all `stages/` folders |
| 01_design | `stages/00_understand/output/`, `_config/`, `shared/` | `input/`, stages 02–04 |
| 02_implement | `stages/01_design/output/`, `_config/`, `shared/` | `input/`, stages 00, 03–04 |
| 03_verify | `stages/02_implement/output/`, `stages/01_design/output/`, `_config/` | `input/`, stages 00, 04 |
| 04_finalize | `stages/03_verify/output/`, `stages/01_design/output/`, `_config/` | `input/`, stages 00–02 references |

## Layers

| Layer | Purpose | Location |
|-------|---------|----------|
| Layer 0 | Identity and global rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Reference material | `_config/`, `shared/`, `stages/*/references/` |
| Layer 4 | Working artifacts | `input/`, `stages/*/output/` |

## Operating rules

- Execute one stage at a time. Stop after writing output. Do not advance without explicit user instruction.
- Each stage output is the human edit surface. The next stage picks up whatever the human left there.
- Do not reply in chat only. The durable handoff is the file in `output/`.
- Load only what the current stage's Inputs table specifies. Do NOT load columns are hard constraints.
- If the task is simple enough to skip a stage, say so and ask the user before skipping.
