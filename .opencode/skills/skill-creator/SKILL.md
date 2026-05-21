---
name: skill-creator
description: Use when creating or improving reusable OpenCode/Claude skills, including SKILL.md structure, trigger descriptions, examples, and safety gates.
---

# Skill Creator

Create small, task-specific skills with clear activation conditions.

## Process

1. Define the repeated task.
2. Define when to use and when not to use the skill.
3. Write concise frontmatter:
   - `name`: lowercase hyphenated
   - `description`: what it does and when to trigger
4. Keep the main workflow in `SKILL.md`.
5. Move long examples, references, or scripts into subfolders only when necessary.
6. Add safety gates for external actions, secrets, destructive work, publishing, or installs.
7. Review with `_workspace/workflows/skill-review/WORKFLOW.md`.
