#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / ".opencode" / "opencode.json"

READ_ONLY_BASH_AGENTS = [
    "general",
    "standard",
    "auto",
    "explore",
    "standard-executor",
    "auto-executor",
]

OPTIONAL_MANUAL_SPECIALISTS = [
    "code-reviewer",
    "security-auditor",
    "performance-analyzer",
]

PRIMARY_AGENTS = ["general", "standard", "auto"]

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
    "git status*",
    "git diff*",
    "git log*",
    "git show*",
    "git grep*",
    "git ls-files*",
    "git branch --show-current",
]

UNSAFE_READ_ONLY_ALLOW_PATTERNS = ["find . *", "sed -n *"]
REQUIRED_ASK_GUARDS = [
    "*--output*",
    "*--pre*",
    "*--ext-diff*",
    "git grep -O*",
    "git grep --open-files-in-pager*",
    "git grep* -O*",
    "git grep* --open-files-in-pager*",
    "*<(*",
]


def load_config(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        raise RuntimeError(f"failed to parse {path.name}: {exc}")


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


def key_index(mapping: dict, key: str) -> int | None:
    try:
        return list(mapping.keys()).index(key)
    except ValueError:
        return None


def main() -> int:
    errors: list[str] = []

    required_paths = [
        CONFIG_PATH,
        ROOT / "AGENTS.md",
        ROOT / ".opencode" / "agents",
        ROOT / ".opencode" / "skills",
        ROOT / ".opencode" / "skills" / "repo-bootstrap" / "SKILL.md",
    ]

    for path in required_paths:
        if not path.exists():
            errors.append(f"missing required path: {path.relative_to(ROOT)}")

    legacy_config_path = ROOT / "opencode.json"
    if legacy_config_path.exists() or legacy_config_path.is_symlink():
        errors.append("legacy root opencode.json must not exist")

    config_path = CONFIG_PATH
    if config_path.is_symlink():
        errors.append(".opencode/opencode.json must be a regular file, not a symlink")

    if config_path.exists():
        try:
            config = load_config(config_path)
            if config.get("model") != "ollama/gemma4:e2b":
                errors.append("model must be ollama/gemma4:e2b")
            if config.get("default_agent") != "general":
                errors.append("default_agent must be general")
            agents = config.get("agent", {})
            for required_agent in [
                "general",
                "standard",
                "auto",
                "standard-executor",
                "auto-executor",
                "explore",
            ]:
                if required_agent not in agents:
                    errors.append(f"missing required agent: {required_agent}")
            stale_agents = [
                "planner",
                "standard-implementer",
                "auto-implementer",
                "standard-operations",
                "auto-operations",
                "standard-docs-writer",
                "auto-docs-writer",
            ] + [
                f"{lane}-{suffix}"
                for suffix in ["build", "plan", "devops"]
                for lane in ("standard", "auto")
            ]
            for stale_agent in stale_agents:
                if stale_agent in agents:
                    errors.append(f"stale agent must be removed: {stale_agent}")
            disallowed_model_marker = "q" + "wen"
            if disallowed_model_marker in json.dumps(config).lower():
                errors.append("config must not contain disallowed model references")
            for primary_agent in PRIMARY_AGENTS:
                agent_config = agents.get(primary_agent, {})
                permission = agent_config.get("permission", {})
                tools = agent_config.get("tools", {})
                if permission.get("edit") != "deny":
                    errors.append(f"{primary_agent} must deny direct edit permission")
                if not isinstance(permission.get("bash"), dict):
                    errors.append(f"{primary_agent} must use a bash permission map")
                for tool_name in ["write", "edit", "webfetch"]:
                    if tools.get(tool_name) is not False:
                        errors.append(f"{primary_agent} tool must be disabled: {tool_name}")
                if tools.get("bash") is not True:
                    errors.append(f"{primary_agent} bash tool must be enabled for read-only commands")
            general_tasks = agents.get("general", {}).get("permission", {}).get("task", {})
            for writable_agent in [
                "standard-executor",
                "auto-executor",
            ]:
                if general_tasks.get(writable_agent) == "allow":
                    errors.append(f"general must not delegate writable work to: {writable_agent}")
            for agent_name in READ_ONLY_BASH_AGENTS + [
                name for name in OPTIONAL_MANUAL_SPECIALISTS if name in agents
            ]:
                agent_config = agents.get(agent_name, {})
                tools = agent_config.get("tools", {})
                bash = bash_permission(agent_config)
                if tools.get("bash") is not True:
                    errors.append(f"{agent_name} bash tool must be enabled")
                if bash.get("*") != "ask":
                    errors.append(f"{agent_name} bash fallback must be ask")
                for pattern in REQUIRED_ASK_GUARDS:
                    if bash.get(pattern) != "ask":
                        errors.append(f"{agent_name} must ask-gate bash pattern: {pattern}")
                for pattern in REQUIRED_READ_ONLY_PATTERNS:
                    if bash.get(pattern) != "allow":
                        errors.append(f"{agent_name} must allow read-only bash pattern: {pattern}")
                output_guard_index = key_index(bash, "*--output*")
                for pattern in ["git diff*", "git log*", "git show*"]:
                    allow_index = key_index(bash, pattern)
                    if (
                        output_guard_index is not None
                        and allow_index is not None
                        and output_guard_index > allow_index
                    ):
                        errors.append(
                            f"{agent_name} must ask-gate *--output* before allowing {pattern}"
                        )
                pre_guard_index = key_index(bash, "*--pre*")
                rg_allow_index = key_index(bash, "rg *")
                if (
                    pre_guard_index is not None
                    and rg_allow_index is not None
                    and pre_guard_index > rg_allow_index
                ):
                    errors.append(f"{agent_name} must ask-gate *--pre* before allowing rg *")
                ext_diff_guard_index = key_index(bash, "*--ext-diff*")
                for pattern in ["git diff*", "git log*", "git show*"]:
                    allow_index = key_index(bash, pattern)
                    if (
                        ext_diff_guard_index is not None
                        and allow_index is not None
                        and ext_diff_guard_index > allow_index
                    ):
                        errors.append(
                            f"{agent_name} must ask-gate *--ext-diff* before allowing {pattern}"
                        )
                git_grep_allow_index = key_index(bash, "git grep*")
                for pattern in [
                    "git grep -O*",
                    "git grep --open-files-in-pager*",
                    "git grep* -O*",
                    "git grep* --open-files-in-pager*",
                ]:
                    guard_index = key_index(bash, pattern)
                    if (
                        guard_index is not None
                        and git_grep_allow_index is not None
                        and guard_index > git_grep_allow_index
                    ):
                        errors.append(
                            f"{agent_name} must ask-gate {pattern} before allowing git grep*"
                        )
                process_guard_index = key_index(bash, "*<(*")
                for pattern in REQUIRED_READ_ONLY_PATTERNS:
                    allow_index = key_index(bash, pattern)
                    if (
                        process_guard_index is not None
                        and allow_index is not None
                        and process_guard_index > allow_index
                    ):
                        errors.append(
                            f"{agent_name} must ask-gate *<(* before allowing {pattern}"
                        )
                for pattern in UNSAFE_READ_ONLY_ALLOW_PATTERNS:
                    if bash.get(pattern) == "allow":
                        errors.append(
                            f"{agent_name} must not automatically allow mutation-capable pattern: {pattern}"
                        )
            for readonly_agent in [
                "general",
                "standard",
                "auto",
                "explore",
            ] + [name for name in OPTIONAL_MANUAL_SPECIALISTS if name in agents]:
                tools = agents.get(readonly_agent, {}).get("tools", {})
                for tool_name in ["write", "edit"]:
                    if tools.get(tool_name) is not False:
                        errors.append(f"{readonly_agent} tool must be disabled: {tool_name}")
                if agents.get(readonly_agent, {}).get("permission", {}).get("edit") != "deny":
                    errors.append(f"{readonly_agent} must deny direct edit permission")
            for specialist in OPTIONAL_MANUAL_SPECIALISTS:
                if specialist in agents:
                    task_permissions = agents[specialist].get("permission", {}).get("task", {})
                    if task_permissions.get("*") != "deny":
                        errors.append(f"{specialist} must deny task delegation")
            standard_tasks = agents.get("standard", {}).get("permission", {}).get("task", {})
            if standard_tasks.get("standard-executor") != "allow":
                errors.append("standard must be allowed to delegate to standard-executor")
            for old_task in ["planner", "standard-implementer", "standard-operations", "auto-operations", "standard-docs-writer", "code-reviewer", "security-auditor", "performance-analyzer"]:
                if standard_tasks.get(old_task) == "allow":
                    errors.append(f"standard must not delegate default workflow task: {old_task}")
            auto_tasks = agents.get("auto", {}).get("permission", {}).get("task", {})
            if auto_tasks.get("auto-executor") != "allow":
                errors.append("auto must be allowed to delegate to auto-executor")
            for old_task in ["planner", "auto-implementer", "standard-operations", "auto-operations", "auto-docs-writer", "code-reviewer", "security-auditor", "performance-analyzer"]:
                if auto_tasks.get(old_task) == "allow":
                    errors.append(f"auto must not delegate default workflow task: {old_task}")
            auto_executor_bash = bash_permission(agents.get("auto-executor", {}))
            if auto_executor_bash.get("*") != "ask":
                errors.append("auto-executor bash fallback must be ask")
            for pattern in VALIDATION_BASH_PATTERNS:
                if auto_executor_bash.get(pattern) != "allow":
                    errors.append(f"auto-executor must allow validation pattern: {pattern}")
            validation_disallowed_agents = [
                "general",
                "standard",
                "auto",
                "explore",
                "standard-executor",
            ]
            for agent_name in validation_disallowed_agents:
                bash = bash_permission(agents.get(agent_name, {}))
                for pattern in VALIDATION_BASH_PATTERNS:
                    if bash.get(pattern) == "allow":
                        errors.append(
                            f"{agent_name} must not automatically allow validation pattern: {pattern}"
                        )
            prompt_paths = extract_prompt_paths(config.get("agent", {}))
            for prompt_path in sorted(set(prompt_paths)):
                if not prompt_path.startswith("agents/"):
                    errors.append(f"prompt path must start with agents/: {prompt_path}")
                if prompt_path.startswith(".opencode/") or prompt_path.startswith("/"):
                    errors.append(f"prompt path must be relative to .opencode: {prompt_path}")
                full_path = config_path.parent / prompt_path
                if not full_path.exists():
                    errors.append(
                        f"prompt file not found: {prompt_path} (from .opencode/opencode.json)"
                    )
        except RuntimeError as exc:
            errors.append(str(exc))

    if errors:
        print("OpenCode setup check failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OpenCode setup check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
