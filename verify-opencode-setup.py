#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / ".opencode" / "opencode.json"

BASH_PROFILE_AGENTS = [
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

PLANNING_ONLY_PRIMARY_AGENTS = ["standard", "auto"]

WEBFETCH_ENABLED_AGENTS = ["general", "standard", "auto", "explore"]

WEBFETCH_DISABLED_AGENTS = ["standard-executor", "auto-executor"]

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
    "git status --*",
    "git diff",
    "git diff *",
    "git diff*",
    "git diff --*",
    "git diff -- *",
    "git diff --stat*",
    "git diff --check*",
    "git diff --cached*",
    "git diff --staged*",
    "git diff --name-only*",
    "git diff --name-status*",
    "git diff --compact-summary*",
    "git log",
    "git log *",
    "git log*",
    "git log --*",
    "git show",
    "git show *",
    "git show*",
    "git show --*",
    "git branch",
    "git branch *",
    "git branch*",
    "git branch --show-current",
    "git ls-files*",
    "git grep*",
    "git rev-parse *",
    "git rev-parse*",
    "git remote -v*",
]

REQUIRED_VERSION_PATTERNS = [
    "node --version",
    "npm --version",
    "python --version",
    "python3 --version",
    "go version",
    "rustc --version",
    "cargo --version",
    "docker --version",
    "kubectl version --client*",
]

REQUIRED_SAFE_COMPOUND_PATTERNS = [
    "git status* && git diff*",
    "git status* && git diff --stat*",
    "git status* && git log*",
    "pwd && ls*",
    "pwd; ls*",
    "git status*; git diff*",
]

UNSAFE_READ_ONLY_ALLOW_PATTERNS = ["find . *", "sed -n *"]
REQUIRED_SHELL_ASK_GUARDS = [
    "*>*",
    "*>>*",
    "*|*",
    "*&&*",
    "*;*",
    "*`*",
    "*$(*",
    "* xargs *",
    "tee *",
    "*--output*",
    "*--pre*",
    "*--ext-diff*",
    "*<(*",
]

REQUIRED_UNSAFE_GIT_ASK_PATTERNS = [
    "git diff --ext-diff*",
    "git grep -O*",
    "git grep --open-files-in-pager*",
    "git grep* -O*",
    "git grep* --open-files-in-pager*",
]

REQUIRED_DANGEROUS_GIT_DENY_PATTERNS = [
    "git push --force*",
    "git reset --hard*",
    "git clean*",
    "git branch -D *",
    "git branch -D*",
]

REQUIRED_DESTRUCTIVE_DENY_PATTERNS = [
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
]

REQUIRED_MUTATING_GIT_ASK_PATTERNS = [
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
]

REQUIRED_INSTALL_NETWORK_INFRA_ASK_PATTERNS = [
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
]

REQUIRED_FILE_MUTATION_ASK_PATTERNS = [
    "mkdir *",
    "touch *",
    "mv *",
    "cp *",
    "chmod *",
    "chown *",
]

BROAD_SHELL_ASK_GUARDS = REQUIRED_SHELL_ASK_GUARDS

COMPOUND_ASK_GUARDS = ["*&&*", "*;*"]

