#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / ".opencode" / "opencode.json"


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
            if config.get("default_agent") != "standard":
                errors.append("default_agent must be standard")
            agents = config.get("agent", {})
            for required_agent in ["standard", "auto"]:
                if required_agent not in agents:
                    errors.append(f"missing required agent: {required_agent}")
            if "qwen" in json.dumps(config).lower():
                errors.append("config must not contain qwen references")
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
