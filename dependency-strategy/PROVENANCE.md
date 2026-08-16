# Release provenance and references

## Public release manifest

Every published comic or production release has a reader-safe manifest owned by
Universe. Platform may generate the proposal, but canon-editor review and merge
make it the public record.

The manifest records:

- permanent release or episode ID and revision;
- release-manifest contract name, version, Codex tag, Codex commit, artifact URI,
  media type, size, and digest;
- input Universe canon version, tag, commit, snapshot URI, size, and digest;
- Platform version, tag, commit, package or image URI, and artifact digest;
- every additional public contract or tool artifact using the stable reference
  tuple;
- build workflow identity, run URL, timestamp, and attestation when available;
- output rendition path or URI, media type, size, `sha256:` digest, and rights
  notice; and
- whether private context influenced the build and, if so, one opaque private
  attestation ID.

The public manifest must not contain a Lore repository URL, commit, path,
branch, issue, object URI, object version, digest, approver identity, or field
that can be derived from private content.

## Restricted private record

When private context is used, a restricted record maps the public opaque
attestation ID to:

- exact Lore commit and owning record IDs;
- context-package ID, object-store version, media type, size, and digest;
- Codex context-package contract reference;
- purpose, authorized Platform consumer, approval, generation time, and expiry;
- retention, logging, caching, and deletion requirements;
- Platform build identity and public release ID; and
- deletion or preservation evidence after the approved retention period.

Generate the attestation ID randomly. Do not derive it from the Lore commit,
content, digest, filename, episode ID, or timestamp. Store the record in Lore or
an approved private provenance system, never in Platform source or public build
artifacts.

## Release ordering

Use this sequence to keep the graph acyclic:

1. release Codex contracts;
2. release the Platform implementation that supports those contracts;
3. release or select input canon snapshot `C(n)`;
4. approve and generate any minimal private context export;
5. build release `R` from those exact inputs and verify every digest;
6. create both public and restricted provenance records as applicable;
7. have Universe editors approve the public artifacts and manifest; and
8. include `R` in a later canon snapshot `C(n+1)`.

Release `R` records `C(n)` as input. It must not claim `C(n+1)` as an input when
that snapshot includes `R`.

## Verification and rebuilds

A verifier must be able to fetch every public artifact, verify its size and
SHA-256 digest, trace it to an immutable tag and source commit, and verify a
build attestation when one exists. A maintainer with private authorization can
perform the same audit through the restricted record without exposing private
identifiers publicly.

Exact provenance makes inputs and outputs identifiable; it does not by itself
promise bit-for-bit reproducibility when tools, timestamps, randomness, fonts,
or external services are uncontrolled. A release claiming reproducibility must
also pin those influences and document the deterministic build procedure.

The examples in [`examples/`](examples/) are non-normative. Codex owns the
machine-readable manifest and context-package schemas used in production.
