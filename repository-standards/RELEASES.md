# Release and tag conventions

## General rules

- Create releases from the protected `main` branch or a documented protected
  release branch.
- Use annotated, immutable tags. Never move or reuse a published tag.
- Record user-visible changes in `CHANGELOG.md` before tagging.
- Attach generated artifacts with source revision, build provenance, checksums,
  and applicable notices.
- Mark unstable releases with a prerelease identifier and GitHub's prerelease
  flag. Do not call an artifact stable solely because it has a tag.
- Publish release notes that identify changes, upgrade or migration steps,
  known limitations, and security-relevant behavior without disclosing an
  unremediated vulnerability.

## Version forms

Software and independently released packages use Semantic Versioning tags of
the form `vMAJOR.MINOR.PATCH`, with optional prerelease suffixes such as
`v1.4.0-rc.1`.

Repositories with multiple independently versioned artifacts prefix the tag
with the durable artifact name, for example `manifest/v1.2.0`. The version's
compatibility meaning and cross-repository pinning rules are decided in issue
#33; this document defines naming and release hygiene only.

Creative publications retain their permanent `DS-NNNN` episode identifier.
That identifier is not a software version. Any corrected rendition or metadata
snapshot records its own revision without changing the episode identity.

`lab` does not publish stable releases by default. `lore` does not publish
public releases or tags. Studio governance and brand releases must document
their repository-specific version form before the first tagged release.

## Changelog

Keep an `Unreleased` section at the top, followed by versioned sections in
reverse chronological order. Group entries under `Added`, `Changed`, `Fixed`,
`Deprecated`, `Removed`, and `Security` only when the group has entries. Link
each release to its comparison and each security entry to a safe advisory when
disclosure is appropriate.
