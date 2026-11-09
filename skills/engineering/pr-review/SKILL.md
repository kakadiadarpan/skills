---
name: pr-review
description: "Review GitHub pull requests in an evidence-first, chat-first style. Use for live PR reviews and rereviews."
---

# PR review

Review the current PR, not the story around it. Find real defects, explain the consequence plainly, and keep the result easy to act on.

## Required skills

Before doing anything else, load @i-have-adhd, @unslop, and @show-me with the skill tool.

- @i-have-adhd and @unslop apply to everything you write, including GitHub comments.
- @show-me applies to chat replies and GitHub comments. Use a diagram when a code path, data flow, or timing is easier to show than to describe. In GitHub comments, put the diagram inside the `<details>` block.

## Scope and permission

- Never write to GitHub without the user's explicit approval. A write is anything other people can see or that changes the PR: comments, reviews, approvals, suggestions, replies, reactions, resolved threads, labels, review requests, PR state, pushes, and code edits.
- Approval covers only what the user saw. Show the exact text and target first. Approving one post does not approve the next, and a new head SHA needs fresh approval.
- Do not duplicate an existing active thread. Recheck the PR head and line positions immediately before posting.
- Review in a separate checkout of the PR head, never in the user's primary checkout.
- Read other repos without changing them. Run `git fetch`, then `git show origin/main:<path>`. Never switch branches or edit files in those checkouts.

## Evidence before verdict

1. Pin the live head and base SHAs. Inspect the full diff, commit list, PR body, current checks, and unresolved review threads.
2. Read the relevant contract, spec, service guidance, and closest working implementation. For pipeline changes, trace producer, transport, and consumer paths.
3. Test the changed behavior when practical. Run tools with the repo's pinned toolchain, such as the Node version in `engines.node`. Separate code failures from sandbox, auth, network, dependency, or test-environment failures. A missing-package error usually means a stale install, not a PR bug.
4. Before a rereview or any publication, refresh the live head, base, checks, and review threads. If the head changed, do not reuse an earlier verdict.

## Findings

- Prefer a small set of high-confidence findings. Do not pad a review with style nits or speculative risks.
- Give each finding a priority: blocking, non-blocking, or nit. Explain the triggering scenario, the concrete bad outcome, and the smallest fix. Link exact lines when available.
- Keep code behavior findings separate from merge or process blockers. Green checks alone do not make a PR merge-ready.
- If the user asks to ignore a finding category, omit it. If no actionable findings remain, say so plainly and note only meaningful residual risk.

## Rereviews

- Start by checking each prior finding against the new head. Report it as fixed, partially fixed, or still open.
- A new test only proves the exact path it exercises. Check neighboring lifecycle and failure paths before calling a finding fixed.

## Review reply

1. Verdict and next action, with the head SHA you reviewed.
2. A short summary of what the PR changes.
3. Numbered findings. Each has a concise title, a priority, a link to the exact lines, and a description with the full evidence and the smallest fix.
4. What you checked, what you couldn't verify, and what still blocks the merge: failing or pending checks, missing code-owner approvals, and whether the user's approval would satisfy them.

When the user asks for an explanation, use simple terms first, then show the code path and timing that prove it.

## Posting to GitHub

- Put line-specific findings inline and anything else in the review body.
- Each inline comment starts with a one-line Conventional Comment, like `issue (blocking): ...`, followed by a `<details><summary>Evidence and suggested fix</summary>` block. Use ```suggestion blocks for concrete edits.
- Pin every review to the head SHA you reviewed (`commit_id`).
- When approving, submit the approval and any inline comments as one review, with this review body:
  - no comments: `looks good!`
  - one non-blocking inline comment: `looks good, left a non-blocking inline comment`
  - two or more non-blocking inline comments: `looks good, left a few non-blocking inline comments`
  A finding that can't go inline goes in the body below that line.
