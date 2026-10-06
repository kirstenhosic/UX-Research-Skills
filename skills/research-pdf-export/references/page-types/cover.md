# Page Type: Cover

Optional first page. Rendered only when the script is invoked with `--cover`. Implemented in `cover_page_cb` and `build_cover` in `scripts/generate_pdf.py`.

## What the script actually draws

1. **Full-bleed background fill** -- solid `primary-darker` (`#162E51`) covering the entire letter-size page.
2. **Accent line** -- a single 1pt horizontal line in `accent-cool` (`#00BDE3`), spanning the content width, drawn 122pt below the top of the page.
3. **Title block** -- pushed down 1.7 inches from the top:
   - Title (required, 45pt Light, white).
   - Subtitle (optional, 24pt Light, `accent-cool`) -- only if `--subtitle` is passed.
   - Description (optional, 14pt Light, `accent-cool-lighter`, `#E1F3F8`) -- only if `--description` is passed.
4. **Metadata block** -- pushed 2.5 inches below the title block. Each item is a label/value pair:
   - Label: 12pt Light, `accent-cool` (e.g. "Research date", "Team").
   - Value: 14pt Light, white.

   The "Research date" pair always renders: its value is `--date`, or the current month and year when `--date` is omitted. The "Team" pair renders only when `--team` is passed.
5. **Logo (optional)** -- no logo ships with the skill. A team that wants its own mark on the cover drops an SVG at `assets/logo.svg` in the skill folder (beside `scripts/`); the script then places it at the bottom-right corner with 57pt margins from the right and bottom edges, scaled to fit a 45x100pt box. Drawing it needs `svglib`. Skipped silently if the file is absent or `svglib` is not installed; an SVG that `svglib` cannot parse is skipped with a warning rather than failing the build.

After the cover, the script appends a `PageBreak` so subsequent pages use the standard content frame.

## CLI flags that drive the cover

| Flag | Required | Effect |
|------|----------|--------|
| `--cover` | Yes (to render this page at all) | Enables cover-page rendering. |
| `--title` | No (defaults to title-cased filename) | Used for cover title and footer template. |
| `--subtitle` | No | Renders the subtitle line. |
| `--description` | No | Renders the description line. |
| `--date` | No | Sets the "Research date" value on the cover and the date in the footer. Defaults to the current month and year. |
| `--team` | No | Renders "Team" metadata pair only when explicitly provided, and becomes the PDF's author metadata. The row is suppressed otherwise (and the author metadata left empty) — no default placeholder. |

## Markdown interactions

If the source markdown has a top-of-document H1 whose text matches the cover title (case-insensitive), the script drops that H1 and a single trailing `---` rule so the title doesn't appear twice. A `## Cover` block in the markdown (heading + body + trailing rule) is also stripped before parsing.

## Style references

- `style-schema.json` > `cover_page.*` -- background, accent line, optional logo placement.
- `style-schema.json` > `text_styles.cover_*` -- title, subtitle, description, metadata label/value styles.
