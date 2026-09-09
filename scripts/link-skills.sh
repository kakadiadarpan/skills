#!/usr/bin/env bash
set -euo pipefail

# Maintainer convenience: make installed skill directories point back to this
# checkout. This avoids copying the skill while it is being edited.

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source="$repo/skills/engineering/pr-review"

if [[ ! -f "$source/SKILL.md" ]]; then
  echo "error: expected skill at $source" >&2
  exit 1
fi

for destination in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
  mkdir -p "$destination"
  target="$destination/pr-review"

  if [[ -e "$target" && ! -L "$target" ]]; then
    echo "error: refusing to replace existing directory: $target" >&2
    echo "Move it aside or remove it yourself, then run this script again." >&2
    exit 1
  fi

  ln -sfn "$source" "$target"
  echo "linked $target -> $source"
done
