*Dr. Morgan UX research suite — author: **Kirsten Hosic**, UX Research Strategy Lead, Security Product Design. MIT licensed.*

---

# Research readout deck

Findings-first slides for a mixed PM, Eng, and Design room. The deck renders
only what exists in passed [findings records](07-findings-record.md); a
slide that needs a quote needs the quote to already be in a record. §4.4 of
`EVALUATION-LOOP.md` is the Definition of Done, and
`skills/research-readout-deck` carries slide-by-slide recipes.

**Slide budget: ~15.** A readout should be skimmable. The spine when you are
at budget: Title, Summary, Recommendations shortlist, one Methodology,
Findings summary, the 4–6 strongest evidence slides, one synthesis
statement, What's next, Full recommendations list. First cuts when over:
standalone Agenda, Context slides, redundant per-participant slides, and
standalone quote slides (fold the quote into its evidence slide).

## The arc

1. **Title** — feature name, "UX Research Findings & Recommendations,"
   contributors and roles, date.
2. **Agenda** — optional at budget.
3. **Context** (optional) — current vs new state, or what was tested, with a
   screenshot or two.
4. **Summary** — three columns: what went well / where it can evolve / how
   we move forward. Lead with the single headline stat or takeaway.
5. **Recommendations shortlist** — the 3–6 that matter most, numbered, key
   phrase bolded.
6. **Findings, per method:**
   - **Methodology** ("Who participated"): n, segments, cadence,
     limitations. State participant type plainly (external SMEs are
     disclosed as "external SME participants, not actual customers"). This is
     the one slide where method belongs — elsewhere, state findings as
     customer facts, not as what the study did. A finding's `confidence` and
     `limits` stay in the record and speaker notes always; on an
     `internal-team` deck a weak-signal qualifier may sit in the notes or be
     left off the deck, but on an `internal-org` or `external` deck it must
     appear on the slide or a marked notes line.
   - **Findings summary** — the numbered takeaways for that method.
   - **Evidence slides**, shaped to the method:
     - Usability: task-by-task results (completion, where people got stuck,
       severity-rated issues), the observed behavior behind each issue, and
       a verbatim quote. Lead with the issue and severity, not the task
       number.
     - Interviews: per-participant deep-dives (user type / primary use case
     / unmet needs), themed finding-plus-interpretation slides, synthesis
       statements.
     - Survey or quant: ratings tables and ranked lists, with exact ns.
7. **Quote slides** — interspersed, not clustered. One verbatim quote,
   large, attributed by role or segment (P-IDs or segment labels; never
   identity).
8. **Synthesis statement** — an occasional full-bleed single-insight slide
   naming the throughline.
9. **What's next** — roadmap, owners, timing; tie findings to upcoming
   work.
10. **Full recommendations and feature requests** — the complete numbered
    backlog; can span slides.
11. **Thanks**, then **Appendix** — reference documents and links.

## Craft notes

- Keep observation, interpretation, and recommendation visually and
  verbally separate; the room must be able to tell what was seen from what
  you concluded.
- **Findings read as customer facts, scoped to their segment.** State what
  the customer does, wants, or faces — not "interviews showed…". Scope the
  copy to the sample: "This segment…", "operators running many live
  clusters…", never a universal "Customers want…" the sample can't support.
- Exact counts on every claim ("5 of 8"), never "most."
- **Order findings by the story and number them in that order.** F1 → F2 → F3
  is presentation order, not analysis order; re-order and you renumber, updating
  every cross-reference (summary slide, next-steps tags, follow-up links, notes)
  so no F# points at the wrong finding.
- **Verbatim and paraphrase render differently.** A verbatim quote is a
  blockquote — quotation marks, italic, an accent bar; a paraphrase is
  upright, no quotation marks, visibly not a quote, attribution small
  beneath. Never set a paraphrase in quotation marks.
- **Title, claim, and quote read as different layers.** On a finding slide the
  title (the claim) is the largest, boldest, upright text; the quote sits lower,
  smaller, italic, behind the accent bar. A skim should tell your finding from
  the participant's words by size and weight alone.
- **Recommendation and workstream owners are teams or roles** — Design, PM,
  Eng — never a person's name. Drop parenthetical name tags ("(via David)")
  and on-slide owner-name labels.
- **Every slide's speaker notes open with `WHAT THIS SLIDE MEANS`** — a
  plain-language gloss for the async reader who wasn't in the room. The
  notes also carry method, provenance, and any qualifier dropped from an
  `internal-team` slide face.
- **Plain language on the slide face and in the notes** — everyday words over
  formal ones, jargon and acronyms spelled out; the `research-readability-checker`
  gate scores it (VOICE item 23).
- Visual weight tracks evidence strength; the strongest finding is not the
  smallest slide.
- Surface the product's value where a finding supports it — sourced to the
  evidence, not a soft positive bolted on to balance every gap.
- **Internal decks keep your organization's logo on every slide** — a small corner
  mark, white on dark slides, dark on light, marking provenance for anyone who
  forwards the file.
- Theme: SLM Portfolio palette (Aptos, deep-navy anchors, teal accent, pale-blue
  content slides) by default; IBM Carbon (IBM Plex, Blue 60) for IBM-branded decks.

## Before release

Gates, then the release sign-off (§11): read every slide, make your own
edits, and re-run the synthesis check if an edit moves a quote, count, or
attribution. After release, offer participants the
[impact message](10-participant-impact-message.md).

---

*Part of the Dr. Morgan UX research suite. Manual alternative to
`skills/research-readout-deck`; §4.4 applies either way.*
