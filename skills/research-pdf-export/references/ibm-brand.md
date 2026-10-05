# IBM Design Language Reference

Design philosophy and conventions for the PDFs this skill renders in IBM Carbon styling (IBM Design Language: IBM Plex Sans and Carbon colors). Exact values (hex codes, font sizes, spacing) live in `style-schema.json`, which mirrors the hardcoded constants in `scripts/generate_ibm_pdf.py` for human reference.

---

## Philosophy

Clarity through simplicity. Consistent use of color and type to create a unified visual system. Every element serves a purpose -- no decoration for its own sake.

## Color Usage

- **Blue family** is the primary accent. Use for interactive elements, section markers, cover backgrounds, and emphasis.
- **Gray family** is the neutral foundation. Use for text, rules, backgrounds, and secondary information.
- **Supplementary colors** (green, red) are reserved for signal indicators only -- never for decoration.

All color tokens and hex values are defined in `style-schema.json` under `colors`.

## Typography

IBM Plex Sans is the sole typeface. Weight selection communicates hierarchy:

- **Light (300):** Display and titles -- creates visual openness
- **Regular (400):** Body text -- optimized for sustained reading
- **Medium (500):** Subheadings -- distinguishes from body without shouting
- **SemiBold (600):** Table headers and labels -- functional emphasis
- **Bold (700):** Inline emphasis only -- never for headings

Font files, weights, and family mappings are defined in `style-schema.json` under `fonts`.

## Conventions

- **Author (PDF metadata):** the `--team` value when one is passed; otherwise left empty
- **Footer (right-aligned):** "Page {N}", or "{note} · Page {N}" when `--footer-note` is passed (for example "Confidential — Internal Use Only")
- **Footer template (left-aligned):** "{title} | {date}"
- **Cover logo:** none ships with the skill; a team can drop its own SVG at `assets/logo.svg` and the cover draws it
- **No emojis** in any output
- **Sentence-case capitalization** for all text (see SKILL.md formatting rules)
