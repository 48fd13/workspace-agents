# Stage NN: Stage Name

## Purpose

One sentence describing this stage's single job.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../previous_stage/output/file.md` | Previous stage artifact |
| Layer 3 reference | `../../_config/file.md` | Stable workspace rule |
| Layer 3 reference | `references/file.md` | Stage-specific rule |

## Do NOT load

- List files and folders that must not be loaded for this stage
- Typically: future stage folders, unrelated reference material, already-consumed inputs

## Process

1. Step one.
2. Step two.
3. Step three.

## Checkpoints (optional)

| After step | Agent presents | Human decides |
|------------|---------------|---------------|
| N | What the agent shows | What the human chooses before the agent continues |

## Audit

Run these checks before saving to `output/`. If any fail, fix before writing output.

| Check | Pass condition |
|-------|---------------|
| [Check name] | [What passing looks like] |

## Outputs

Write to `output/`:

- `artifact-name.md`

Do not only respond in chat. The durable handoff is the file in `output/`.

## Review gate

Stop after writing output. Wait for the user to review and approve before the next stage runs.

## Verify (optional)

Checks for consistency with earlier stages or source material.
