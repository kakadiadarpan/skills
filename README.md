# Personal Agent Skills

Small, composable skills for coding agents.

## Install

Choose one installation method. Installing both would make the same skill
available twice.

### Any compatible agent

Use the skills installer to copy the skill into a project or supported agent
configuration:

```sh
npx skills@latest add kakadiadarpan/skills
```

Select **pr-review** when prompted. The copied files are yours to customize;
run `npx skills@latest update` when you want to pull in upstream changes.

`pr-review` works best with these three skills. Installing them is highly recommended:

```sh
npx skills@latest add ayghri/i-have-adhd --skill i-have-adhd
npx skills@latest add cursor/plugins --skill unslop
npx skills@latest add humanlayer/skills --skill show-me
```

## Available skills

| Skill | What it does |
| --- | --- |
| [`pr-review`](./skills/engineering/pr-review/SKILL.md) | Reviews pull requests with evidence before verdict; can publish precise review comments only when asked. |

## Development

Skills are under `skills/<category>/<skill-name>/`. Each skill has a required
`SKILL.md` with YAML frontmatter. Evaluation prompts live in that skill's
`evals/` directory and are excluded from distributed `.skill` packages.

Validate the skill:

```sh
python scripts/validate-skills.py
```

Package a standalone installable skill:

```sh
python scripts/package-skill.py skills/engineering/pr-review dist
```

The package is written to `dist/pr-review.skill`.
