# Repository bootstrap checklist

Complete this checklist in the repository's creation pull request. Link the
accepted architecture decision that authorizes the repository.

## Identity and access

- [ ] Name, single responsibility, accountable owner, and visibility match the
      Studio architecture.
- [ ] Description and three to eight topics follow `METADATA.md`.
- [ ] `main` is the default branch; access is least-privilege.
- [ ] Issues, Wiki, Projects, Discussions, advisories, and forking follow the
      repository-feature defaults or record an exception.

## Files

- [ ] README is completed from `templates/README.md` without placeholders.
- [ ] The root `LICENSE` and `NOTICE` match the licensing matrix.
- [ ] `CODEOWNERS` names real users or teams and covers sensitive paths.
- [ ] `CHANGELOG.md`, `.gitignore`, and repository-specific documentation are
      present where applicable.
- [ ] Organization community-health defaults are inherited, or each local
      override documents its reason and includes the complete required set.
- [ ] Pull-request and issue templates render correctly on the default branch.

## Workflow and security

- [ ] The default branch has the required review, CODEOWNER, stale-approval,
      conversation, force-push, and deletion controls.
- [ ] Any plan-limited protection gap is recorded with owner and review date.
- [ ] Required CI checks are real, stable, and named; no placeholder is required.
- [ ] Private reporting instructions are tested without opening a public issue.
- [ ] Secret scanning, dependency alerts, and Dependabot security updates are
      enabled where available and applicable.
- [ ] `dependabot.yml` covers each actual ecosystem, or the repository records
      that it currently has no dependencies.

## Taxonomy and release

- [ ] Shared labels match `labels.yml`; local labels use the documented prefixes.
- [ ] The issue forms reference labels that exist in the repository.
- [ ] The release model and tag form are documented, or the repository explicitly
      states that it does not publish releases.
- [ ] The first validation run checks links, structured files, and any executable
      scaffold.

## Handoff

- [ ] The creation pull request lists settings that cannot be represented in Git.
- [ ] A maintainer verifies the default branch after merge.
- [ ] The repository is added to `ARCHITECTURE.md` and the Studio portfolio index.
- [ ] Exceptions have an owner, rationale, compensating control, and review date.
