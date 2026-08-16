# Compatibility policy

## Codex contracts

Each independently consumable Codex contract declares a public interface and
uses Semantic Versioning `MAJOR.MINOR.PATCH`.

- **Major:** an existing conforming producer or consumer must change to preserve
  correctness, safety, or meaning.
- **Minor:** backward-compatible additions, new optional capabilities, or a
  deprecation with the old behavior still supported.
- **Patch:** compatible corrections or clarifications that do not alter
  conforming behavior.

A breaking change includes removing or renaming a field, making an optional
field required, rejecting previously valid input, changing a field's meaning or
units, narrowing an accepted range, changing identity or ordering guarantees,
or weakening a documented security, privacy, or disclosure invariant.

Adding an optional field is minor only when old consumers can safely receive an
object without it and new producers do not emit it to consumers that have not
declared support. Each contract defines its unknown-field behavior; there is no
organization-wide assumption that unknown fields are ignored.

Versions below `1.0.0` are unstable and require exact-version compatibility
review for every upgrade. They do not make unannounced production breakage
acceptable.

## Consumer declarations

A consumer records both:

- a tested compatibility interval used to discover acceptable upgrades; and
- the exact resolved artifact tuple used by builds and releases.

Support for `MAJOR.MINOR` means accepting the documented behavior of the same
major at that minor or lower, subject to the contract's capability negotiation.
It does not authorize automatic upgrades without tests.

Every upgrade is a reviewed change that updates the pin, verifies the digest,
runs conformance fixtures, records migration effects, and updates the consumer
support matrix.

## Breaking-change process

A breaking Codex change requires:

1. an accepted RFC and new major version;
2. an inventory and owner for every known consumer;
3. parallel old/new schemas and conformance fixtures;
4. a migration guide and rollback plan;
5. a deprecation release before removal; and
6. a dated support window.

The default support window lasts through at least one stable minor release and
90 days after the replacement becomes available, whichever is longer. An RFC
may shorten it only for a documented security emergency or with explicit
approval from every affected consumer owner.

Retired releases and their notices remain available when legally and
operationally possible. Do not rewrite an old artifact to fix it; release a new
version and mark the old version affected or deprecated.

## Platform and canon

Platform's externally consumed software interface uses Semantic Versioning.
Internal implementation changes are versioned according to their effect on the
declared interface and emitted artifacts.

Universe canon snapshots continue to use `MAJOR.MINOR.PATCH` under their canon
policy: retcons are major, additive public canon is minor, and corrections that
do not change story truth are patch. Canon compatibility describes public story
truth, not software API compatibility.

Private Lore records do not receive public semantic versions. A context package
uses the semantic version of its Codex package contract plus an immutable object
version and digest for that exact export.
