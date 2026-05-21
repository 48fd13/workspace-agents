#!/usr/bin/env python3
"""Initialize a folder-workflow workspace from a template.

Interactive mode (no arguments): prompts for target directory and template,
then copies the chosen workspace template and a local copy of the pipeline
template into _workspace/pipelines/pipeline-template/.

Non-interactive mode: pass target and --template to skip prompts.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


KIT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = KIT_ROOT / "templates"
AVAILABLE_TEMPLATES = ["minimal", "development", "personal"]

TEMPLATE_DESCRIPTIONS = {
    "minimal":     "lightweight folder — notes, small projects, simple routing",
    "development": "engineering/code/cloud repo — full dev workflows, runbooks, pipelines",
    "personal":    "personal notes, learning, writing — vault-style workflows",
}


def copy_tree(src: Path, dst: Path, overwrite: bool) -> list[str]:
    written: list[str] = []
    for source in sorted(src.rglob("*")):
        relative = source.relative_to(src)
        destination = dst / relative
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() and not overwrite:
            continue
        shutil.copy2(source, destination)
        written.append(str(relative))
    return written


def prompt_target() -> Path:
    print("\nWhere should the workspace be created?")
    print("Enter a path to an existing directory (absolute or relative to current dir).")
    raw = input("Target directory: ").strip()
    if not raw:
        print("No path entered. Aborting.", file=sys.stderr)
        sys.exit(1)
    path = Path(raw).expanduser().resolve()
    if not path.exists():
        print(f"Directory does not exist: {path}", file=sys.stderr)
        sys.exit(1)
    if not path.is_dir():
        print(f"Not a directory: {path}", file=sys.stderr)
        sys.exit(1)
    return path


def prompt_template() -> str:
    print("\nChoose a workspace template:")
    for i, name in enumerate(AVAILABLE_TEMPLATES, 1):
        print(f"  {i}. {name} — {TEMPLATE_DESCRIPTIONS[name]}")
    raw = input("Template [1/2/3] or name: ").strip()
    if raw.isdigit():
        idx = int(raw) - 1
        if 0 <= idx < len(AVAILABLE_TEMPLATES):
            return AVAILABLE_TEMPLATES[idx]
        print(f"Invalid selection: {raw}", file=sys.stderr)
        sys.exit(1)
    if raw in AVAILABLE_TEMPLATES:
        return raw
    print(f"Unknown template: {raw}. Choose from: {', '.join(AVAILABLE_TEMPLATES)}", file=sys.stderr)
    sys.exit(1)


def prompt_overwrite() -> bool:
    raw = input("\nOverwrite existing files? [y/N]: ").strip().lower()
    return raw in ("y", "yes")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "target",
        nargs="?",
        help="Directory to initialize. Omit to use interactive mode.",
    )
    parser.add_argument(
        "--template",
        choices=AVAILABLE_TEMPLATES,
        help="Template to apply. Omit to choose interactively.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files.",
    )
    args = parser.parse_args()

    interactive = args.target is None and args.template is None

    if interactive:
        print("=" * 60)
        print("  Workspace Initializer")
        print("  workflow-kit/scripts/init-workspace.py")
        print("=" * 60)
        target_dir = prompt_target()
        template = prompt_template()
        overwrite = prompt_overwrite()
    else:
        if args.target is None:
            print("Error: target directory required in non-interactive mode.", file=sys.stderr)
            return 1
        target_dir = Path(args.target).expanduser().resolve()
        template = args.template or "minimal"
        overwrite = args.overwrite
        if not target_dir.exists() or not target_dir.is_dir():
            print(f"Target directory does not exist: {target_dir}", file=sys.stderr)
            return 1

    template_dir = TEMPLATES_DIR / template
    if not template_dir.is_dir():
        print(f"Template not found: {template_dir}", file=sys.stderr)
        return 1

    print(f"\nInitializing '{template}' workspace in: {target_dir}")

    # Copy workspace template
    written = copy_tree(template_dir, target_dir, overwrite)

    # Copy pipeline template into _workspace/pipelines/pipeline-template/
    pipeline_src = TEMPLATES_DIR / "pipeline"
    pipeline_dst = target_dir / "_workspace" / "pipelines" / "pipeline-template"
    pipeline_written = []
    if pipeline_src.is_dir():
        pipeline_written = copy_tree(pipeline_src, pipeline_dst, overwrite)
        if pipeline_written:
            written += [f"_workspace/pipelines/pipeline-template/{f}" for f in pipeline_written]

    if written:
        print("\nFiles written:")
        for path in written:
            print(f"  + {path}")
    else:
        print("\nNo files written — existing files were preserved (use --overwrite to force).")

    print(f"\nDone. Workspace '{template}' initialized at:")
    print(f"  {target_dir}")

    print("\nNext steps:")
    print(f"  1. Review AGENTS.md — set the project role and safety gates.")
    print(f"  2. Edit _workspace/map/workspace-map.md — describe your project folders.")
    print(f"  3. Edit _workspace/map/routing-table.md — map tasks to workflows.")
    if template == "development":
        print(f"  4. Browse _workspace/workflows/ — pre-built dev workflows are ready to use.")
        print(f"  5. Create a pipeline: copy _workspace/pipelines/pipeline-template/ into")
        print(f"     _workspace/pipelines/<your-pipeline-name>/ and customize stage contracts.")
    else:
        print(f"  4. Create a pipeline: copy _workspace/pipelines/pipeline-template/ into")
        print(f"     _workspace/pipelines/<your-pipeline-name>/ and customize stage contracts.")
    print(f"\n  Verify: python3 {Path(__file__).resolve()} --verify {target_dir}")
    print(f"  (or run: python3 workflow-kit/scripts/verify-workspace.py {target_dir})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
