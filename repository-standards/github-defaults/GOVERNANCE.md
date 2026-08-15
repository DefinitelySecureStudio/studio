# Governance

Definitely Secure Studio repositories use responsibility-based ownership. The
Studio architecture identifies the authoritative repository for each concern;
the repository README identifies its accountable maintainers and boundaries.

## Roles

- **Organization owners** maintain organization access, shared policy, and
  cross-repository governance.
- **Repository maintainers** own repository health, triage, releases, settings,
  and enforcement of its responsibility boundary.
- **CODEOWNERS** provide required review for named paths and do not gain authority
  outside those paths merely by reviewing a change.
- **Contributors** propose changes and supply the evidence needed for review.

One person may hold multiple roles. Access remains least-privilege and is
reviewed when responsibilities change.

## Decisions

- Organization-wide architecture, licensing, brand, and repository-standard
  decisions are recorded in the public `studio` repository.
- Stable cross-repository technical contracts are decided in `codex`.
- Product implementation decisions remain with the affected repository.
- Public canon requires canon-editor approval; private lore requires authorized
  lore-editor approval and does not become public through an internal merge.

Maintainers seek evidence and practical consensus. The accountable owner makes
the final decision when consensus is not available and records the rationale in
the issue, pull request, or ADR appropriate to its scope.

## Changes to governance

Changes to organization-wide governance require a Studio issue, a focused pull
request, and owner review. Repository-local overrides must explain the concrete
boundary that requires them and remain compatible with organization policy.
