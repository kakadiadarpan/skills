---
name: pr-review
description: "Review GitHub pull requests in an evidence-first, chat-first style. Use for live PR reviews and rereviews."
---

# PR review

Review the current PR, not the story around it. Find real defects, explain the consequence plainly, and keep the result easy to act on.

## Recommended skills

This skill is designed to run with @i-have-adhd, @unslop, and @show-me. Before doing anything else, load each one that is installed with the skill tool.

If any are missing, tell the user once, at the start of the review, which ones and how to install them. Then continue the review without them.

```sh
npx skills@latest add ayghri/i-have-adhd --skill i-have-adhd
npx skills@latest add cursor/plugins --skill unslop
npx skills@latest add humanlayer/skills --skill show-me
```

- @i-have-adhd and @unslop apply to everything you write, including GitHub comments.
- @show-me applies to chat replies and GitHub comments. Use a diagram when a code path, data flow, or timing is easier to show than to describe. In GitHub comments, put a long diagram inside a `<details>` block.

## Scope and permission

- Never write to GitHub without the user's explicit approval. A write is anything other people can see or that changes the PR: comments, reviews, approvals, suggestions, replies, reactions, resolved threads, labels, review requests, PR state, pushes, and code edits.
- Approval covers only what the user saw. Show the exact text and target first. Approving one post does not approve the next, and a new head SHA needs fresh approval.
- A pending review counts as a write. Staging it and submitting it each need approval.
- Do not duplicate an existing active thread. Recheck the PR head and line positions immediately before posting.
- Review in a separate checkout of the PR head, never in the user's primary checkout.
- Read other repos without changing them. Run `git fetch`, then `git show origin/main:<path>`. Never switch branches or edit files in those checkouts.

## What to look for

In priority order:

1. Bugs and flaws: wrong behavior, failure paths, races, data loss, and security.
2. Simplifications and code reuse: code that duplicates an existing helper, or that can be shorter with the same behavior.
3. Docs and tests: changed behavior with no test, or a contract change with no doc update.

## Evidence before verdict

1. Pin the live head and base SHAs. Inspect the full diff, commit list, PR body, current checks, and unresolved review threads.
2. Read the relevant contract, spec, service guidance, and closest working implementation. For pipeline changes, trace producer, transport, and consumer paths.
3. Do not run builds, typechecks, or tests. Read the PR's CI results instead. Separate code failures from flaky, auth, network, dependency, or CI-environment failures.
4. Before a rereview or any publication, refresh the live head, base, checks, and review threads. If the head changed, do not reuse an earlier verdict.

## Findings

- Prefer a small set of high-confidence findings. Do not pad a review with speculative risks.
- Label each finding with a [Conventional Comments](https://conventionalcomments.org/) label:
  - `issue`: a concrete problem. Pair it with the fix.
  - `suggestion`: a specific improvement. Say what to change and why.
  - `question`: a possible problem you could not confirm. Ask instead of asserting.
  - `todo`: a small, required change.
  - `nitpick`: a preference. Never blocking.
  - `thought` or `note`: context for the author. Never blocking.
  - `praise`: something done well. At most one per review, and only when sincere.
- Decorate `issue`, `suggestion`, and `todo` with `(blocking)` or `(non-blocking)`. Use `(if-minor)` when the author should fix it only if the change is small. Add at most one topic decoration, such as `(security)` or `(test)`.
- For each finding, explain the triggering scenario, the concrete bad outcome, how likely it is, and the smallest fix. Link exact lines when available.
- Keep code behavior findings separate from merge or process blockers. Green checks alone do not make a PR merge-ready.
- If the user asks to ignore a finding category, omit it. If no actionable findings remain, say so plainly and note only meaningful residual risk.

## Rereviews

- Start by checking each prior finding against the new head. Report it as fixed, partially fixed, or still open.
- A new test only proves the exact path it exercises. Check neighboring lifecycle and failure paths before calling a finding fixed.

## Review reply

1. Verdict and next action, with the head SHA you reviewed.
2. A short summary of what the PR changes.
3. Numbered findings. Each starts with its label and decorations, then the subject, a link to the exact lines, and a description with the full evidence and the smallest fix.
4. What you checked, what you couldn't verify, and what still blocks the merge: failing or pending checks, missing code-owner approvals, and whether the user's approval would satisfy them.

When the user asks for an explanation, use simple terms first, then show the code path and timing that prove it.

## Posting to GitHub

- Put line-specific findings inline on the exact files and lines, and anything else in the review body.
- Each inline comment follows the Conventional Comments format:

  ```text
  **<label> (<decorations>):** <subject>

  <discussion>
  ```

  The subject says what to do. The discussion explains why, the bad outcome, how likely it is, and the fix, in a few short paragraphs. Put long evidence, such as traces, logs, or tables, in a `<details>` block. Use ```suggestion blocks for concrete edits.
- Write in a professional, friendly tone, following ASD-STE100 Simplified Technical English: short sentences, active voice, one instruction per sentence, and the same word for the same thing.
- Stage comments as a pending review (omit `event`). Submit it only when the user says to submit.
- Pin every review to the head SHA you reviewed (`commit_id`).
- When approving, submit the approval and any inline comments as one review, with this review body:
  - no comments: `looks good!`
  - one inline comment: `looks good, left an inline comment`
  - two or more inline comments: `looks good, left a few inline comments`

  A finding that can't go inline goes in the body below that line.
