# research-pdf-export

Markdown in, PDF in USWDS styling out (ReportLab, U.S. Web Design System color tokens, the Public Sans typeface, optional cover page, TOC from a `## Contents` list).

Adapted from the `document-conversion` skill by Neil Everette. The renderer and style reference are his; the marketplace manifest, install prompt and usage-telemetry script were removed when it joined this suite.

Dr. Morgan offers this at the export seam for anything drafted as Markdown (plans, guides, survey text, findings appendices). It is Markdown-only: for `.docx` or `.pptx`, use `research-document-template`.

Needs `reportlab`, installed into a temporary venv by the skill. `svglib` is only needed for the optional cover logo: no logo ships with the skill, so to put your team's mark on the cover, drop an SVG at `assets/logo.svg` and the renderer draws it when present. Footers read `{title} | {date}` on the left and `Page N` on the right; pass `--footer-note "Confidential — Internal Use Only"` (or any note) to render `{note} · Page N`.

Public Sans ships with the skill in `assets/fonts/` (ten static TTFs) under the SIL Open Font License 1.1; `OFL.txt` and `LICENSE.md` sit beside the fonts. Nothing is downloaded at run time. If the fonts can't be loaded, the script prints one warning and the PDF falls back to Helvetica, with the same colors and layout.
