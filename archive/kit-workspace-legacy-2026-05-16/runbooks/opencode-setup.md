# OpenCode Setup Runbook

## Install globally from this repo

From `/Users/spider/workspace/workflow-kit`:

```sh
./setup.sh
```

To target another config directory:

```sh
OPENCODE_CONFIG_DIR=/path/to/opencode ./setup.sh
```

## After config changes

1. Regenerate `.opencode/opencode.json` when source config changes.
2. Run `python3 verify-opencode-setup.py`.
3. Restart OpenCode so it reloads config, agents, and skills.
