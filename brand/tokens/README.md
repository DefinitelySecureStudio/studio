# Definitely Secure design tokens

Version: 1.0.0

These files are the machine-readable implementation of the approved brand system.

| File | Format | Authority |
| --- | --- | --- |
| [`colors.json`](colors.json) | DTCG-compatible JSON | Canonical color values and metadata |
| [`colors.yaml`](colors.yaml) | YAML | Mirror of the color token hierarchy |
| [`colors.css`](colors.css) | CSS | Raw colors and theme-aware semantic roles |
| [`typography.json`](typography.json) | DTCG-compatible JSON | Canonical families, weights, sizes, line heights, and tracking |
| [`typography.css`](typography.css) | CSS | Font faces, role variables, and utilities |
| [`index.css`](index.css) | CSS | Convenience entry point importing both CSS systems |

Use semantic CSS variables when a role exists. JSON token paths use DTCG `$type` and `$value` fields. Consumers that do not yet implement composite typography tokens may read the individual family, weight, dimension, number, and tracking groups.

Token changes follow the [brand changelog](../CHANGELOG.md) and version policy in the [Brand Guide](../BRAND_GUIDE.md).
