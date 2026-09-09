#!/usr/bin/env python3
"""Package one skill directory as a portable .skill ZIP archive."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


EXCLUDED_DIRECTORY_NAMES = {"evals", "__pycache__", "node_modules"}
EXCLUDED_FILE_NAMES = {".DS_Store"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def should_include(path: Path, skill_dir: Path) -> bool:
    relative_path = path.relative_to(skill_dir)
    return not (
        any(part in EXCLUDED_DIRECTORY_NAMES for part in relative_path.parts[:-1])
        or path.name in EXCLUDED_FILE_NAMES
        or path.suffix in EXCLUDED_SUFFIXES
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", type=Path, help="directory containing SKILL.md")
    parser.add_argument("output_dir", type=Path, nargs="?", default=Path("dist"))
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        print(f"error: SKILL.md not found in {skill_dir}", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_file = args.output_dir.resolve() / f"{skill_dir.name}.skill"

    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if path.is_file() and should_include(path, skill_dir):
                archive.write(path, path.relative_to(skill_dir.parent))

    print(output_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
