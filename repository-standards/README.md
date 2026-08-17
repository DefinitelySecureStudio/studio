# Repository standards

This directory is the authoritative implementation guide for creating and
maintaining Definitely Secure Studio repositories. The governing decision is
[ADR 0005](../adr/0005-organization-repository-standards.md).

## What is inherited

The contents of [`github-defaults/`](github-defaults/) are promoted unchanged to
the public `DefinitelySecureStudio/.github` repository. GitHub supplies those
community-health files to organization repositories that do not define a local
file of the same type.

A repository-local file takes precedence. If a repository contains any file in
`.github/ISSUE_TEMPLATE/`, its whole issue-template directory is local: GitHub
does not combine it with the organization default directory. Keep the complete
set locally when overriding one issue form.

## What is applied locally

GitHub does not inherit licenses, notices, README files, changelogs, CODEOWNERS,
labels, Dependabot configuration, metadata, or branch settings. Apply those
using:

- [`templates/`](templates/) for repository files;
- [`LABELS.md`](LABELS.md) and [`labels.yml`](labels.yml) for label definitions;
- [`BRANCH-AND-REVIEW.md`](BRANCH-AND-REVIEW.md) for default-branch controls;
- [`DEPENDENCIES.md`](DEPENDENCIES.md) for update automation;
- [`CONSTITUTION-REFERENCE.md`](CONSTITUTION-REFERENCE.md) for immutable
  constitutional references, conformance declarations, and re-review;
- [`RELEASES.md`](RELEASES.md) for tags and releases;
- [`METADATA.md`](METADATA.md) for descriptions, topics, and feature settings;
  and
- [`BOOTSTRAP-CHECKLIST.md`](BOOTSTRAP-CHECKLIST.md) for final verification.

The repository's license classification comes from the
[licensing policy](../licensing/POLICY.md), not from this template set.

## Override rule

Use an organization default unless the repository has a concrete difference in
responsibility, visibility, security boundary, audience, or release process.
Document the reason near the overridden instruction. Local preferences alone
are not enough to fork a default.

## Change flow

1. Propose organization-standard changes in `studio`.
2. Review effects on every existing repository and local override.
3. Merge the Studio decision.
4. Promote `github-defaults/` to the public `.github` repository.
5. Apply non-inherited template or setting changes to affected repositories.
6. Record exceptions and a review date in the affected repository.
