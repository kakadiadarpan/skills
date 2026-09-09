#!/usr/bin/env python3
"""Validate the repository's Agent Skills-compatible SKILL.md files."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"\A---\n(?P<contents>.*?)\n---\n", re.DOTALL)


def parse_frontmatter(path: Path) -> dict[str, str]:
    content = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        raise ValueError("missing or malformed YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group("contents").splitlines():
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"unsupported frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def validate(path: Path) -> list[str]:
    try:
        fields = parse_frontmatter(path)
    except ValueError as error:
        return [str(error)]

    errors: list[str] = []
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append("missing required 'name'")
    elif not NAME_PATTERN.fullmatch(name):
        errors.append("'name' must be kebab-case")
    elif path.parent.name != name:
        errors.append(f"directory name {path.parent.name!r} must match skill name {name!r}")

    if not description:
        errors.append("missing required 'description'")
    elif len(description) > 1_024:
        errors.append("'description' must not exceed 1024 characters")

    return errors


def main() -> int:
    skill_files = sorted(SKILLS_ROOT.rglob("SKILL.md"))
    if not skill_files:
        print("No SKILL.md files found under skills/.", file=sys.stderr)
        return 1

    invalid = False
    for skill_file in skill_files:
        errors = validate(skill_file)
        relative_path = skill_file.relative_to(ROOT)
        if errors:
            invalid = True
            for error in errors:
                print(f"FAIL {relative_path}: {error}", file=sys.stderr)
        else:
            print(f"OK   {relative_path}")

    return 1 if invalid else 0


if __name__ == "__main__":
    raise SystemExit(main())
