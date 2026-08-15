# Third-party dependency and asset rules

These rules apply to code, packages, snippets, fonts, images, audio, video,
datasets, models, model outputs, templates, and other material not authored and
owned by Definitely Secure Studio.

## Before adding material

1. Record its source URL, version or immutable revision, author or owner, and
   license identifier. Prefer an SPDX identifier when one exists.
2. Read the actual license and verify that the intended use, modification,
   distribution, hosting, and commercial use are allowed. A public download or
   a package-registry listing is not enough.
3. Confirm that the provider has a credible right to license the material. Do
   not use material with unknown or unverifiable provenance.
4. Check compatibility with the destination repository and distribution. Do not
   add copyleft, source-available, noncommercial, no-derivatives, field-of-use,
   or custom terms without maintainer and legal review.
5. Prefer a package-manager dependency to vendoring source. Pin an exact version
   or lockfile-resolved version where the ecosystem supports it.

## When material is accepted

- Preserve copyright, license, attribution, modification, and trademark notices.
- Include the complete license text or attribution in the location its license
  requires. Use `THIRD_PARTY_NOTICES` for distribution-level notices when
  appropriate.
- Keep file-level license headers and use `SPDX-License-Identifier` declarations
  where practical. Do not replace a third-party header with a Studio header.
- Keep third-party assets in a clearly named directory with a nearby license or
  provenance file. Do not place them inside a Studio proprietary asset directory
  without an explicit exception notice.
- Re-run license and vulnerability review when the dependency version, source,
  build packaging, or distribution model changes.

## Special cases

- **Fonts:** retain the font license, copyright statement, and Reserved Font Name
  declarations. Bundled Studio fonts currently identified as OFL-1.1 remain
  under that license; the Studio's surrounding typography guidance remains
  proprietary.
- **Creative assets:** obtain written terms that cover the exact media, channels,
  territories, duration, modifications, and commercial uses needed. Stock,
  marketplace, or commissioned assets are not presumed transferable.
- **AI-assisted material:** record the tool, model, date, source inputs, and
  applicable provider terms. Do not submit private lore, personal data, or
  third-party copyrighted inputs unless the use is approved. Human review and
  provenance records are required before publication.
- **Datasets and models:** review data rights, privacy, acceptable-use terms,
  redistribution restrictions, model-license conditions, and generated-output
  terms separately from the calling code's license.
- **Copied snippets:** treat snippets as third-party code unless they are plainly
  trivial or their license and provenance are recorded. A link in a comment does
  not cure incompatible terms.

## Pull-request evidence

A pull request adding third-party material should identify:

- the material and why it is needed;
- source, version, and license;
- where required notices are stored;
- whether it ships to users or is development-only; and
- any review or approval required by the triggers in
  [`POLICY.md`](POLICY.md#review-triggers).
