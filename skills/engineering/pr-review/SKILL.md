---
name: pr-review
description: "Review pull requests in evidence-first, chat-first style."
---

# PR review

Review the current PR, not the story around it. Find real defects, explain the consequence plainly, and keep the result easy to act on.

## Scope and permission

- Default to a read-only, chat-first review.
- Use inline comments for line-specific issues. Use Conventional Comments, such as `**issue (blocking)**: ...` or `**issue (non-blocking)**: ...`. State the consequence and smallest credible fix.
- Do not duplicate an existing active thread. Recheck the PR head and line positions immediately before posting.

## Evidence before verdict

1. Pin the live head and base SHAs. Inspect the full diff, commit list, PR body, current checks, and unresolved review threads.
2. Read the relevant contract, spec, service guidance, and closest working implementation. For pipeline changes, trace producer, transport, and consumer paths.
3. Test the changed behavior when practical. Separate code failures from sandbox, auth, network, dependency, or test-environment failures.
4. Before a rereview or any publication, refresh the live head, base, checks, and review threads. If the head changed, do not reuse an earlier verdict.

## Findings

- Prefer a small set of high-confidence findings. Do not pad a review with style nits or speculative risks.
- Use a clear priority. Explain the triggering scenario, the concrete bad outcome, and the smallest fix. Link exact lines when available.
- Keep code behavior findings separate from merge or process blockers. Green checks alone do not make a PR merge-ready.
- If the user asks to ignore a finding category, omit it. If no actionable findings remain, say so plainly and note only meaningful residual risk.

## Rereviews

- Start by checking each prior finding against the new head. Report it as fixed, partially fixed, or still open.
- A new test only proves the exact path it exercises. Check neighboring lifecycle and failure paths before calling a finding fixed.

## Output shape

- Lead with the verdict or next action.
- Keep findings short and concrete. Use numbered items for multiple findings.
- For an inline comment requested with a details block, put the Conventional Comment first, then use `<details><summary>...</summary>` for the evidence and suggested fix.
- When the user asks for an explanation, use simple terms first, then show the code path and timing that prove it.
