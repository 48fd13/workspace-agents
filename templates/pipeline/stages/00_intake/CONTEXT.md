# Stage 00: Intake

## Purpose

Clarify the input, scope, and intended pipeline output.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../../input/` | User-provided source/input for this run |
| Layer 3 reference | `../../_config/` | Stable workspace rules, if relevant |

## Do NOT load

- `stages/01_process/` or later — do not read ahead
- `shared/` unless explicitly needed for intake

## Process

1. Read the run input.
2. Identify goal, constraints, missing information, and target output.
3. Do not perform downstream processing yet.
4. Produce a concise intake brief.

## Outputs

Write to `output/`:

- `intake-brief.md`

Do not only respond in chat. The durable handoff for this stage is the file in `output/`.

## Review gate

Stop after writing output. Wait for the user to review and edit `output/intake-brief.md` before stage 01 runs.
