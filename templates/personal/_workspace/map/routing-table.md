# Routing Table

| User request | Workflow | Required context / skill |
|---|---|---|
| Learn a topic | `_workspace/workflows/learning/WORKFLOW.md` | `_workspace/context/learning-principles.md` |
| Clean up or clarify a note | `_workspace/workflows/note-processing/WORKFLOW.md` | `_workspace/context/vault-rules.md` |
| Extract article/video/webpage notes | `_workspace/workflows/source-processing/WORKFLOW.md` | `_workspace/context/source-processing-rules.md` |
| Polish personal writing | `_workspace/workflows/writing-polish/WORKFLOW.md` | `_workspace/context/writing-voice.md` |
| Multi-step task needing review between steps | pipeline in `_workspace/pipelines/` | pipeline `CONTEXT.md`, stage `CONTEXT.md` |
| General help | no workflow required | read only needed files |
