# Label taxonomy

Every repository starts with the labels in [`labels.yml`](labels.yml). Names use
a lowercase `category:value` form so lists sort predictably. Do not create a
synonym when an existing label expresses the same meaning.

## Categories

| Prefix | Purpose | Required use |
| --- | --- | --- |
| `type:` | Kind of work or report | Exactly one after triage |
| `status:` | Current workflow state | Zero or one; remove stale states |
| `priority:` | Urgency and impact | Zero or one; maintainers assign it |
| `area:` | Repository or domain ownership | One or more when useful |

The shared `area:` labels describe organization-wide concerns. Repositories may
add durable local areas such as `area:schemas` or `area:canon`, but must keep the
same prefix and avoid team names that may change.

## Priority definitions

- `priority:p0`: active critical incident, disclosure, or data-loss risk;
- `priority:p1`: urgent, severe impact with no reasonable workaround;
- `priority:p2`: normal planned work; and
- `priority:p3`: low urgency, polish, or future consideration.

Security vulnerabilities are never filed publicly merely to obtain a label.
Use the private reporting process in `SECURITY.md`.

## Lifecycle

- Issue forms add a type and `status:triage` automatically.
- A maintainer removes `status:triage` after confirming scope and ownership.
- `status:blocked` must state the blocking condition in a comment.
- `status:ready` means requirements are sufficient for implementation.
- Close completed, duplicate, declined, or invalid work with a short rationale;
  do not create permanent status labels for terminal states already represented
  by GitHub.
