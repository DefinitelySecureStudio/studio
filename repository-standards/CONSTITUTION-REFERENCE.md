# Constitution reference and conformance declaration

Every maintained Definitely Secure Studio repository records the exact
Constitution version it was assessed against. The declaration makes scope and
evidence discoverable; it does not turn a repository README into constitutional
authority.

## Required immutable reference

For version 1.0.0 and later, record all three values:

```text
version: 1.0.0
tag: constitution/v1.0.0
commit: <full 40-character commit tagged by constitution/v1.0.0>
```

Link the tag to the immutable Studio release and the commit to the exact
`CONSTITUTION.md` revision. Do not use `main`, another branch, `latest`, a
version range, a copied Constitution, or a tag without its full commit as the
governing reference. Historical pre-1.0 assessments pin the full Studio commit.

## Repository declaration

Place a reader-safe declaration in the repository README or its root governance
file:

```markdown
## Constitutional alignment

- Constitution: [Definitely Secure Studio Constitution v1.0.0](<immutable tag URL>)
- Constitution commit: [`<full commit>`](<commit URL>)
- Status: `<Conforming | Authorized exception | Transition required | Nonconforming — blocked | Not assessed>`
- Assessed scope: `<repository paths, systems, workflows, and releases covered>`
- Excluded scope: `<scope and rationale, or None>`
- Accountable owner: `<named human or maintained team with named decision owner>`
- Assessment revision and date: `<repository commit>; <ISO 8601 date>`
- Evidence: `<durable conformance record or issue/PR>`
- Active constitutional exceptions: `<stable IDs, or None>`
- Next review: `<date or material trigger>`
```

Do not write “constitutionally compliant” without the status, assessed scope,
exact version and commit, owner, and evidence. A declaration covers only the
identified repository revision and scope. Sensitive evidence remains in a
paired restricted record; the public declaration contains only a reader-safe
reference.

## ADRs, RFCs, specifications, workflows, and releases

Repeat the exact Constitution version, tag, and commit in a material ADR, RFC,
stable specification, agent instruction set, workflow contract, manifest, or
release record when its authority, safeguards, or approval depends on that
version. Also record the applicable checklist profile and evidence location.

A document reviewed against one version does not float to another automatically.
Generated copies and prompt excerpts may provide context but must identify the
authoritative immutable reference and must not be treated as a competing source.

## Adoption and re-review

- A **Major** Constitution version requires a new impact assessment, complete
  applicable checklist, explicit owner approval, and migration before a
  `Conforming` claim.
- A **Minor** version requires review of every addition and affected assumption,
  updated evidence, and an explicit adoption record.
- A **Patch** requires verification that corrected wording did not change a
  relied-on interpretation and an updated pin before claiming the Patch.

Re-review is also required when repository responsibility, visibility, data,
authority, provider, contract, agent capability, release model, protected
boundary, or material implementation changes; when evidence becomes stale; or
when an incident, finding, waiver, or constitutional exception affects the
claim.

Preserve the previous declaration and assessment in Git history. Never edit an
old release record to imply that a later Constitution version governed it.

## Nonconformance and exceptions

Use `Transition required`, `Nonconforming — blocked`, or `Not assessed` honestly
when the evidence does not support `Conforming`. A release waiver does not cure
repository-wide constitutional nonconformance. An `Authorized exception` status
must identify the active entry in
[`CONSTITUTION_EXCEPTIONS.md`](../CONSTITUTION_EXCEPTIONS.md) and cannot claim
coverage beyond its exact scope or expiry.
