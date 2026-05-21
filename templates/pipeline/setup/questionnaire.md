# Setup Questionnaire

<!-- Agent instructions: Read this file when the user types "setup".
     Ask all questions in a single conversational pass.
     After collecting answers, write them into the relevant _config/ and shared/ files.
     When done, confirm what was configured and tell the user where to start. -->

<!-- Rules for authoring questions:
     1. Ask only system-level questions — things that configure the pipeline permanently.
     2. Per-run details (topic, input, subject) are asked conversationally at stage 00, not here.
     3. Every question should have a default so the user can skip what they don't care about.
     4. After setup, these answers should never need to be asked again. -->

### Q1: [Question text]
- Writes to: `_config/[file].md`
- Type: free text
- Default: [default value]

### Q2: [Question text]
- Writes to: `_config/[file].md`
- Type: selection
- Options: Option A, Option B, Option C

---

## After setup

Tell the user:
- What was configured and where it was written
- How to start the first stage (`stages/00_intake/CONTEXT.md`)
- That they can re-run `setup` at any time to reconfigure
