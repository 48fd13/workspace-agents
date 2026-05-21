# Concepts

The system has three layers.

## 1. Root workspace

```text
/Users/spider/workspace
```

This is the machine-level starting point and router. Its `_workspace/` stays small and only decides where work should happen.

## 2. Framework kit

```text
/Users/spider/workspace/workflow-kit
```

This is the reusable kit. It provides OpenCode config, templates, scripts, skills, docs, and global instructions.

The kit should not act as the main machine router. It should be maintainable as a normal repo.

## 3. Target workspace

A target repo or vault gets its own local workflow only when useful:

```text
target/
├── AGENTS.md
├── CLAUDE.md
└── _workspace/
```

Examples:

- backend repo → `templates/development`
- Obsidian vault → customized personal workspace
- tiny project → `templates/minimal`

## Rule of thumb

Root routes. Kit provides. Target owns local context.
