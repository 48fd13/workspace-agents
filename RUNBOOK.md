# Runbook

This file is repository-specific and should be generated/updated during bootstrap.

## Setup

- For this machine, `/Users/spider/workspace/agents/.opencode/` is the canonical OpenCode source. Global OpenCode config should symlink `/Users/spider/.config/opencode/opencode.json`, `/Users/spider/.config/opencode/agents`, and `/Users/spider/.config/opencode/skills` to the matching paths under that source.

## Local Development

- Add commands to run services/apps locally.

## Quality Checks

- Add lint/format/test/build commands for touched scope.
- Validate OpenCode setup with `python3 verify-opencode-setup.py` from the repository root.
- OpenCode automatically permits configured read-only/status commands, including read-only git status/diff/log/show/branch/grep/ls-files/rev-parse/remote checks and explicit read-only compound status combos; mutating git commands and broad compound, pipe, redirection, command substitution, `xargs`, and `tee` forms remain ask-gated or denied.
- In OpenCode permissions, automatic validation commands are allowlisted for standalone `general` and `auto-executor`; standard validation remains confirmation-gated through `standard-executor`.

## Release / Deploy

- Add release and deployment procedures if applicable.

## Troubleshooting

- Add high-signal recovery and debugging commands.
