# Contributor notes

- Keep each installable skill under `skills/<category>/<name>/SKILL.md`.
- The folder name and frontmatter `name` must match and use kebab-case.
- Keep the `description` specific about when the skill should trigger.
- Put test prompts in `<skill>/evals/evals.json`; packages exclude those files.
- Run `python scripts/validate-skills.py` before committing.
- Do not modify code, post reviews, or otherwise publish side effects from a
  skill unless the user has explicitly requested that action.
