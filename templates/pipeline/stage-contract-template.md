# Stage NN: Stage Name

<!-- One sentence describing this stage's single job.
     Copy this file into stages/NN_stagename/CONTEXT.md and fill it in.
     Delete all comments before use. -->

## Inputs

<!-- List every file the agent should load for this stage.
     Distinguish Layer 3 (stable reference, same every run) from Layer 4 (working artifact, changes each run).
     Be explicit — the agent loads exactly what is listed here and nothing else. -->

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../00_previous/output/artifact.md` | Output from the previous stage |
| Layer 3 reference | `../../_config/conventions.md` | Stable project rules |
| Layer 3 reference | `references/stage-specific.md` | Reference material for this stage only |

## Do NOT load

<!-- Hard constraint. List what must not be loaded during this stage.
     Always include: future stage folders, unrelated reference material, already-consumed inputs. -->

- `stages/NN_next/` and later — do not read ahead
- `../../input/` — already consumed in stage 00
- `shared/` — unless explicitly needed for this stage

## Process

<!-- Step-by-step instructions for the agent. Be specific about what good looks like.
     Do not describe what to do in vague terms — encode the best practice for this phase. -->

1. Step one.
2. Step two.
3. Step three.

## Checkpoints (optional)

<!-- Use checkpoints for stages where the agent should pause mid-stage and show intermediate work
     before continuing. Useful for creative or high-stakes decisions within a stage. -->

| After step | Agent presents | Human decides |
|------------|----------------|---------------|
| 2 | Draft of X | Approve or redirect before step 3 |

## Audit

<!-- Checks the agent runs before writing to output/. If any check fails, fix first.
     Make pass conditions concrete and verifiable. -->

Run these checks before saving to `output/`. If any fail, fix before writing output.

| Check | Pass condition |
|-------|----------------|
| [Check name] | [What passing looks like — specific, not vague] |

## Outputs

<!-- Name every file the agent writes to output/. One file per artifact.
     The output/ folder is the human edit surface — the next stage reads whatever the human left here. -->

Write to `output/`:

- `artifact-name.md` — one-line description of what this file contains

Do not only respond in chat. The durable handoff is the file in `output/`.

## Review gate

Stop after writing output. Wait for the user to review and edit `output/artifact-name.md` before the next stage runs.
