#!/usr/bin/env bash
set -euo pipefail

# Maintainer convenience: make installed skill directories point back to this
# checkout. This avoids copying a skill while it is being edited.

repo="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

shopt -s nullglob
skill_files=("$repo"/skills/*/*/SKILL.md)
if [[ ${#skill_files[@]} -eq 0 ]]; then
  echo "error: no skills found under $repo/skills" >&2
  exit 1
fi

for skill_file in "${skill_files[@]}"; do
  source="$(dirname "$skill_file")"
  name="$(basename "$source")"

  for destination in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
    mkdir -p "$destination"
    target="$destination/$name"

    if [[ -e "$target" && ! -L "$target" ]]; then
      echo "skip $target: existing directory, move it aside to link" >&2
      continue
    fi

    ln -sfn "$source" "$target"
    echo "linked $target -> $source"
  done
done
