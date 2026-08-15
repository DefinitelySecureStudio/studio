# Repository metadata conventions

## Name and description

Repository names follow the naming rules in
[`ARCHITECTURE.md`](../ARCHITECTURE.md#naming-convention).

Write a single-sentence description in plain language that says what the
repository owns. Keep it under 160 characters, omit a trailing period when the
GitHub UI would display it as a label, and avoid implementation details likely
to change.

## Topics

Use three to eight lowercase, hyphenated topics. Every Studio repository uses
`definitely-secure-studio`; add durable responsibility and domain topics rather
than languages, temporary initiatives, or team names unless discovery truly
depends on them.

## Repository features

- Enable Issues when the repository accepts tracked work.
- Disable Wiki because versioned documentation belongs in the repository.
- Disable Projects unless a repository owner documents a local planning need;
  organization Projects are preferred for cross-repository work.
- Disable Discussions unless a named moderation and support owner exists.
- Enable vulnerability reporting and security advisories where GitHub supports
  them.
- Disable forking for private repositories when the organization plan exposes
  that control.
- Set merge options according to
  [`BRANCH-AND-REVIEW.md`](BRANCH-AND-REVIEW.md).

## Visibility and ownership

Visibility follows the architecture and licensing decisions; it is never chosen
from the template default. Assign a CODEOWNER before accepting contributions.
Descriptions and topics do not override the README, license, or repository
responsibility boundary.
