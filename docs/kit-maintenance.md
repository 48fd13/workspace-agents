# Kit Maintenance

Use this doc when changing the framework kit itself.

## Common tasks

| Task | Where |
|---|---|
| Add a reusable project template | `templates/` |
| Add artifact templates | `docs/artifacts/` — canonical source; copy into workspace templates as needed |
| Add or update OpenCode skills | `.opencode/skills/` |
| Update active OpenCode agent prompt | `.opencode/agents/general.md` |
| Update global OpenCode instructions | `.opencode/AGENTS.md` — keep this file as a tiny fallback shim |
| Change runtime permissions | `.opencode/config/permissions/` then regenerate config |
| Update init/verify behavior | `scripts/` |
| Explain framework concepts | `docs/` |
| Author or edit a pipeline | `docs/mwp-conventions.md` — read this first |

## Validation

Run from the kit root:

```sh
python3 -m py_compile scripts/init-workspace.py scripts/verify-workspace.py
python3 verify-opencode-setup.py
python3 scripts/verify-workspace.py templates/minimal
python3 scripts/verify-workspace.py templates/development
python3 scripts/verify-workspace.py templates/personal
```

## Maintenance rules

- Keep root `~/workspace/_workspace/` as the daily router.
- Keep this repo as the reusable kit.
- Keep `.opencode/agents/` to the active `general.md` prompt only.
- Put copyable project state in `templates/`, not in a kit-local `_workspace/`.
- Put explanation in `docs/`.
- Put reusable artifact skeletons in `docs/artifacts/` and copy them into workspace templates.
