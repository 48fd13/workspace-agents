# MWP Authoring Conventions

Rules to follow when building or editing pipelines in this kit. These apply to all files under `templates/pipeline/` and any pipeline created in a workspace's `_workspace/pipelines/`.

## File roles

| File | Role | Size target |
|------|------|-------------|
| `CLAUDE.md` | Folder map — describes the workspace structure for the human | Any |
| `CONTEXT.md` | Router — triggers, routing table, load/don't-load table | 25–80 lines |
| `stages/*/CONTEXT.md` | Stage contract — inputs, process, audit, outputs, review gate | 30–100 lines |
| `_config/`, `shared/`, `references/` | Reference material (Layer 3) — stable rules, guidelines, constraints | Any |
| `input/`, `stages/*/output/` | Working artifacts (Layer 4) — per-run content, changes each run | Any |

**CONTEXT.md files are routers, not content.** If you find yourself writing actual rules or guidelines in a CONTEXT.md, move them to a reference file and add a pointer.

## One-way references

References between stages flow forward only. If Stage 03 reads from Stage 02 output, Stage 02 must not read from Stage 03.

```
Stage 00 → Stage 01 → Stage 02   ✓
Stage 02 → Stage 01               ✗
```

This prevents circular dependencies and keeps each stage independently re-runnable.

## Canonical sources

Every piece of information lives in exactly one file. If the same content appears in two places, one of them should become a pointer to the other.

- Voice rules live in `_config/voice.md` — stages reference it, they do not copy it
- Stage output is the single source of truth for downstream stages — do not paraphrase it in a later stage's contract

## Selective section loading

The Inputs table should specify which *section* of a file to load, not just the file. This keeps the agent's attention focused.

```markdown
| Layer 3 reference | `_config/voice.md` | "Hard Constraints" section only |
```

Only specify full file when every section is needed.

## Do NOT load is a hard constraint

The "Do NOT load" section in a stage contract is not a suggestion. It enforces the context window boundary for that stage. An agent that loads future stage folders or already-consumed inputs will degrade in quality.

## Audit before output

Every stage contract should have an Audit table. The audit runs before writing to `output/`. It is the stage's quality gate — if any check fails, the agent fixes before saving.

## Checkpoints for creative stages

Use checkpoints inside stages where human direction is valuable mid-stage — before a full draft is written, not after. A checkpoint presents options or a brief for the human to steer, then continues only after confirmation.

## Specs define WHAT, not HOW

When a stage produces a specification for the next stage (e.g. an animation spec, a design brief, a technical plan), it defines what the output should be and when things happen — not how to implement it. Leave implementation decisions to the stage that builds.

## setup/questionnaire.md

Every pipeline should have a `setup/questionnaire.md`. It runs once when the user types `setup`. It asks only system-level questions (things that configure the pipeline permanently), not per-run questions (those are asked conversationally at stage 00). After setup, these answers are written into the relevant reference files and never asked again.

## status trigger

When the user types `status`, scan `stages/*/output/` folders. A stage is COMPLETE if its output folder contains files other than `.gitkeep`. Otherwise it is PENDING. Render a simple pipeline diagram showing each stage and its status.
