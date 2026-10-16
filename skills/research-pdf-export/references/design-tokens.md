# Design Tokens: muted navy + Public Sans

Design conventions for the PDFs this skill renders: the suite's muted navy palette (`DESIGN-SYSTEM.md`, "Color Palette") with the Public Sans typeface. Exact values (font sizes, spacing, layout) live in `style-schema.json`, which mirrors the hardcoded constants in `scripts/generate_pdf.py` for human reference.

---

## Philosophy

Clarity through simplicity. Consistent use of color and type to create a unified visual system. Every element serves a purpose -- no decoration for its own sake.

Pages are light-dominant, formal, and quiet: navy is the single structural color, there is no bright or saturated blue anywhere, and every piece of text meets WCAG AA contrast against its background.

## Color tokens

The script names each constant after its role in the palette. Contrast ratios are WCAG 2.x.

| Script constant | Name | Hex | Used for | Contrast |
|---|---|---|---|---|
| `NAVY` | Navy | `#002436` | Section titles, H2, TOC title and numbers, accent bars, callout bar and text, table header text and rule, cover background | 16.1:1 on white, 14.4:1 on Mist; white on it 16.1:1 |
| `STEEL` | Steel | `#00537E` | H3 | 8.3:1 on white |
| `CHARCOAL` | Charcoal | `#1F2A30` | Body, bullets, table cells, TOC entries | 14.7:1 on white, 13.1:1 on Mist |
| `SLATE` | Slate | `#5C6670` | Footer text, callout attribution | 5.9:1 on white, 5.2:1 on Mist |
| `MIST` | Mist | `#F0F3F4` | Callout fill | fill only |
| `COOL_GRAY` | Cool Gray | `#E3E8EA` | Table header row | fill only |
| `RULE_GRAY` | Rule Gray | `#D4D8D9` | Thin rules, table row lines, TOC row lines, footer rule | non-text only |
| `ZEBRA` | Zebra | `#F7F9F9` | Alternate table rows | fill only |
| `LINK_BLUE` | Link Blue | `#167FA6` | External links only | 4.5:1 on white |
| `ON_DARK` | Muted sky | `#9CC3D5` | Accent on the navy cover: rule, subtitle, metadata labels | 8.6:1 on navy |
| `ON_DARK_SOFT` | Pale | `#DCE6EB` | Light text on navy: cover description | 12.7:1 on navy |
| `WHITE` | White | `#FFFFFF` | Page background; cover title and metadata values | — |

Status colors are reserved for signal indicators, never decoration, and always paired with a word or icon. The script defines them; the current layout uses none.

| Script constant | Hex | Use |
|---|---|---|
| `STATUS_OK` | `#4F7A28` | On track (5.1:1 on white) |
| `STATUS_RISK` | `#9A6A00` | At risk (4.7:1 on white) |
| `STATUS_BLOCK` | `#A33A3A` | Blocked or critical (6.5:1 on white) |

Rules:

- **One structural color.** Navy carries the skeleton; Steel marks the third level; everything else is charcoal on white or a cool gray.
- **Small text is `CHARCOAL` or `SLATE`.** Never a lighter gray.
- **No bright blue or cyan.** Link Blue is for links and nothing else.
- **Status colors signal, they don't decorate.**

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

- **Color palette:** the suite's own (`DESIGN-SYSTEM.md`), no company's visual identity.
- **Public Sans:** [github.com/uswds/public-sans](https://github.com/uswds/public-sans), also on Google Fonts as "Public Sans". Licensed under the SIL Open Font License 1.1; GSA's modifications are dedicated to the public domain (CC0), and the combined font is used under the OFL. The full terms ship in `assets/fonts/OFL.txt` and `assets/fonts/LICENSE.md`.

## Conventions

- **Author (PDF metadata):** the `--team` value when one is passed; otherwise left empty
- **Footer (right-aligned):** "Page {N}", or "{note} · Page {N}" when `--footer-note` is passed (for example "Confidential — Internal Use Only")
- **Footer template (left-aligned):** "{title} | {date}"
- **Cover logo:** none ships with the skill; a team can drop its own SVG at `assets/logo.svg` and the cover draws it (needs `svglib`)
- **No emojis** in any output
- **Sentence-case capitalization** for all text
