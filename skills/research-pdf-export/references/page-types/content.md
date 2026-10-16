# Page Type: Content

The default page frame for every body page (everything after cover and TOC). Implemented in `content_page_cb` and `parse_markdown` in `scripts/generate_pdf.py`.

## Page frame

The script draws **only a footer** on each content page. There is no top header rule, no document title in a header, no header page-number badge.

Each content page renders:

- **Footer rule** -- a 0.5pt `rule_gray` (`#D4D8D9`) horizontal line, full content width, drawn 0.15 inch below the bottom margin.
- **Footer text (left)** -- `{title}  |  {date}`, in 6.5pt Regular `slate` (`#5C6670`), drawn 0.35 inch below the bottom margin. `{title}` is the value passed via `--title` (or a title-cased version of the markdown filename). `{date}` is `--date` or "Month YYYY" of the current date.
- **Footer text (right)** -- `Page {N}`, same font/color, right-aligned at the same y-offset. When `--footer-note "<text>"` is passed, it renders as `{note}  ·  Page {N}` instead (e.g. `Confidential — Internal Use Only  ·  Page 3`). There is no default note.

The content area is everything between the top margin and the 0.85 inch bottom margin, with 0.75 inch left/right margins -- a 7.0 inch content width. The top margin is 0.75 inch plus 0.15 inch the document template adds, so body text starts 0.9 inch from the top edge.

All text is Public Sans, loaded from the skill's `assets/fonts/`. If those fonts can't be loaded, the same page renders in Helvetica (see `design-tokens.md`).

## Supported markdown elements

The body parser renders:

- **Headings**: `#` (H1, 32pt Light, `navy`), `##` (H2, 16pt Medium, `navy`), `###` (H3, 12pt Medium, `steel`; `####` and deeper render the same way). Headings are inline: no accent bar, no rule, no page break.
- **Body paragraphs**: 9.5pt Regular, `charcoal` (`#1F2A30`).
- **Inline formatting**: `**bold**`, `*italic*`, `***bold italic***`, `[label](url)` (external `http(s)` links render in `link_blue`, `#167FA6`; internal anchors are bolded). Bold and italic work in every element that takes inline formatting: headings, body, bullets, table cells, and callouts.
- **Bullet lists**: `- ` or `* ` (em-dash bullet), and indented sub-bullets (round bullet, deeper indent).
- **Blockquotes**: `> ` rendered as a callout box (`mist` fill, 3pt `navy` left bar, 9pt Italic text in `navy`, inline formatting intact). A line directly after the quote that starts with `--` or `—` becomes the attribution, in 8pt Regular `slate`. A single `*...*` wrapping the whole quote is dropped, since the callout is already italic.
- **Tables**: standard pipe-delimited markdown tables with a separator row. `cool_gray` header fill, SemiBold `navy` header text, 1pt `navy` rule under the header, white and `zebra` rows, 0.4pt `rule_gray` row lines.
- **Horizontal rules**: `---` (and `***`, `___`) rendered as thin rules.
- **Page breaks**: an explicit `<!-- pagebreak -->` HTML comment forces a new page.
- **Bold-label paragraphs**: lines that start with `**Label:**` get the label bolded inline.

## What the script does NOT do

- It does not draw a top header rule, page number, or running title at the top of content pages.
- It does not auto-detect or generate executive-summary, conclusion, or section-divider page types -- those are just regular content rendered with the H1/H2/H3 styles.
- It does not insert page breaks between H1 sections automatically. Authors must add `<!-- pagebreak -->` where they want a forced break.

## Style references

- `style-schema.json` > `content_footer.*` -- footer rule + text layout.
- `style-schema.json` > `text_styles.*` -- all text element styles.
- `style-schema.json` > `table_style.*` -- table formatting.
- `style-schema.json` > `callout_box.*` -- blockquote/callout formatting.
- `style-schema.json` > `thin_rule.*` -- the rule drawn for `---`.
