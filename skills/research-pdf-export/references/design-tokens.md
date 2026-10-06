# Design Tokens: USWDS + Public Sans

Design conventions for the PDFs this skill renders in USWDS styling: the U.S. Web Design System (USWDS) color tokens with the Public Sans typeface. Exact values (font sizes, spacing, layout) live in `style-schema.json`, which mirrors the hardcoded constants in `scripts/generate_pdf.py` for human reference.

---

## Philosophy

Clarity through simplicity. Consistent use of color and type to create a unified visual system. Every element serves a purpose -- no decoration for its own sake.

Pages are light-dominant with one accent color, and every piece of text meets WCAG AA contrast against its background.

## Color tokens

Hex values are the published USWDS defaults. The script names each constant after its token (`primary` is `PRIMARY`, `base-dark` is `BASE_DARK`). Contrast ratios are WCAG 2.x.

| Script constant | USWDS token | Hex | Used for | Contrast |
|---|---|---|---|---|
| `PRIMARY` | `primary` | `#005EA2` | The single accent: TOC accent bar and numbers, callout left bar, links | 6.72:1 on white, 5.39:1 on `primary-lighter` |
| `PRIMARY_DARK` | `primary-dark` | `#1A4480` | Secondary accent (defined; the current layout doesn't use it) | 9.62:1 on white |
| `PRIMARY_DARKER` | `primary-darker` | `#162E51` | Dark anchor: cover background; callout quote text | white on it 13.60:1; 10.90:1 on `primary-lighter` |
| `PRIMARY_LIGHTER` | `primary-lighter` | `#D9E8F6` | Accent tint: callout fill | fill only |
| `ACCENT_COOL` | `accent-cool` | `#00BDE3` | Accent on dark: cover rule, subtitle, metadata labels | 6.08:1 on `primary-darker` |
| `ACCENT_COOL_LIGHTER` | `accent-cool-lighter` | `#E1F3F8` | Light text on dark: cover description | 11.90:1 on `primary-darker` |
| `INK` | `ink` | `#1B1B1B` | Headings, body, table text; table header rule; TOC heavy rule | 17.22:1 on white, 15.11:1 on `base-lightest` |
| `BASE_DARK` | `base-dark` | `#565C65` | Secondary text: footers, callout attribution | 6.74:1 on white, 5.40:1 on `primary-lighter` |
| `BASE_LIGHTER` | `base-lighter` | `#DFE1E2` | Rules and dividers: thin rules, table row lines, TOC row lines, footer rule | non-text only |
| `BASE_LIGHTEST` | `base-lightest` | `#F0F0F0` | Fills: table header row, zebra rows | fill only |
| `WHITE` | white | `#FFFFFF` | Page background; cover title and metadata values | — |

State tokens are reserved for signal indicators, never decoration. The script defines them; the current layout uses none.

| Script constant | USWDS token | Hex | Use |
|---|---|---|---|
| `SUCCESS` / `SUCCESS_DARKER` | `success` / `success-darker` | `#00A91C` / `#216E1F` | Fill / text (6.34:1 on white) |
| `ERROR` / `ERROR_DARK` | `error` / `error-dark` | `#D54309` / `#B50909` | Fill / text (6.98:1 on white) |
| `WARNING` | `warning` | `#FFBE2E` | Fill only, always with `ink` text (10.38:1); never as text |
| `INFO` / `INFO_DARKER` | `info` / `info-darker` | `#00BDE3` / `#2E6276` | Fill / text (6.72:1 on white) |

Rules:

- **One accent.** `primary` on light pages, `accent-cool` on the dark cover.
- **Small text is `ink` or `base-dark`.** Never use `base` (`#71767A`, 4.03:1 on `#F0F0F0`) or a lighter gray for text.
- **State colors signal, they don't decorate.**

## Typography

Public Sans is the sole typeface. Weight communicates hierarchy:

- **Light (300):** display and titles -- H1, the Contents page, every line on the cover
- **Regular (400):** body text, bullets, table cells, footers, callout attribution
- **Medium (500):** subheadings (H2, H3)
- **SemiBold (600):** table header row
- **Bold (700):** inline emphasis only (`**bold**`), never headings
- **Italic (400 italic):** callout (blockquote) text

Inline markup keeps the weight of the text around it: `*italic*` becomes Light Italic in an H1, Medium Italic in an H2, SemiBold Italic in a table header. `**bold**` is always Bold, and `***bold italic***` is always Bold Italic.

### Font files and fallback

The ten static faces (`PublicSans-Light.ttf` through `PublicSans-BoldItalic.ttf`) ship with the skill in `assets/fonts/`, beside `OFL.txt` and `LICENSE.md`. The script loads them from there by default; `--font-dir` points it at another folder holding the same ten files. Nothing is downloaded.

If any of the ten can't be loaded, the script prints one warning on stderr and renders every face in Helvetica, so the PDF still builds with the same colors and layout:

| Public Sans face | Helvetica stand-in |
|---|---|
| Light, Regular | Helvetica |
| Medium, SemiBold, Bold | Helvetica-Bold |
| Italic, LightItalic | Helvetica-Oblique |
| MediumItalic, SemiBoldItalic, BoldItalic | Helvetica-BoldOblique |

## Sources and licenses

- **USWDS color tokens:** [theme tokens](https://designsystem.digital.gov/design-tokens/color/theme-tokens/) and [state tokens](https://designsystem.digital.gov/design-tokens/color/state-tokens/). USWDS is in the public domain (CC0 1.0).
- **Public Sans:** [github.com/uswds/public-sans](https://github.com/uswds/public-sans), also on Google Fonts as "Public Sans". Licensed under the SIL Open Font License 1.1; GSA's modifications are dedicated to the public domain (CC0), and the combined font is used under the OFL. The full terms ship in `assets/fonts/OFL.txt` and `assets/fonts/LICENSE.md`.

## Conventions

- **Author (PDF metadata):** the `--team` value when one is passed; otherwise left empty
- **Footer (right-aligned):** "Page {N}", or "{note} · Page {N}" when `--footer-note` is passed (for example "Confidential — Internal Use Only")
- **Footer template (left-aligned):** "{title} | {date}"
- **Cover logo:** none ships with the skill; a team can drop its own SVG at `assets/logo.svg` and the cover draws it (needs `svglib`)
- **No emojis** in any output
- **Sentence-case capitalization** for all text
