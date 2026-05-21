#!/usr/bin/env python3
"""Verify the OpenCode folder-workflow baseline."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / ".opencode" / "opencode.json"
BUILD_CONFIG_PATH = ROOT / ".opencode" / "scripts" / "build-config.py"
SOURCE_CONFIG_PATH = ROOT / ".opencode" / "config" / "base.json"
PERMISSIONS_DIR = ROOT / ".opencode" / "config" / "permissions"

REQUIRED_PATHS = [
    CONFIG_PATH,
    BUILD_CONFIG_PATH,
    SOURCE_CONFIG_PATH,
    PERMISSIONS_DIR / "agents.json",
    PERMISSIONS_DIR / "bash-readonly.json",
    PERMISSIONS_DIR / "bash-validation.json",
    PERMISSIONS_DIR / "bash-risky-ask.json",
    PERMISSIONS_DIR / "bash-shell-risky-ask.json",
    PERMISSIONS_DIR / "bash-destructive-deny.json",
    ROOT / ".opencode" / "config" / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "CLAUDE.md",
    ROOT / "CHANGELOG.md",
    ROOT / "VERSION",
    ROOT / ".opencode" / "AGENTS.md",
    ROOT / "scripts" / "init-workspace.py",
    ROOT / "scripts" / "verify-workspace.py",
    ROOT / "docs" / "README.md",
    ROOT / "docs" / "concepts.md",
    ROOT / "docs" / "template-selection.md",
    ROOT / "docs" / "kit-maintenance.md",
    ROOT / "docs" / "mwp-compatibility.md",
    ROOT / "docs" / "mwp-conventions.md",
    ROOT / "docs" / "artifacts" / "plan-template.md",
    ROOT / "docs" / "artifacts" / "handoff-template.md",
    ROOT / "docs" / "artifacts" / "stage-contract-template.md",
    ROOT / "docs" / "artifacts" / "stage-review-checklist.md",
    ROOT / "templates" / "minimal" / "AGENTS.md",
    ROOT / "templates" / "development" / "AGENTS.md",
    ROOT / "templates" / "personal" / "AGENTS.md",
    ROOT / "templates" / "pipeline" / "CONTEXT.md",
    ROOT / ".opencode" / "agents" / "general.md",
    ROOT / ".opencode" / "skills" / "repo-bootstrap" / "SKILL.md",
    ROOT / ".opencode" / "skills" / "workflow-kit-bootstrap" / "SKILL.md",
]

RETIRED_AGENT_PROMPTS = [
    ROOT / ".opencode" / "agents" / "standard" / "standard.md",
    ROOT / ".opencode" / "agents" / "standard" / "executor.md",
    ROOT / ".opencode" / "agents" / "auto" / "auto.md",
    ROOT / ".opencode" / "agents" / "auto" / "executor.md",
    ROOT / ".opencode" / "agents" / "code-reviewer.md",
    ROOT / ".opencode" / "agents" / "security-auditor.md",
    ROOT / ".opencode" / "agents" / "performance-analyzer.md",
]

VALIDATION_BASH_PATTERNS = [
    "npm test*",
    "npm run test*",
    "npm run lint*",
    "npm run typecheck*",
    "npm run check*",
    "npm run build*",
    "npm run format:check*",
    "pnpm test*",
    "pnpm run test*",
    "pnpm lint*",
    "pnpm run lint*",
    "pnpm typecheck*",
    "pnpm run typecheck*",
    "pnpm check*",
    "pnpm run check*",
    "pnpm build*",
    "pnpm run build*",
    "pnpm run format:check*",
    "yarn test*",
    "yarn lint*",
    "yarn typecheck*",
    "yarn check*",
    "yarn build*",
    "yarn format:check*",
    "bun test*",
    "bun run test*",
    "bun run lint*",
    "bun run typecheck*",
    "bun run check*",
    "bun run build*",
    "pytest*",
    "python -m pytest*",
    "python3 -m pytest*",
    "python -m unittest*",
    "python3 -m unittest*",
    "ruff check*",
    "python -m ruff check*",
    "python3 -m ruff check*",
    "mypy*",
    "pyright*",
    "python -m compileall*",
    "python3 -m compileall*",
    "go test*",
    "go vet*",
    "go list*",
    "cargo test*",
    "cargo check*",
    "cargo clippy*",
    "cargo build*",
    "cargo fmt --check*",
    "make test*",
    "make lint*",
    "make check*",
    "make verify*",
    "make build*",
    "mvn test*",
    "mvn verify*",
    "./mvnw test*",
    "./mvnw verify*",
    "gradle test*",
    "gradle check*",
    "./gradlew test*",
    "./gradlew check*",
    "python3 verify-opencode-setup.py",
]

REQUIRED_READ_ONLY_PATTERNS = [
    "pwd",
    "ls",
    "ls *",
    "rg *",
    "grep *",
    "cat ./*",
    "head *",
    "tail *",
    "wc *",
    "file *",
    "stat *",
    "du -sh *",
    "tree *",
    "git status",
    "git status *",
    "git status*",
    "git diff*",
    "git log*",
    "git show*",
    "git branch*",
    "git ls-files*",
    "git grep*",
    "git rev-parse*",
    "git remote -v*",
]

REQUIRED_ASK_PATTERNS = [
    "npm install*",
    "pnpm install*",
    "yarn install*",
    "bun install*",
    "pip install*",
    "brew install*",
    "apt install*",
    "sudo apt*",
    "curl *",
    "wget *",
    "ssh *",
    "scp *",
    "rsync *",
    "docker *",
    "docker compose *",
    "kubectl *",
    "helm *",
    "terraform *",
    "mkdir *",
    "touch *",
    "rmdir *",
    "mv *",
    "cp *",
    "chmod *",
    "chown *",
    "git push*",
    "git add*",
    "git commit*",
    "git checkout*",
    "git switch*",
    "git restore*",
    "git merge*",
    "git rebase*",
    "git pull*",
    "git fetch*",
    "git tag*",
    "git stash*",
    "git worktree*",
    "git submodule*",
    "*>*",
    "*>>*",
    "*|*",
    "*&&*",
    "*;*",
    "*`*",
    "*$(*",
    "* xargs *",
    "tee *",
]

REQUIRED_DENY_PATTERNS = [
    "rm -rf *",
    "rm -r *",
    "sudo rm*",
    "find * -delete*",
    "find * -exec rm*",
    "chmod -R *",
    "chown -R *",
    "dd *",
    "mkfs*",
    "terraform destroy*",
    "kubectl delete*",
    "helm uninstall*",
    "docker system prune*",
    "docker volume rm*",
    "git push --force*",
    "git reset --hard*",
    "git clean*",
    "git branch -D *",
]


def load_config(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise RuntimeError(f"failed to parse {path.name}: {exc}")


def build_generated_config() -> dict:
    try:
        spec = importlib.util.spec_from_file_location("opencode_build_config", BUILD_CONFIG_PATH)
        if spec is None or spec.loader is None:
            raise RuntimeError("failed to load build-config.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.build_config()
    except Exception as exc:
        raise RuntimeError(f"failed to build generated config from source: {exc}")


def extract_prompt_paths(value) -> list[str]:
    paths: list[str] = []
    if isinstance(value, dict):
        for nested in value.values():
            paths.extend(extract_prompt_paths(nested))
    elif isinstance(value, list):
        for nested in value:
            paths.extend(extract_prompt_paths(nested))
    elif isinstance(value, str):
        match = re.fullmatch(r"\{file:(.+)\}", value.strip())
        if match:
            paths.append(match.group(1))
    return paths


def bash_permission(agent_config: dict) -> dict:
    permission = agent_config.get("permission", {})
    bash = permission.get("bash", {})
    return bash if isinstance(bash, dict) else {}


def file_has_disable_true(path: Path) -> bool:
    text = path.read_text()
    return bool(re.search(r"(?m)^disable:\s*true\s*$", text))


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_PATHS:
        if not path.exists():
            errors.append(f"missing required path: {path.relative_to(ROOT)}")

    legacy_config_path = ROOT / "opencode.json"
    if legacy_config_path.exists() or legacy_config_path.is_symlink():
        errors.append("legacy root opencode.json must not exist")

    for retired_prompt in RETIRED_AGENT_PROMPTS:
        if retired_prompt.exists() and not file_has_disable_true(retired_prompt):
            errors.append(f"retired agent prompt must contain disable: true: {retired_prompt.relative_to(ROOT)}")

    if CONFIG_PATH.exists():
        try:
            config = load_config(CONFIG_PATH)
            generated_config = build_generated_config()
            if generated_config != config:
                errors.append(".opencode/opencode.json is stale; run python3 .opencode/scripts/build-config.py")

            if config.get("model") != "ollama/gemma4:e2b":
                errors.append("model must be ollama/gemma4:e2b")
            if config.get("default_agent") != "general":
                errors.append("default_agent must be general")

            agents = config.get("agent", {})
            allowed_runtime_agents = {"general", "plan", "build"}
            for agent_name in agents:
                if agent_name not in allowed_runtime_agents:
                    errors.append(f"runtime config must not include retired agent: {agent_name}")
            for disabled_builtin in ["plan", "build"]:
                if agents.get(disabled_builtin, {}).get("disable") is not True:
                    errors.append(f"built-in agent must be disabled: {disabled_builtin}")

            general_config = agents.get("general", {})
            general_permission = general_config.get("permission", {})
            general_tools = general_config.get("tools", {})
            if general_config.get("mode") != "primary":
                errors.append("general must be a primary agent")
            if general_permission.get("edit") != "allow":
                errors.append("general must allow direct edit permission")
            if general_permission.get("task") != "deny":
                errors.append("general must deny task delegation")
            for tool_name in ["write", "edit", "bash", "read", "grep", "glob", "webfetch"]:
                if general_tools.get(tool_name) is not True:
                    errors.append(f"general tool must be enabled: {tool_name}")

            bash_targets = [
                ("global/default", config.get("permission", {}).get("bash", {})),
                ("general", bash_permission(general_config)),
            ]
            for target_name, bash in bash_targets:
                if bash.get("*") != "ask":
                    errors.append(f"{target_name} bash fallback must be ask")
                for pattern in REQUIRED_READ_ONLY_PATTERNS:
                    if bash.get(pattern) != "allow":
                        errors.append(f"{target_name} must allow read-only bash pattern: {pattern}")
                for pattern in REQUIRED_ASK_PATTERNS:
                    if bash.get(pattern) != "ask":
                        errors.append(f"{target_name} must ask-gate bash pattern: {pattern}")
                for pattern in REQUIRED_DENY_PATTERNS:
                    if bash.get(pattern) != "deny":
                        errors.append(f"{target_name} must deny bash pattern: {pattern}")
            general_bash = bash_permission(general_config)
            for pattern in VALIDATION_BASH_PATTERNS:
                if general_bash.get(pattern) != "allow":
                    errors.append(f"general must allow validation pattern: {pattern}")

            prompt_paths = extract_prompt_paths(config.get("agent", {}))
            for prompt_path in sorted(set(prompt_paths)):
                if not prompt_path.startswith("agents/"):
                    errors.append(f"prompt path must start with agents/: {prompt_path}")
                if prompt_path.startswith(".opencode/") or prompt_path.startswith("/"):
                    errors.append(f"prompt path must be relative to .opencode: {prompt_path}")
                full_path = CONFIG_PATH.parent / prompt_path
                if not full_path.exists():
                    errors.append(f"prompt file not found: {prompt_path}")
        except RuntimeError as exc:
            errors.append(str(exc))

    if errors:
        print("OpenCode folder-workflow setup check failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OpenCode folder-workflow setup check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
