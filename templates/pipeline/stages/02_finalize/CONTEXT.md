# Stage 02: Finalize

## Purpose

Turn the reviewed intermediate artifact into the final deliverable.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../01_process/output/processed-output.md` | Reviewed intermediate artifact |
| Layer 3 reference | `../../_config/` | Stable workspace rules, if relevant |
| Layer 3 reference | `references/` | Stage-specific finalization rules |

## Do NOT load

- `../../input/` — already consumed by stage 00
- `stages/00_intake/references/` or `stages/01_process/references/` — prior stage rules
- Any stage output other than stage 01

## Process

1. Read the reviewed stage 01 output.
2. Produce the final output.
3. Verify alignment with stage 00 and stage 01 decisions.
4. Flag unresolved issues instead of hiding them.

## Outputs

Write to `output/`:

- `final-output.md`
- `validation-note.md` when useful

Do not only respond in chat. The durable handoff for this stage is the file in `output/`.

## Review gate

Stop after writing output. The user reviews the final output before publishing, filing, or using it downstream.
