# Stage 00: Understand

Clarify the task, explore the relevant codebase, and surface unknowns before any design or code is written.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../../input/` | Task description, ticket, requirements |
| Layer 3 reference | `../../_config/` | Project stack and conventions, if present |

## Do NOT load

- Any `stages/` folder — do not read ahead
- `shared/` unless explicitly needed

## Process

1. Read the task input and restate it in your own words: what is being asked, what is the expected outcome.
2. Identify the relevant area of the codebase — files, modules, services likely touched.
3. Identify what is known, what is assumed, and what is genuinely unknown.
4. Surface constraints: backwards compatibility, API contracts, data shape, performance, security implications.
5. Flag risks: things that could go wrong, areas of high complexity or fragility.
6. State the smallest useful scope — what is the minimum that satisfies the task.
7. List open questions that need answers before or during design.

Do not propose solutions yet. This stage is about understanding, not deciding.

## Audit

| Check | Pass condition |
|-------|----------------|
| Task restated clearly | The output captures the goal without ambiguity |
| Relevant code identified | The affected area is named, not guessed |
| Unknowns explicit | Assumptions are labeled as assumptions |
| Risks named | At least one risk or constraint is surfaced if any exist |
| Scope is bounded | A minimum viable scope is stated |

## Outputs

Write to `output/`:

- `task-brief.md` — task restatement, affected area, knowns/unknowns, constraints, risks, scope, open questions

Do not only respond in chat. The durable handoff is the file in `output/`.

## Review gate

Stop after writing `task-brief.md`. Wait for the user to review and edit before stage 01 runs. Open questions should be answered before proceeding.
