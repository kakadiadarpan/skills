# Personal agent skills

Small, composable skills for coding agents.

## Install

Pick skills interactively:

```sh
npx skills@latest add kakadiadarpan/skills
```

Or install one by name:

```sh
npx skills@latest add kakadiadarpan/skills --skill <name>
```

The copied files are yours to customize. Run `npx skills@latest update` to pull in upstream changes.

## Available skills

| Skill | What it does | Works best with |
| --- | --- | --- |
| [`pr-review`](./skills/engineering/pr-review/SKILL.md) | Reviews pull requests with evidence before verdict. Posts to GitHub only with explicit approval. | [i-have-adhd](https://github.com/ayghri/i-have-adhd), [unslop](https://github.com/cursor/plugins), [show-me](https://github.com/humanlayer/skills) |

Install the companion skills a skill recommends with the same command, for example:

```sh
npx skills@latest add ayghri/i-have-adhd --skill i-have-adhd
npx skills@latest add cursor/plugins --skill unslop
npx skills@latest add humanlayer/skills --skill show-me
```

## Development

Each skill lives in `skills/<category>/<name>/`:

```text
skills/<category>/<name>/
├── SKILL.md          # required, YAML frontmatter with name and description
├── agents/           # optional, per-agent metadata
└── evals/evals.json  # optional, test prompts, excluded from packages
```

| Command | What it does |
| --- | --- |
| `python3 scripts/validate-skills.py` | Checks every `SKILL.md` |
| `python3 scripts/package-skill.py skills/<category>/<name>` | Writes `dist/<name>.skill` |
| `bash scripts/link-skills.sh` | Links every skill into `~/.claude/skills` and `~/.agents/skills` for local editing |

To add a skill, create its folder, add a row to the table above, and run the validator.
