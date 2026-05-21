# Stage 01: Process

## Purpose

Transform the reviewed intake output into the main intermediate artifact.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../00_intake/output/intake-brief.md` | Reviewed intake from previous stage |
| Layer 3 reference | `../../_config/` | Stable workspace rules, if relevant |
| Layer 3 reference | `references/` | Stage-specific rules |

## Do NOT load

- `../../input/` — already consumed by stage 00
- `stages/02_finalize/` — do not read ahead
- Other stage references not listed above

## Process

1. Read the reviewed intake brief.
2. Apply the stage-specific transformation.
3. Preserve constraints and decisions from stage 00.
4. Produce the main intermediate output.

## Outputs

Write to `output/`:

- `processed-output.md`

Do not only respond in chat. The durable handoff for this stage is the file in `output/`.

## Review gate

Stop after writing output. Wait for the user to review and edit `output/processed-output.md` before stage 02 runs.
