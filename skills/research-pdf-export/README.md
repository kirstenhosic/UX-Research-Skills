# research-pdf-export

Markdown in, PDF in IBM Carbon styling out (ReportLab, IBM Plex Sans, IBM Design Language colors, optional cover page, TOC from a `## Contents` list).

Adapted from the `document-conversion` skill by Neil Everette. The renderer and style reference are his; the marketplace manifest, install prompt and usage-telemetry script were removed when it joined this suite.

Dr. Morgan offers this at the export seam for anything drafted as Markdown (plans, guides, survey text, findings appendices). It is Markdown-only: for `.docx` or `.pptx`, use `research-document-template`.

Needs `reportlab` and `svglib` (installed into a temporary venv by the skill) and, for an optional cover logo, `cairo` via `brew install cairo pkg-config`. No logo ships with the skill: to put your team's mark on the cover, drop an SVG at `assets/logo.svg` and the renderer draws it when present. Footers read `{title} | {date}` on the left and `Page N` on the right; pass `--footer-note "Confidential — Internal Use Only"` (or any note) to render `{note} · Page N`. IBM Plex Sans is optional; without it the PDF falls back to built-in fonts.
