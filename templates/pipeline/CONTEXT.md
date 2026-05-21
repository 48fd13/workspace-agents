# Pipeline: {{Pipeline Name}}

<!-- Replace {{Pipeline Name}} with a real name.
     Add one sentence describing what this pipeline produces.
     This file is Layer 1 — the agent reads it first after AGENTS.md to orient and route. -->

## Triggers

<!-- Keep these two triggers in every pipeline. They are standard. -->

| Keyword | Action |
|---------|--------|
| `setup` | Run `setup/questionnaire.md` to configure this pipeline |
| `status` | Scan `stages/*/output/` — report COMPLETE (has files) or PENDING for each stage |

## Routing

<!-- One row per stage. Update stage names and paths to match your pipeline.
     The agent uses this table to find the right stage contract. -->

| Task | Go to |
|------|-------|
| Run stage 00 | `stages/00_stagename/CONTEXT.md` |
| Run stage 01 | `stages/01_stagename/CONTEXT.md` |
| Run stage 02 | `stages/02_stagename/CONTEXT.md` |

## Context loading by stage

<!-- This table tells the agent what to load and what to never load at each stage.
     The "Do NOT load" column is a hard constraint — not a suggestion.
     One-way rule: stage N reads from stage N-1 output only. Never read ahead. -->

| Stage | Load | Do NOT load |
|-------|------|-------------|
| 00_stagename | `input/`, `_config/` | all later stage folders |
| 01_stagename | `stages/00_stagename/output/`, `_config/`, `stages/01_stagename/references/` | `input/`, later stage folders |
| 02_stagename | `stages/01_stagename/output/`, `_config/`, `stages/02_stagename/references/` | `input/`, stage 00 references, stage 01 references |

## Layers

<!-- Do not change this section — it is the same for every pipeline. -->

| Layer | Purpose | Location |
|-------|---------|----------|
| Layer 0 | Identity and global rules | nearest `AGENTS.md` |
| Layer 1 | Pipeline routing and shared context | this file |
| Layer 2 | Stage contract | `stages/*/CONTEXT.md` |
| Layer 3 | Reference material | `_config/`, `shared/`, `stages/*/references/` |
| Layer 4 | Working artifacts | `input/`, `stages/*/output/` |

## Operating rules

<!-- Do not change these rules — they enforce the stop-and-review discipline that makes pipelines work. -->

- Execute one stage at a time. Stop after writing output. Do not advance to the next stage without explicit user instruction.
- Each stage output is the human edit surface. The next stage picks up whatever the human left in `output/`.
- Do not reply in chat only. The durable handoff is the file in `output/`.
- Load only what the current stage's Inputs table specifies. The "Do NOT load" column is a hard constraint.
- If a stage seems skippable for the current task, say so and ask the user before skipping.
