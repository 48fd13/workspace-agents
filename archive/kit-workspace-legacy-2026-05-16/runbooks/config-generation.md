# Config Generation Runbook

Runtime config is generated. Do not hand-edit permission maps in `.opencode/opencode.json`.

Edit:

- `.opencode/config/base.json`
- `.opencode/config/permissions/*.json`

Then run:

```sh
python3 .opencode/scripts/build-config.py
python3 verify-opencode-setup.py
```

Restart OpenCode after changes.