DISALLOWED_BLANKET_ALLOW_PATTERNS = [
    "*",
    "git *",
    "docker *",
    "npm *",
    "sudo *",
    "*&&*",
    "*;*",
    "*|*",
    "*>*",
    "*>>*",
    "*`*",
    "*$(*",
    "* xargs *",
    "tee *",
    "*--output*",
    "*--pre*",
    "*--ext-diff*",
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
            general_config = agents.get("general", {})
            general_permission = general_config.get("permission", {})
            general_tools = general_config.get("tools", {})
            if general_config.get("mode") != "primary":
                errors.append("general must be a primary agent")
            if general_permission.get("edit") != "allow":
                errors.append("general must allow direct edit permission")
            if not isinstance(general_permission.get("bash"), dict):
                errors.append("general must use a bash permission map")
            for tool_name in ["write", "edit", "bash", "read", "grep", "glob"]:
                if general_tools.get(tool_name) is not True:
                    errors.append(f"general tool must be enabled: {tool_name}")
            if general_tools.get("webfetch") is not True:
                errors.append("general tool must be enabled: webfetch")
            general_bash = bash_permission(general_config)
            for pattern in VALIDATION_BASH_PATTERNS:
                if general_bash.get(pattern) != "allow":
                    errors.append(f"general must allow validation pattern: {pattern}")
            general_tasks = general_permission.get("task", {})
            if general_tasks.get("*") != "deny":
                errors.append("general must deny task delegation by default")
            if general_tasks.get("explore") != "allow":
                errors.append("general may delegate only read-only exploration to explore")
            for delegated_agent, value in general_tasks.items():
                if delegated_agent not in ["*", "explore"] and value == "allow":
                    errors.append(f"general must not delegate writable/default workflow work to: {delegated_agent}")

            for primary_agent in PLANNING_ONLY_PRIMARY_AGENTS:
                agent_config = agents.get(primary_agent, {})
                permission = agent_config.get("permission", {})
                tools = agent_config.get("tools", {})
                if permission.get("edit") != "deny":
                    errors.append(f"{primary_agent} must deny direct edit permission")
                if not isinstance(permission.get("bash"), dict):
                    errors.append(f"{primary_agent} must use a bash permission map")
                for tool_name in ["write", "edit"]:
                    if tools.get(tool_name) is not False:
                        errors.append(f"{primary_agent} tool must be disabled: {tool_name}")
                if tools.get("bash") is not True:
                    errors.append(f"{primary_agent} bash tool must be enabled for read-only commands")
            for agent_name in WEBFETCH_ENABLED_AGENTS:
                tools = agents.get(agent_name, {}).get("tools", {})
                if tools.get("webfetch") is not True:
                    errors.append(f"{agent_name} tool must be enabled: webfetch")
            for agent_name in WEBFETCH_DISABLED_AGENTS:
                tools = agents.get(agent_name, {}).get("tools", {})
                if tools.get("webfetch") is not False:
                    errors.append(f"{agent_name} tool must be disabled: webfetch")
            bash_targets = [("global/default", config.get("permission", {}).get("bash", {}))]
            bash_targets.extend(
                (agent_name, bash_permission(agents.get(agent_name, {})))
                for agent_name in BASH_PROFILE_AGENTS
            )
            bash_targets.extend(
                (agent_name, bash_permission(agents.get(agent_name, {})))
                for agent_name in OPTIONAL_MANUAL_SPECIALISTS
                if agent_name in agents
            )
            for agent_name, bash in bash_targets:
                agent_config = agents.get(agent_name, {})
                tools = agent_config.get("tools", {})
                if agent_name != "global/default" and tools.get("bash") is not True:
                    errors.append(f"{agent_name} bash tool must be enabled")
                if bash.get("*") != "ask":
                    errors.append(f"{agent_name} bash fallback must be ask")
                fallback_index = key_index(bash, "*")
                if fallback_index is None:
                    errors.append(f"{agent_name} bash fallback must be present")
                elif fallback_index != 0:
                    errors.append(f"{agent_name} bash fallback ask must be the first rule")
                for pattern in DISALLOWED_BLANKET_ALLOW_PATTERNS:
                    if bash.get(pattern) == "allow":
                        errors.append(f"{agent_name} must not broadly allow bash pattern: {pattern}")
                for pattern in REQUIRED_SHELL_ASK_GUARDS:
                    if bash.get(pattern) != "ask":
                        errors.append(f"{agent_name} must ask-gate bash pattern: {pattern}")
                for pattern in REQUIRED_INSTALL_NETWORK_INFRA_ASK_PATTERNS:
                    if bash.get(pattern) != "ask":
                        errors.append(f"{agent_name} must ask-gate install/network/infra pattern: {pattern}")
                for pattern in REQUIRED_FILE_MUTATION_ASK_PATTERNS:
                    if bash.get(pattern) != "ask":
                        errors.append(f"{agent_name} must ask-gate file mutation pattern: {pattern}")
                for pattern in REQUIRED_UNSAFE_GIT_ASK_PATTERNS:
                    if bash.get(pattern) != "ask":
                        errors.append(f"{agent_name} must ask-gate unsafe git pattern: {pattern}")
                for pattern in REQUIRED_DANGEROUS_GIT_DENY_PATTERNS:
                    if bash.get(pattern) != "deny":
                        errors.append(f"{agent_name} must deny dangerous git pattern: {pattern}")
                for pattern in REQUIRED_DESTRUCTIVE_DENY_PATTERNS:
                    if bash.get(pattern) != "deny":
                        errors.append(f"{agent_name} must deny destructive pattern: {pattern}")
                for pattern in REQUIRED_MUTATING_GIT_ASK_PATTERNS:
                    if bash.get(pattern) != "ask":
                        errors.append(f"{agent_name} must ask-gate mutating git pattern: {pattern}")
                for pattern in REQUIRED_READ_ONLY_PATTERNS:
                    if bash.get(pattern) != "allow":
                        errors.append(f"{agent_name} must allow read-only bash pattern: {pattern}")
                    allow_index = key_index(bash, pattern)
                    if (
                        fallback_index is not None
                        and allow_index is not None
                        and fallback_index > allow_index
                    ):
                        errors.append(
                            f"{agent_name} must place fallback ask before read-only allow: {pattern}"
                        )
                for pattern in REQUIRED_VERSION_PATTERNS:
                    if bash.get(pattern) != "allow":
                        errors.append(f"{agent_name} must allow harmless version pattern: {pattern}")
                    allow_index = key_index(bash, pattern)
                    if (
                        fallback_index is not None
                        and allow_index is not None
                        and fallback_index > allow_index
                    ):
                        errors.append(
                            f"{agent_name} must place fallback ask before version allow: {pattern}"
                        )
                for pattern in REQUIRED_SAFE_COMPOUND_PATTERNS:
                    if bash.get(pattern) != "allow":
                        errors.append(
                            f"{agent_name} must allow safe compound bash pattern: {pattern}"
                        )
                    allow_index = key_index(bash, pattern)
                    if (
                        fallback_index is not None
                        and allow_index is not None
                        and fallback_index > allow_index
                    ):
                        errors.append(
                            f"{agent_name} must place fallback ask before safe compound allow: {pattern}"
                        )
                for guard in BROAD_SHELL_ASK_GUARDS:
                    guard_index = key_index(bash, guard)
                    guarded_allow_patterns = [
                        pattern for pattern in REQUIRED_READ_ONLY_PATTERNS if pattern.startswith("git ")
                    ]
                    for pattern in guarded_allow_patterns:
                        allow_index = key_index(bash, pattern)
                        if (
                            guard_index is not None
                            and allow_index is not None
                            and guard_index < allow_index
                        ):
                            errors.append(
                                f"{agent_name} must place read-only allow {pattern} before broad shell guard {guard}"
                            )
                unsafe_order_pairs = [
                    ("git push --force*", "git push*"),
                    ("git branch -D *", "git branch*"),
                    ("git branch -D*", "git branch*"),
                    ("git diff --ext-diff*", "git diff*"),
                    ("git diff --ext-diff*", "git diff --*"),
                    ("git grep -O*", "git grep*"),
                    ("git grep --open-files-in-pager*", "git grep*"),
                    ("git grep* -O*", "git grep*"),
                    ("git grep* --open-files-in-pager*", "git grep*"),
                ]
                for unsafe_pattern, broad_pattern in unsafe_order_pairs:
                    unsafe_index = key_index(bash, unsafe_pattern)
                    broad_index = key_index(bash, broad_pattern)
                    if (
                        unsafe_index is not None
                        and broad_index is not None
                        and unsafe_index < broad_index
                    ):
                        errors.append(
                            f"{agent_name} must place {unsafe_pattern} after broad git allow {broad_pattern}"
                        )
                for guard in COMPOUND_ASK_GUARDS:
                    guard_index = key_index(bash, guard)
                    for pattern in REQUIRED_SAFE_COMPOUND_PATTERNS:
                        allow_index = key_index(bash, pattern)
                        if (
                            guard_index is not None
                            and allow_index is not None
                            and guard_index > allow_index
                        ):
                            errors.append(
                                f"{agent_name} must place broad compound guard {guard} before explicit safe compound {pattern}"
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
                        and guard_index < git_grep_allow_index
                    ):
                        errors.append(
                            f"{agent_name} must ask-gate {pattern} after allowing git grep*"
                        )
                for pattern in UNSAFE_READ_ONLY_ALLOW_PATTERNS:
                    if bash.get(pattern) == "allow":
                        errors.append(
                            f"{agent_name} must not automatically allow mutation-capable pattern: {pattern}"
                        )
            for readonly_agent in [
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
            for executor_name in ["standard-executor", "auto-executor"]:
                executor_bash = bash_permission(agents.get(executor_name, {}))
                for pattern in VALIDATION_BASH_PATTERNS:
                    if executor_bash.get(pattern) != "allow":
                        errors.append(f"{executor_name} must allow validation pattern: {pattern}")
            validation_disallowed_agents = [
                "standard",
                "auto",
                "explore",
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
