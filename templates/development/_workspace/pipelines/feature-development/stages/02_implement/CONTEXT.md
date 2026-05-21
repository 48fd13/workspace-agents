# Stage 02: Implement

Write the code as specified in the approved design. Follow the design exactly — do not extend scope, refactor unrelated code, or make undecided design choices during implementation.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../01_design/output/design.md` | Approved solution design |
| Layer 3 reference | `../../_config/` | Project conventions, code style, patterns |
| Layer 3 reference | `../../shared/` | Shared constraints |

## Do NOT load

- `../00_understand/output/` — design already incorporates this
- `stages/03_verify/` or later — do not read ahead
- `../../input/` — already consumed

## Process

1. Read the design. Treat it as the specification — implement what it says.
2. Make the smallest set of changes that fully satisfies the design. Do not gold-plate.
3. Follow existing conventions in the codebase: naming, structure, error handling, logging patterns.
4. Write or update tests where the project has a test suite and the change has testable behavior.
5. Do not refactor code outside the scope of the design. If you notice something worth fixing, note it as a follow-up.
6. If the design is ambiguous on a specific point, make the conservative choice and flag it in the summary.
7. If the implementation reveals a flaw in the design, stop and surface it rather than working around it silently.

## Audit

| Check | Pass condition |
|-------|----------------|
| Design followed | No undecided choices made silently; no scope added |
| Conventions respected | Naming, structure, and patterns match the existing codebase |
| Tests present | New behavior has test coverage if a test suite exists |
| No unrelated changes | Only files specified in the design are modified |
| Deviations flagged | Any deviation from the design is noted and explained |

## Outputs

Write to `output/`:

- `implementation-summary.md` — what was implemented, files changed, deviations from design (if any), tests added, follow-ups identified

Do not only respond in chat. The durable handoff is the file in `output/`.

## Review gate

Stop after writing `implementation-summary.md`. Wait for the user to review the implementation before verification runs.
