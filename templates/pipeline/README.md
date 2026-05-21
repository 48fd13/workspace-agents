# Pipeline Template

Use this template when a task is **sequential, reviewable, and repeatable**: it has natural stage boundaries where human review between stages improves the final result, and you expect to run the same pipeline more than once with different input.

Do not use a pipeline for one-shot tasks, simple edits, Q&A, or ad hoc troubleshooting. Those belong in `_workspace/workflows/`.

## When to create a pipeline

Ask: if stage 1 produces bad output, does stage 2 also go wrong?

If yes — this is a pipeline. Getting the early stages right (understanding, design, research) determines the quality of everything downstream. A review gate between stages lets you course-correct before errors propagate.

Examples:
- requirements → design → implementation → verification → finalize
- source material → extraction → synthesis → compressed notes → filing
- intake → analysis → report draft → final output

## Concepts

### Five-layer context hierarchy

Every pipeline stage receives context from exactly the layers it needs — no more.

| Layer | What it is | Where it lives |
|-------|------------|----------------|
| Layer 0 | Identity — nearest `AGENTS.md` tells the agent what workspace it is in | project root |
| Layer 1 | Routing — pipeline `CONTEXT.md` tells the agent which stage handles the task | `CONTEXT.md` |
| Layer 2 | Stage contract — tells the agent what to read, do, and write for this stage | `stages/*/CONTEXT.md` |
| Layer 3 | Reference material — stable rules, conventions, voice guides, config | `_config/`, `shared/`, `stages/*/references/` |
| Layer 4 | Working artifacts — per-run input and stage outputs | `input/`, `stages/*/output/` |

Agents load Layers 0–2 always. They load only the Layer 3 and Layer 4 files the stage contract specifies. Everything else stays unloaded — this keeps the context window focused and model performance high.

### Layer 3 vs Layer 4

| | Layer 3: Reference | Layer 4: Working |
|---|---|---|
| Changes between runs | No | Yes |
| Examples | voice.md, conventions.md, style.md | research-output.md, draft.md |
| Model should | Internalize as constraints | Process as input |
| Configured | Once during setup | Each run |
| Location | `_config/`, `shared/`, `references/` | `input/`, `output/` |

Think of Layer 3 as the recipe (the factory) and Layer 4 as the ingredients (the product).

### One stage, one job

Each stage does one thing and writes one output. A stage that researches does not also draft. A stage that implements does not also verify. This follows Unix's single-responsibility principle and prevents the context window from mixing unrelated concerns.

### Every output is an edit surface

The output of each stage is a plain Markdown file the human can open, read, and edit before the next stage runs. The next stage picks up whatever the human left there. This is the review gate — the human is always in control of what flows forward.

### Do NOT load is a hard constraint

Each stage contract has a "Do NOT load" section. This is not a suggestion — it prevents future stage context from polluting the current stage and forces clean separation of concerns. Agents must respect it.

### Configure the factory, not the product

`_config/` and `shared/` are configured once when the pipeline is set up. They hold stable rules (style, conventions, constraints) that apply to every run. Per-run material (the actual input being processed) goes in `input/` and gets replaced each run.

### Audit before output

Each stage contract includes an Audit section — a checklist the agent runs before writing to `output/`. If any check fails, the agent fixes the issue first. This catches problems before they reach the human review gate.

### One-way references

Stage N reads from Stage N-1's output. Stage N never reads from Stage N+1. Never load future stage folders during the current stage.

## Folder structure

```
pipeline-name/
├── CONTEXT.md              (Layer 1 — routing, triggers, load table, operating rules)
├── README.md               (human-facing description, not loaded by agent)
├── setup/
│   └── questionnaire.md    (run once to configure _config/ — triggered by "setup" keyword)
├── _config/                (Layer 3 — stable rules shared across all stages)
├── shared/                 (Layer 3 — shared reference material across stages)
├── input/                  (Layer 4 — run-specific source material, replaced each run)
└── stages/
    ├── 00_stagename/
    │   ├── CONTEXT.md      (Layer 2 — stage contract)
    │   ├── references/     (Layer 3 — stage-specific reference material)
    │   └── output/         (Layer 4 — human edit surface, input to next stage)
    ├── 01_stagename/
    │   ├── CONTEXT.md
    │   ├── references/
    │   └── output/
    └── 02_stagename/
        ├── CONTEXT.md
        ├── references/
        └── output/
```

No `CLAUDE.md` inside the pipeline. The agent is routed here via the workspace routing table and reads `CONTEXT.md` as Layer 1.

## How to create a pipeline

### 1. Decide if you need a pipeline

The task must be all three:
- **Sequential**: stage 2 depends on stage 1 output
- **Reviewable**: a human should check each stage before the next runs
- **Repeatable**: you will run this pipeline more than once with different input

### 2. Name your stages

Map the natural breakpoints in your workflow. Each stage should have one job. Name them with two-digit prefixes so order is explicit:

```
00_understand → 01_design → 02_implement → 03_verify → 04_finalize
00_intake → 01_extract → 02_synthesize → 03_file
00_research → 01_draft → 02_review → 03_publish
```

Three to five stages is typical. More than six is a signal the pipeline is too complex or stages should be merged.

### 3. Copy this template

```sh
cp -r workflow-kit/templates/pipeline/ _workspace/pipelines/your-pipeline-name/
```

### 4. Edit `CONTEXT.md`

Replace `{{Pipeline Name}}` with a real name and description. Update:
- Routing table (stage names and paths)
- Context loading table (what each stage loads and must not load)
- Add any pipeline-specific operating rules

### 5. Write stage contracts

For each stage, edit `stages/NN_stagename/CONTEXT.md` using `stage-contract-template.md` as the guide. Each contract must define:
- **Inputs**: exact Layer 3 and Layer 4 files to load
- **Do NOT load**: future stages and unrelated files
- **Process**: what the agent does, step by step
- **Audit**: checks to run before writing output
- **Outputs**: what file(s) to write to `output/`
- **Review gate**: explicit stop instruction

### 6. Add reference material

Put stable rules and conventions in `_config/` or `shared/`. Put stage-specific reference material in `stages/NN/references/`. These are Layer 3 — they are configured once and reused across runs.

### 7. Write the setup questionnaire (optional)

If the pipeline needs one-time configuration (style preferences, project conventions, output format), write questions in `setup/questionnaire.md`. The agent runs this when the user types `setup` and writes answers to `_config/`.

## How to run a pipeline

1. Put run-specific source material in `input/`.
2. Tell the agent: `run stage 00_stagename`
3. Agent reads CONTEXT.md → stage contract → loads only specified files → writes to `output/` → stops.
4. Review the output file. Edit if needed.
5. Tell the agent: `run stage 01_stagename`
6. Repeat until the final stage is complete.

Never say "run the whole pipeline" — always invoke one stage at a time.

## Reference files in this template

| File | Purpose |
|------|---------|
| `CONTEXT.md` | Annotated pipeline-level template — copy and fill in |
| `stage-contract-template.md` | Annotated stage contract template — copy into each stage |
| `stage-review-checklist.md` | Human checklist for reviewing stage output before proceeding |
| `setup/questionnaire.md` | Template for the setup trigger questionnaire |
