# ADR 0005: Organization repository standards and GitHub defaults

- Status: Accepted
- Date: 2026-08-15
- Decision owners: Definitely Secure Studio
- Related issue: [#32 — Create organization-wide repository templates and defaults](https://github.com/DefinitelySecureStudio/studio/issues/32)
- Parent epic: [#2 — Repository Architecture](https://github.com/DefinitelySecureStudio/studio/issues/2)

## Context

The Studio now maintains public governance, tooling, specification, experiment,
and canon repositories plus a private lore repository. Their responsibilities
and licenses differ, but contributors should not have to relearn basic issue,
review, security, support, release, and repository-management conventions in
each one.

GitHub can inherit supported community-health files from a public organization
repository named `.github`. It does not inherit every repository file or
setting, and a repository-local issue-template directory replaces the entire
inherited issue-template directory. Branch rules, labels, dependency updates,
metadata, licenses, CODEOWNERS, and changelogs therefore need an explicit
bootstrap process in addition to inherited defaults.

The organization currently uses GitHub Free. Default-branch protection is
available for the public repositories, but GitHub does not allow it on the
private `lore` repository under the current plan.

## Decision

Create a public organization repository named `.github` and populate it from
[`repository-standards/github-defaults/`](../repository-standards/github-defaults/).
It will be the authoritative distribution point for supported organization-wide
community-health files:

- `CODE_OF_CONDUCT.md`;
- `CONTRIBUTING.md`;
- `GOVERNANCE.md`;
- `SECURITY.md`;
- `SUPPORT.md`;
- issue forms and their chooser configuration; and
- the pull-request template.

The source templates, policies, and bootstrap checklist remain versioned in
`studio/repository-standards/`. Changes to organization defaults are proposed
here first, then promoted to `.github` without changing their substance. A
repository may override a default only when its responsibility, visibility,
security boundary, or release model requires different instructions. The local
file must identify the reason for the override.

Files and settings that GitHub does not inherit are applied per repository from
the same standard. These include the README skeleton, license and notice,
CODEOWNERS, changelog, labels, Dependabot configuration, repository metadata,
default-branch settings, and branch/review rules.

All repositories use `main` as the default branch and changes reach `main`
through pull requests. The public repositories require one approving review,
CODEOWNER review, dismissal of stale approvals, resolution of review threads,
and blocked force-pushes and deletions. Required status checks are added only
after a stable CI job exists; a placeholder check is never required.

`lore` follows the same pull-request workflow by policy, but its missing
platform-enforced branch protection is a recorded exception until the
organization upgrades to a plan that supports protection for private
repositories. Maintainers must not confuse the policy with a technical control.

Repository labels, releases, descriptions, topics, dependency updates, and
bootstrap verification follow the documents under `repository-standards/`.

## Rationale

A public `.github` repository gives contributors consistent guidance without
copying files into every repository. Keeping the canonical source in `studio`
preserves organization-level review and prevents the distribution repository
from becoming a second governance authority.

Separating inherited files from bootstrap-only files mirrors GitHub's actual
behavior. Explicit local overrides preserve repository-specific boundaries,
especially public canon and private lore handling.

## Consequences

### Positive

- New repositories can be created from one repeatable checklist.
- Common contribution and reporting guidance changes in one distribution point.
- Labels, metadata, reviews, releases, and dependency updates use named rules.
- GitHub Free limitations are visible instead of silently weakening policy.

### Tradeoffs

- Promotion from `studio` to `.github` is a coordinated change.
- Local overrides must be reviewed when organization defaults change.
- Some repository settings still require API or owner-level configuration.
- Private branch protection requires a future plan upgrade or an equivalent
  platform control.

## Rejected alternatives

### Copy every common file into every repository

Rejected because copies drift and obscure whether a local difference is
intentional. Only files GitHub cannot inherit, or justified overrides, belong in
each repository.

### Make the `.github` repository private

Rejected because GitHub requires it to be public for most organization-wide
community-health defaults.

### Treat repository templates as branch protection

Rejected because documentation cannot prevent a force push or unreviewed merge.
The standard distinguishes policy from enforced GitHub settings.

## Implementation

The complete standard and source templates live in
[`repository-standards/`](../repository-standards/). The
[`bootstrap checklist`](../repository-standards/BOOTSTRAP-CHECKLIST.md) is the
required acceptance record for each new repository.
