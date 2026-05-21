#!/usr/bin/env python3
"""Verify a folder-workflow workspace in any project directory."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


STANDARD_REQUIRED_PATHS = [
    "AGENTS.md",
    "_workspace/README.md",
    "_workspace/map/workspace-map.md",
    "_workspace/map/routing-table.md",
    "_workspace/map/naming-conventions.md",
    "_workspace/map/safety-rules.md",
    "_workspace/outputs/README.md",
]

PIPELINE_REQUIRED_PATHS = [
    "CONTEXT.md",
    "README.md",
    "input/README.md",
    "_config/README.md",
    "shared/README.md",
    "stages/00_intake/CONTEXT.md",
    "stages/00_intake/references/README.md",
    "stages/00_intake/output/README.md",
    "stages/01_process/CONTEXT.md",
    "stages/01_process/references/README.md",
    "stages/01_process/output/README.md",
    "stages/02_finalize/CONTEXT.md",
    "stages/02_finalize/references/README.md",
    "stages/02_finalize/output/README.md",
]

OLD_LAYOUT_DIRS = [
    "00-map",
    "10-workflows",
    "20-runbooks",
    "30-context",
    "40-outputs",
    "_map",
    "_workflows",
    "_runbooks",
    "_context",
    "_outputs",
]


def referenced_workspace_paths(routing_table: Path) -> list[str]:
    text = routing_table.read_text()
    # Capture backticked _workspace paths from the routing table.
    return sorted(set(re.findall(r"`(_workspace/[^`]+)`", text)))


def pipeline_stage_contexts(root: Path) -> list[Path]:
    stages_dir = root / "stages"
    if not stages_dir.exists():
        return []
    return sorted(stages_dir.glob("*/CONTEXT.md"))


def verify_pipeline_contracts(root: Path) -> list[str]:
    errors: list[str] = []
    contexts = pipeline_stage_contexts(root)
    if not contexts:
        errors.append("pipeline workspace must include at least one stages/*/CONTEXT.md")
        return errors
    for context in contexts:
        text = context.read_text()
        for heading in ["## Inputs", "## Process", "## Outputs", "## Review gate"]:
            if heading not in text:
                errors.append(f"pipeline stage missing {heading}: {context.relative_to(root)}")
        stage_dir = context.parent
        for child in ["references", "output"]:
            if not (stage_dir / child).is_dir():
                errors.append(f"pipeline stage missing {child}/: {stage_dir.relative_to(root)}")
    return errors


def verify_skills(root: Path) -> list[str]:
    errors: list[str] = []
    skills_dir = root / ".opencode" / "skills"
    if not skills_dir.exists():
        return errors
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"missing skill file: {skill_file.relative_to(root)}")
            continue
        text = skill_file.read_text()
        if "name:" not in text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else True:
            errors.append(f"skill frontmatter missing name: {skill_file.relative_to(root)}")
        if "description:" not in text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else True:
            errors.append(f"skill frontmatter missing description: {skill_file.relative_to(root)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", nargs="?", default=".", help="Workspace root to verify.")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        print(f"Target is not a directory: {root}", file=sys.stderr)
        return 1

    is_pipeline = (root / "CONTEXT.md").exists() and (root / "stages").is_dir()
    required_paths = PIPELINE_REQUIRED_PATHS if is_pipeline else STANDARD_REQUIRED_PATHS

    for relative in required_paths:
        if not (root / relative).exists():
            errors.append(f"missing required path: {relative}")

    if is_pipeline:
        errors.extend(verify_pipeline_contracts(root))
    else:
        routing_table = root / "_workspace" / "map" / "routing-table.md"
        if routing_table.exists():
            for relative in referenced_workspace_paths(routing_table):
                if not (root / relative).exists():
                    errors.append(f"routing table references missing path: {relative}")

    for relative in OLD_LAYOUT_DIRS:
        path = root / relative
        if path.exists():
            try:
                has_entries = any(path.iterdir()) if path.is_dir() else True
            except OSError:
                has_entries = True
            if has_entries:
                warnings.append(f"old layout path still exists: {relative}")

    errors.extend(verify_skills(root))

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if errors:
        print("Workspace verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Workspace verification passed: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
