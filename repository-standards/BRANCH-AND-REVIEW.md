# Branch and review policy

## Default branch

- Use `main` as the default branch.
- Do not commit directly to `main`; merge through a pull request.
- Use short-lived branches named `type/description`, such as
  `feat/context-builder` or `fix/manifest-validation`. Codex automation uses the
  required `codex/` prefix.
- Delete merged branches unless they are maintained release branches.

## Required protection

Protect the default branch in every repository with:

- at least one approving review;
- dismissal of stale approvals after new commits;
- a required CODEOWNER review;
- resolution of all review conversations;
- blocked force pushes; and
- blocked branch deletion.

Do not grant routine bypasses. Emergency bypasses require an owner, written
reason, linked follow-up issue, and retrospective review.

Require status checks only after the repository has stable CI. Name the exact
checks and require the branch to be current when the check is deterministic and
reasonably fast. Never create or require a placeholder check.

Prefer squash merging for focused feature and maintenance pull requests. Use a
merge commit only when preserving a coordinated history is materially useful;
use rebase merge only when the repository documents why its commit sequence is
part of the maintained record.

## Review expectations

- Authors do not approve their own changes when another qualified reviewer is
  available.
- Review against responsibility boundaries, security, licensing, tests,
  documentation, and rollback—not only syntax.
- Changes to governance, licenses, security policy, release controls,
  CODEOWNERS, or GitHub workflows require the accountable owner.
- Public tooling uses synthetic, licensed, or already-public fixtures.
- Canon and lore changes follow their editorial and disclosure policies in
  addition to this standard.

## Current GitHub Free exception

GitHub currently enforces this policy on the public repositories. The private
`lore` repository cannot enable branch protection under the organization's
current GitHub Free plan. Until the plan changes, Lore maintainers must use pull
requests and the same review rules as a procedural control, restrict write
access, and review the exception quarterly. This is a known control gap, not an
equivalent technical safeguard.
