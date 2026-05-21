#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage: ./setup.sh [--dry-run] [--help]

Symlink this repository's selected .opencode entries into the global OpenCode
config directory. The destination defaults to ~/.config/opencode and can be
overridden with OPENCODE_CONFIG_DIR.

Options:
  --dry-run  Show planned changes without modifying files or running checks
  --help     Show this help
EOF
}

DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --dry-run)
      DRY_RUN=1
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      usage >&2
      exit 2
      ;;
  esac
done

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
REPO_ROOT="$SCRIPT_DIR"
SOURCE="$REPO_ROOT/.opencode"
GLOBAL_AGENTS_SOURCE="$REPO_ROOT/.opencode/AGENTS.md"
DEST="${OPENCODE_CONFIG_DIR:-$HOME/.config/opencode}"
DEST_PARENT="$(dirname -- "$DEST")"
TIMESTAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP_DIR="$DEST/backups/$TIMESTAMP"
DEST_BACKUP="$DEST.backup-$TIMESTAMP"

REQUIRED_ENTRIES=(
  "opencode.json"
  "agents"
  "skills"
  "config"
  "scripts"
)

log() {
  printf '%s\n' "$*"
}

run() {
  if [ "$DRY_RUN" -eq 1 ]; then
    log "DRY-RUN: $*"
  else
    "$@"
  fi
}

resolve_path() {
  python3 -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).resolve())' "$1"
}

is_correct_symlink() {
  local link_path="$1"
  local source_path="$2"

  [ -L "$link_path" ] || return 1
  [ "$(resolve_path "$link_path")" = "$(resolve_path "$source_path")" ]
}

backup_dest_if_needed() {
  if [ -e "$DEST" ] || [ -L "$DEST" ]; then
    if [ -d "$DEST" ]; then
      return 0
    fi

    local backup_path="$DEST_BACKUP"
    if [ -e "$backup_path" ] || [ -L "$backup_path" ]; then
      backup_path="$DEST_BACKUP-$$"
    fi

    log "Backing up existing non-directory config path: $DEST -> $backup_path"
    run mv "$DEST" "$backup_path"
  fi
}

backup_entry() {
  local entry_path="$1"
  local entry_name="$2"

  run mkdir -p "$BACKUP_DIR"
  log "Backing up conflict: $entry_path -> $BACKUP_DIR/$entry_name"
  run mv "$entry_path" "$BACKUP_DIR/$entry_name"
}

link_entry() {
  local entry_name="$1"
  local source_path="$SOURCE/$entry_name"
  local dest_path="$DEST/$entry_name"

  if [ ! -e "$source_path" ]; then
    echo "Required source entry is missing: $source_path" >&2
    exit 1
  fi

  if is_correct_symlink "$dest_path" "$source_path"; then
    log "Already linked: $dest_path -> $source_path"
    return 0
  fi

  if [ -e "$dest_path" ] || [ -L "$dest_path" ]; then
    backup_entry "$dest_path" "$entry_name"
  fi

  log "Linking: $dest_path -> $source_path"
  run ln -s "$source_path" "$dest_path"
}

if [ ! -d "$SOURCE" ]; then
  echo "Missing source directory: $SOURCE" >&2
  exit 1
fi

log "Repository root: $REPO_ROOT"
log "OpenCode source: $SOURCE"
log "OpenCode destination: $DEST"

if [ "$DRY_RUN" -eq 1 ]; then
  log "Dry run only; no files will be changed and checks will not run."
fi

if [ "$DRY_RUN" -eq 1 ]; then
  log "DRY-RUN: python3 .opencode/scripts/build-config.py"
else
  (cd "$REPO_ROOT" && python3 .opencode/scripts/build-config.py)
fi

run mkdir -p "$DEST_PARENT"
backup_dest_if_needed
run mkdir -p "$DEST"

for entry in "${REQUIRED_ENTRIES[@]}"; do
  link_entry "$entry"
done

if [ -f "$GLOBAL_AGENTS_SOURCE" ]; then
  if is_correct_symlink "$DEST/AGENTS.md" "$GLOBAL_AGENTS_SOURCE"; then
    log "Already linked: $DEST/AGENTS.md -> $GLOBAL_AGENTS_SOURCE"
  else
    if [ -e "$DEST/AGENTS.md" ] || [ -L "$DEST/AGENTS.md" ]; then
      backup_entry "$DEST/AGENTS.md" "AGENTS.md"
    fi
    log "Linking: $DEST/AGENTS.md -> $GLOBAL_AGENTS_SOURCE"
    run ln -s "$GLOBAL_AGENTS_SOURCE" "$DEST/AGENTS.md"
  fi
else
  log "Global AGENTS source not found; skipping: $GLOBAL_AGENTS_SOURCE"
fi

if [ -f "$REPO_ROOT/verify-opencode-setup.py" ]; then
  if [ "$DRY_RUN" -eq 1 ]; then
    log "DRY-RUN: python3 verify-opencode-setup.py"
  else
    (cd "$REPO_ROOT" && python3 verify-opencode-setup.py)
  fi
else
  log "Verifier not found; skipping: $REPO_ROOT/verify-opencode-setup.py"
fi

cat <<EOF

OpenCode global config mapping complete.

Next steps:
  1. Restart OpenCode so it reloads global config.
  2. Test that a simple command such as 'git status' runs without an unexpected prompt.
  3. Edit permissions under .opencode/config/permissions/ when needed.
  4. Regenerate config after permission edits:
     cd "$REPO_ROOT" && python3 .opencode/scripts/build-config.py
  5. Global OpenCode instructions are linked from .opencode/AGENTS.md.
EOF
