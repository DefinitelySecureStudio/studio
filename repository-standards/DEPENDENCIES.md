# Dependency and update policy

Dependency intake follows the licensing and provenance rules in
[`licensing/THIRD_PARTY.md`](../licensing/THIRD_PARTY.md).

## Dependabot defaults

Add `.github/dependabot.yml` when a repository contains a supported package
manifest, container definition, GitHub Actions workflow, or other maintained
ecosystem. Start from
[`templates/.github/dependabot.yml.example`](templates/.github/dependabot.yml.example)
and keep only ecosystems actually present.

- Run version updates weekly, Monday morning in `America/New_York`.
- Group non-major development updates when the ecosystem supports grouping.
- Limit open update pull requests to avoid hiding product work.
- Apply `type:maintenance` and `area:dependencies` labels.
- Target `main` unless a maintained release branch has an explicit policy.
- Keep lockfiles committed when the ecosystem expects them.

Enable Dependabot security updates for repositories with dependencies. Treat a
security update as urgent based on exploitability and exposure, not the version
number alone. Do not auto-merge dependency changes until stable CI covers the
affected build and tests; even then, restrict auto-merge to reviewed, low-risk
updates under an explicit repository policy.

Repositories without dependencies do not add an empty active configuration.
Reassess when the first manifest or workflow dependency is introduced.
