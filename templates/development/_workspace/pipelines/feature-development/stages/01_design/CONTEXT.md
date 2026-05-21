# Stage 01: Design

Produce a concrete solution design based on the understood task. The design is the contract for implementation — it must be approved before any code is written.

## Inputs

| Layer | Path | Use |
|-------|------|-----|
| Layer 4 working | `../00_understand/output/task-brief.md` | Clarified task, risks, scope, open questions |
| Layer 3 reference | `../../_config/` | Project conventions, architecture rules |
| Layer 3 reference | `../../shared/` | Shared patterns and constraints |

## Do NOT load

- `../../input/` — already consumed in stage 00
- `stages/02_implement/` or later — do not read ahead

## Process

1. Read the task brief. Treat open questions as resolved if the user answered them; flag if still open.
2. Propose an approach: what changes, where, and why. Prefer the simplest solution that meets the requirement.
3. Identify the specific files, modules, functions, or interfaces to be created or modified.
4. Describe the data flow or control flow change if relevant.
5. Consider alternatives: name at least one alternative approach and explain why it was not chosen.
6. Address the risks from stage 00: how does the design handle or mitigate each one?
7. Define the interface or contract: what does the change expose, accept, or return?
8. State what will not be changed and why (non-goals).
9. Flag any design decisions that need user input before implementation begins.

The design should be specific enough that a developer (or the agent in stage 02) could implement it without guessing.

## Audit

| Check | Pass condition |
|-------|----------------|
| Approach is concrete | Files and change locations are named, not described vaguely |
| Risks addressed | Each risk from stage 00 is handled or accepted with rationale |
| Alternative considered | At least one alternative is named and rejected with reason |
| Interface defined | What the change exposes or accepts is explicit |
| Non-goals stated | What is out of scope is named |
| No open questions blocking implementation | All blockers are resolved or escalated |

## Outputs

Write to `output/`:

- `design.md` — approach, affected files, data/control flow, alternatives considered, risk handling, interface definition, non-goals, open decisions

Do not only respond in chat. The durable handoff is the file in `output/`.

## Review gate

Stop after writing `design.md`. Wait for the user to review and approve the design before any implementation begins. The user may edit the design directly — stage 02 picks up whatever is there.
