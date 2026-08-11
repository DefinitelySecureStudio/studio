# Definitely Secure accessibility contrast report

Status: Approved

Generated: 2026-08-11

Token version: 1.0.0

Ratios use the WCAG relative-luminance formula with unrounded sRGB token values. AA normal text requires 4.5:1, AA large text requires 3:1, and AAA normal text requires 7:1. Large text means at least 24 px regular or approximately 18.66 px bold.

| Pair | Foreground | Background | Ratio | AA normal | AA large | AAA normal | Approved role |
| --- | --- | --- | ---: | --- | --- | --- | --- |
| Light body | `#101828` | `#F8FAFC` | 16.96:1 | Pass | Pass | Pass | Normal text |
| Light secondary | `#475467` | `#F8FAFC` | 7.35:1 | Pass | Pass | Pass | Normal text |
| Light link | `#1D4E79` | `#F8FAFC` | 8.30:1 | Pass | Pass | Pass | Normal text |
| Primary reverse | `#F8FAFC` | `#101828` | 16.96:1 | Pass | Pass | Pass | Normal text |
| Gold control | `#101828` | `#F4B942` | 10.03:1 | Pass | Pass | Pass | Normal text |
| Coral callout | `#101828` | `#D95D52` | 4.76:1 | Pass | Pass | Fail | Normal text |
| Teal reverse | `#F8FAFC` | `#2F7F79` | 4.53:1 | Pass | Pass | Fail | Normal text |
| Violet reverse | `#F8FAFC` | `#6E62A6` | 5.07:1 | Pass | Pass | Fail | Normal text |
| Dark body | `#F8FAFC` | `#101828` | 16.96:1 | Pass | Pass | Pass | Normal text |
| Dark secondary | `#E4E7EC` | `#1D2939` | 11.86:1 | Pass | Pass | Pass | Normal text |
| Dark link | `#BFD9D7` | `#101828` | 11.93:1 | Pass | Pass | Pass | Normal text |
| Info message | `#1D4E79` | `#EAF2FA` | 7.68:1 | Pass | Pass | Pass | Normal text |
| Success message | `#205642` | `#E8F4EE` | 7.53:1 | Pass | Pass | Pass | Normal text |
| Warning message | `#704200` | `#FFF2D6` | 7.67:1 | Pass | Pass | Pass | Normal text |
| Danger message | `#7A2730` | `#FBEAEC` | 8.37:1 | Pass | Pass | Pass | Normal text |
| Comic panel | `#101828` | `#E8EEEF` | 15.13:1 | Pass | Pass | Pass | Normal text |
| Comic alternate | `#101828` | `#F3E9DC` | 14.79:1 | Pass | Pass | Pass | Normal text |
| Comic caption | `#101828` | `#F5E6B8` | 14.28:1 | Pass | Pass | Pass | Normal text |

## Required failures and restrictions

- Status Gold on Console Paper is 1.69:1 and is prohibited for text.
- Console Paper on Status Gold is the same 1.69:1 and is prohibited for text; use Assurance Ink instead.
- Console Paper on Meeting Coral is 3.56:1 and is not approved for body text.
- Neutral 400 on Neutral 50 is 2.46:1 and is restricted to disabled or nonessential decoration.
- Console Paper on Protocol Violet is 5.07:1; it passes AA normal text but not AAA.

## Non-text requirements

Interactive boundaries, focus indicators, and meaningful graphic objects require at least 3:1 against adjacent colors. Links in body copy are underlined. Status messages use a label or icon in addition to hue. Comic dialogue and essential line work remain legible in grayscale. Re-test after opacity, blending, antialiasing, imagery, or print conversion changes an effective color.
