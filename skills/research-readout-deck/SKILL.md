---
name: research-readout-deck
description: >-
  Render a clean, easy-to-digest readout slide deck (.pptx) from synthesized
  findings records — the output of a completed analysis (Scenario A) — for a
  product team. Use this whenever someone wants to present, share, or "write
  up" research findings as slides, build a UXR readout or research share-out,
  or summarize what users said for PMs, engineers, and designers. Trigger on
  phrases like "research readout," "findings deck," "share out my study," "turn
  these notes into slides," "UXR presentation," or "make a deck from this
  research," even when the word "skill" isn't used — including requests that
  arrive with only raw notes, transcripts, or a prose summary. Take those too,
  but recommend running the analysis first and say what the shortcut costs; a
  notes-built deck cannot match one built on a full analysis. The deck follows
  a findings-first narrative arc and is built for a mixed product-team audience
  (PM + Eng + UXD).
---

# Research Readout Deck

Build a research readout: a slide deck that takes a product team from "what
question did we ask" to "here's what we learned and what we should do about it,"
fast and without making them dig. The audience is a mixed product team, so the
deck has to land for three readers at once: PMs want the answer and the
recommendations, engineers want the specifics and the feasibility signals, and
designers want the interaction-level detail. Write for all three by leading with
the decision-relevant takeaway and keeping the evidence one layer down.

This skill owns the *content and narrative*. It hands the actual `.pptx`
mechanics (rendering, layout, QA) to the **pptx** skill.

> **Prerequisite — the `pptx` skill.** This skill does not render slides on its
> own; it produces the structure, narrative, and content rules, then delegates
> generation and visual QA to the separate **pptx** skill. Read this file first
> for the structure, then read the pptx skill before generating any slides. If
> the pptx skill isn't available in your environment, you can still use this file
> to plan the deck's content and narrative — just flag that the actual `.pptx`
> build needs it.

## When you're invoked

There are two ways this goes, and they produce different decks.

**The good path:** you're handed a set of **findings records** that have already
been through synthesis. Each one carries its own evidence, exact counts,
confidence, and limits. Your job is then selection and arrangement — pick the
findings that carry the story, impose the narrative, build the slides. You are
not deciding what the study found.

**The degraded path:** you're handed raw notes, transcripts, or a prose summary
and asked to make the deck. You can do this, and sometimes it's the only option.
But say once, plainly, what it costs — because synthesizing *while* building
slides is exactly where readouts go wrong. A quote gets tightened to fit a text
box. A "4 of 8" softens into "most." A hedge gets dropped because the line
scanned better without it. Recommend running synthesis first — not as a
formality, but because a notes-built deck cannot reach the quality of one built
on a full analysis, and this skill exists for the records-first case. If the
user wants to proceed anyway, proceed — then flag every inference you had to
make, by name, at the end, and say how far the deck can travel (below).

## Step 1 — Start from findings records

### The record shape

A findings record is the unit this deck renders from. If you have the UX
Research Skills repo, `FINDINGS-CONTRACT.md` is the full spec and governs. The
minimum shape — all this skill needs to build from — is:

```
FINDING F1
  statement:      one finding, at insight level where the evidence reaches it
  rq:             the research question it answers, or UNMAPPED
  prevalence:     exact counts — "5 of 8", never "most"
  scope:          product · persona · the conditions they were under
  evidence:       >=1 verbatim quote or observed behavior, each with a
                  participant ID and a locatable source
  disconfirming:  what contradicts this — or "none found" / "not sought"
  confidence:     high / medium / low, and why
  limits:         what this finding does not apply to
  recommendation: optional as a whole — but if it reaches a slide it carries
                  action, owner, depends_on (the finding IDs it rests on),
                  horizon (this-quarter / direction-of-travel), confidence,
                  alternatives_considered, and reverses_if
  telling_detail: the concrete specific that could only have come from being
                  in the room (optional; use it when it's there)
  artifact_ref:   the screen, flow, or state this happened on (optional)
```

### The rendering rule

**Render only what a record contains.** This is the point of the whole file.

If a slide needs a quote, the quote has to already be in a record. If it isn't,
the deck can't produce it — and the gap becomes visible instead of getting
filled. Concretely:

- Every claim on a slide carries its finding ID — on the slide face, or in the
  speaker notes if that would clutter it
- A quote on a slide matches its record's quote exactly, character for character
- A number on a slide matches `prevalence`. "5 of 8" never becomes "most"
- `confidence` and `limits` appear somewhere for every finding you show
- Anything on a slide with no matching record is a defect, not a style choice

### Validate before you build

Run this before writing a single slide. It takes a minute and it catches the
failure this skill exists to prevent.

1. **Do records exist?** If not, you're on the degraded path — say so, then
   follow it.
2. **Does each record you plan to use carry the minimum fields?** `statement`,
   at least one sourced verbatim `evidence` entry, exact `prevalence`, `scope`
   (product + persona), `rq`, and a `participant_type` on every evidence entry.
   A record missing any of those isn't a finding, it's a recollection. Don't
   build a slide on it. `participant_type` matters on a slide specifically:
   a quote from an internal colleague reporting on customers reads as a
   customer quote once it is set in 28pt beside a photo, and the record is the
   only place that distinction survives.
3. **Is `destination` declared** — `internal-team`, `internal-org`, or
   `external`? Put it on the title slide and in the filename. Forwarding is how
   this material actually travels, and a deck that doesn't say where it was
   meant to go can't warn the person who forwards it. Ask; don't guess.
4. **Are there more findings than slide budget?** Usually yes, and that's
   normal. Choose. Don't compress all of them onto crowded slides.

If a record fails check 2, report the gap to the user by finding ID and ask.
Never fill it in yourself.

### Then gather the deck-specific context

The records tell you what the study found. They don't tell you these — collect
them separately, and ask once rather than inventing anything.

**About the study (for the title + methodology):**
- Product / feature name and a one-line description of what was tested
- Study type(s): interviews, survey, usability test, diary study, etc.
- Sample: how many participants, what segments (e.g. enterprise vs. SMB),
  experience levels, recruiting source, and any limitations
- Contributors and roles (UX Research, PM, UXD, Eng) and the date
- Optional: a link/location for the full research doc

**About the framing:**
- The decision or question that prompted the research — the deck leads with this
- Which findings the user considers the headline, if they have a view

**About delivery:**
- Theme: **default to the USWDS palette** — white content slides,
  `primary-darker` anchors, a single `primary` blue accent, Public Sans type
  (the palette below). Only swap the palette if the user requires a different
  brand, and keep the same discipline when you do
- Any hard constraints (must-include sections). The deck targets **~15 slides**
  by default — see the slide budget in Step 3
- Screenshots of the tested UI (screens, states, flows, the artifact under test) — ask for these if the study touched an interface and none came with the findings; most usability readouts should be screenshot-led

### The degraded path — no records, just notes

When the user says "here are my notes, make the deck," don't refuse and don't
pretend it's equivalent. Do this instead:

1. **Say once what's missing and why it matters.** Three fields cannot be
   recovered at deck-build time, because each one requires having swept the
   whole corpus: `disconfirming` (what contradicts this finding), `limits` (what
   it doesn't apply to), and `confidence` (how much weight it bears). A deck
   built from notes will simply not have them, and their absence is invisible on
   a slide — which is precisely what makes it dangerous. Recommend running the
   analysis first (Scenario A); this path exists for the deadline, not as an
   alternative of equal standing.
2. **If they'd rather proceed, proceed.** A useful deck today beats a rigorous
   one that never gets built.
3. **Then reconstruct records as you go.** For each finding you put on a slide,
   write the record — even a partial one — and show the user. Mark what you
   inferred versus what the notes actually say. This is slower than freehanding
   slides and it is the entire safeguard.
4. **State your assumptions inline at the end**, not buried in a slide ("I
   treated X as the headline finding; nothing in the notes gave me a
   participant count for the onboarding issue, so that slide says 'multiple
   participants' and should be corrected before you present it").
5. **Say how far this deck can travel.** Every deck faces the safety scan and
   `research-synthesis-checker` in deck mode before it ships. Records
   reconstructed from notes — marked inferred, `disconfirming: not sought` —
   are honest, and that honesty draws flags: workable for an `internal-team`
   readout, where flags ride along as Reviewer Notes, and the wrong foundation
   for anything headed `internal-org` or `external`, where deck mode starts
   blocking. If the deck is going beyond the team, say so now: that is the
   moment to stop and run the analysis, because that is the version that
   passes clean.

## Step 2 — Separate observation, interpretation, and recommendation

This is the discipline that makes a readout trustworthy. For every finding,
keep three things distinct:

- **Observation** — what users actually did or said (evidence: n, %, quote).
- **Interpretation** — what you think it means, marked as your read.
- **Recommendation** — what the team should do about it.

The example deck does this explicitly: data on the left, an *Interpretation*
block underneath, recommendations collected separately. Preserve that
separation. Don't smuggle an interpretation in as if it were an observation,
and don't state a recommendation without the finding it rests on.

Also calibrate strength of evidence. "13 of 16 described it as very useful" is
representative; one participant's offhand comment is anecdotal. Say which is
which. If a claim is thin, label it ("early signal," "worth validating").

## Step 3 — Impose the narrative arc

Use this order. It's findings-first: the team gets the answer before the
evidence, then the evidence backs it up, then the full backlog, then next
steps. Skip sections that don't apply; don't pad. Detailed slide-by-slide
recipes (layouts, what goes where) live in
[references/deck-structure.md](references/deck-structure.md) — read it before
building.

**Slide budget — keep it to ~15.** A readout should be skimmable, so target
**no more than 15 slides**. A large multi-method study may run a little over, but
stay tight — never pad to fill space. With that budget, the *spine* is: Title,
Summary, Recommendations shortlist, one Methodology, Findings summary, the 4-6
strongest evidence slides, one synthesis statement, What's next, and the Full
recommendations list. The first things to cut or merge when you're over budget:
a standalone Agenda, Context slides, redundant per-participant slides (keep the
2-3 that carry the story), standalone quote slides (fold the quote into the
evidence slide instead), and the Appendix. A tight spine beats completeness.

1. **Title** — feature name, "UX Research Findings & Recommendations," contributors + roles, date, optional link.
2. **Agenda** — the sections below, so readers can orient.
3. **(Optional) Context** — current vs. new state, or what was tested, with a screenshot or two.
4. **Summary** — three columns: *what went well* / *where it can evolve* / *how we move forward*. Lead with the single headline stat or takeaway.
5. **Recommendations (shortlist)** — the 3-6 that matter most, numbered, key phrase bolded.
6. **Section divider → Findings**, then for each method:
   - **Methodology** ("Who we spoke to" / "Who participated"): n, segments, cadence, limitations. Brief — not the rationale for why the method was chosen.
   - **Findings (summary)** for that method — the numbered takeaways.
   - **Evidence**, shaped to the method:
     - **Usability testing** (a primary method here): task-by-task results
       (completion, where people got stuck, severity-rated issues), the observed
       behavior behind each issue, and a verbatim quote that captures it. Lead
       with the issue and its severity, not the task number.
     - **Interviews** (the other primary method): per-participant deep-dives
       (User type / Primary use case / Unmet needs), themed 3-column
       finding+interpretation slides, and synthesis statements.
     - **Survey or other quant**: ratings tables and ranked lists.
7. **Quote slides** — interspersed throughout, not clustered. One verbatim quote, large, attributed by role/segment.
8. **Synthesis statements** — occasional full-bleed single-insight slides that name the throughline ("The root of their challenges lies with X").
9. **What's next** — roadmap, owners, timing; tie findings to upcoming work.
10. **Full list of recommendations & feature requests** — the complete backlog, numbered, can span slides.
11. **Thanks**, then **Appendix** — reference documents / links.

## Step 4 — Write slides for a mixed audience

- **Show, don't describe — use screenshots.** This is a usability-heavy team,
  and a readout about an interface should *show* that interface. Whenever a
  finding is about a specific screen, flow, state, or artifact, put the actual
  screenshot on the slide and annotate it (a callout, an arrow, a circle on the
  spot where people struggled) rather than describing the UI in prose. Screens
  anchor context slides, per-participant/per-task slides, issue slides, and
  before/after comparisons. Ask the user for screenshots up front if the
  findings reference the UI and none were provided — a tree test or notes-only
  study may legitimately have none, but most usability readouts should be
  screenshot-led. Crop tight to the relevant area and keep annotations in the
  accent color. A record's `artifact_ref` tells you which screen a finding
  happened on — use it to pick the right screenshot instead of guessing.
- **One idea per slide.** A slide title should be a *claim*, not a topic.
  "Users struggle to build complex queries" beats "Query building."
- **Lead with the takeaway, support with evidence.** Big stat or one-line
  insight up top; detail below.
- **Keep the detail that proves someone was there.** A record's
  `telling_detail` — the participant who kept a cheat sheet in a text file, the
  sticky note on the monitor — is the strongest signal in the deck that this
  came from real sessions and not a summary of a summary. It survives the trip
  to the slide. Don't sand it off for being specific; specific is the point.
- **Quotes earn their place.** Use them to make a finding human, not to fill
  space. Verbatim from the record, attributed, anonymized. **Render verbatim and
  paraphrase differently so no one mistakes one for the other:** a verbatim quote
  is a blockquote — quotation marks, italic, an accent bar down the side; a
  paraphrase is upright, no quotation marks, visibly not a quote. Never set a
  paraphrase in quotation marks, and never blur the two into one style. The
  `participant_type` distinction rides here too: a customer's own words and an
  internal SME reporting on customers must not read the same on the slide.
- **The finding title and the quote must read as different things.** On a finding
  slide the claim (the title) is the largest text — bold, upright, `ink`,
  sitting at the top under its kicker and accent rule. The quote sits lower,
  smaller, italic, set off by the accent bar. That visual gap is what lets a
  skimming reader tell your finding from the participant's words at a glance;
  never let a title and a quote share size, weight, and color, and never stack a
  quote where the title should be. The evidence supports the claim — it doesn't
  impersonate it.
- **Make recommendations actionable and mapped.** Each rec shows the finding IDs
  from its `depends_on` and the owner from its record. Prioritize; don't dump.
  **The owner renders as a team or role — Design, PM, Eng — never a person's
  name.** Drop parenthetical name tags ("(via Alex)") and any on-slide owner-name
  label: on a slide that is a redaction leak, not attribution.
- **Label the horizon.** A `direction-of-travel` recommendation on a slide next
  to a `this-quarter` one, with nothing distinguishing them, is how a direction
  becomes a commitment in the room. Render the label.
- **Respect the three readers.** Where a finding has engineering or design
  implications, name them — feasibility notes for eng, interaction detail for
  design, impact/priority for PM.
- **Plain language, everywhere the reader looks.** Write the slide face and the
  speaker notes the way you'd explain the finding to a colleague at their desk —
  short, common words over formal ones (*use* not *utilize*, *about* not
  *regarding*, *start* not *commence*), one idea per line, contractions fine.
  Spell out jargon and internal acronyms the first time; a readout often travels
  beyond the room. This isn't a style preference — it's scored: the
  `research-readability-checker` gate flags formal or academic register against
  VOICE item 23 (plain language) on both the slide copy and the notes, so a deck
  that reads like a journal paragraph comes back before release.

### What goes on the slide vs. what goes in the notes

The slide face is for the customer's reality; the study's machinery goes in the
speaker notes. This is the discipline that decides how a readout reads to the
room, and it's four separate calls:

- **State findings as customer facts, not as study process.** The slide says what
  the customer does, wants, or runs into — "Customers manage clusters they can't
  see in one place," not "Interviews surfaced a visibility theme" or "In 5 of 7
  sessions we heard…". Research-process framing describes *your* work, not the
  reader's takeaway; it belongs on the methodology slide and in the notes, never
  in a finding's headline. (This is `VOICE-AND-STYLE.md` Part 3's method-note rule,
  applied to a slide.)
- **Scope the copy to the segment, on the slide.** Write "This segment…",
  "Operators running many live clusters…" — never a bare universal "Customers
  want…" the sample can't carry. The record's `scope` is the source; the slide
  copy has to honor it, because a scope buried in a notes line reads as a universal
  claim on the slide. A finding true of one persona is still a finding — label it.
- **Keep weakening language off the slide face; keep the limit in the record.**
  Confidence and limits are required for every finding — but they live in the
  record and speaker notes, and the slide face stays neutral. Self-deprecating
  evidence words ("sparse," "thin," "only one session," "not a finding yet,"
  "reported, not verbatim") make the data read weaker than the record says it is,
  so they don't go on the slide. **Destination decides how far this goes:** on an
  **`internal-team`** deck — the room that sat in the sessions — the weak-signal
  qualifier can be dropped from the deck entirely, because the record still carries
  it and everyone reading already knows the sample. On **`internal-org`** or
  **`external`** it must appear, on the slide or a clearly-marked notes line; a
  finding shown to people who weren't there, without its limit, overstates itself.
  Never drop a finding's confidence or scope from the *record* — the carve-out is
  about the slide face, not the finding.
- **Surface the product's value, backed by evidence.** A readout that only lists
  problems misrepresents the study as much as one that only lists wins. Where the
  evidence shows the product already delivering — the capability the segment
  values, the workaround they built *because* they want the thing — put it on the
  slide (the Summary's "what went well" column, the opportunity or throughline
  slide). This is not both-sidesing: don't bolt a compensating positive onto every
  criticism. It's showing the real shape of what you found, value included, each
  claim sourced to a finding like any other.

## Step 5 — Build the deck (delegate to pptx)

Read the **pptx** skill now and follow it to generate the `.pptx`. Key things
to carry over:

- **Findings-first, claim-titled slides**, per the structure above.
- **Screenshots of the tested UI**, annotated, on the context, per-task/
  participant, and issue slides — see Step 4. If you have screens, lead with them.
- **Section dividers** use a full-color background with a single short phrase —
  these set the rhythm of the deck and separate Interviews / Survey / What's next.
- **Quote slides** are deliberately sparse: one large centered quote, attribution
  small beneath it. Verbatim quotes carry the blockquote treatment (marks, italic,
  accent bar); a paraphrase is set upright without marks (see Step 4).
- **Speaker notes open with "What this slide means."** Every slide's notes lead
  with one plain-language line explaining the slide the way you'd explain it to a
  colleague at their desk, so someone reading the deck async — who wasn't in the
  room and can't hear you present — still gets it. The notes are also where the
  method detail, the provenance (customer-reported vs. SME's own view), and any
  weak-signal qualifier kept off the slide face (Step 4) actually live.
- **Data tables** (survey ratings) get a clean three-column treatment:
  statement / number (with SD if you have it) / plain-language reading.
- Honor the pptx skill's anti-patterns: no accent stripes or underlines under
  titles, no text-only filler slides, strong contrast, no overflow. Every slide
  needs a visual element (stat callout, icon, chart, screenshot, or quote mark).

### Theme — USWDS palette (Public Sans / `primary` blue on white)

Use the **U.S. Web Design System (USWDS) palette with Public Sans**: light and
grid-disciplined — predominantly **white (`#FFFFFF`)** content slides with crisp
`ink` type (`#1B1B1B`), a single **`primary` blue (`#005EA2`)** accent, and
**`primary-darker` (`#162E51`)** dark anchors for title, dividers, and closing
slides (with white type and an **`accent-cool` (`#00BDE3`)** accent on those
dark slides). Flat color only (no gradients, shadows, glows, or rounded-corner
gimmicks); lead with type hierarchy and whitespace, left-aligned to a grid.
Typography is **Public Sans** (Public Sans for headings, body, data, and
small-caps meta labels; Public Sans Light for big titles and large statements;
Public Sans Light Italic for pull quotes; Roboto Mono only where data or a table
needs a monospace), falling back to a clean grotesque (Helvetica Neue / Arial) if
Public Sans is unavailable — never a serif.

Whatever palette the deck uses, keep the same discipline: one dark anchor, one
accent, light content backgrounds, AA contrast. For another brand, swap in that
brand's palette (its primary color as the accent) and hold everything else.

**Keep the organization's logo on every slide for an internal readout.** An
internal-use deck (destination `internal-team` / `internal-org`) carries
**your organization's logo** as a small, consistent corner mark on every slide,
white on the dark title/divider/closing slides and dark on the light content
slides. It signals provenance to colleagues who forward or re-open the file. For
an `external` deck, follow whatever brand and co-marketing rules the destination
requires instead. The mark is a fixed corner element; it does not count as the
slide's one accent.

**The full USWDS color-token palette (hex values + per-role usage), the status
colors, and the every-slide aesthetic guardrails live in
[references/deck-structure.md](references/deck-structure.md) — read it before
building, and enforce the guardrails again in QA (Step 6).**

## Step 6 — QA the content, not just the pixels

Run the pptx skill's visual QA (subagents, overflow check). On top of that,
check the *content*:

**First, a record-fidelity pass — no net-new data.** Before anything else, go
slide by slide and verify that every piece of information traces back to a
findings record (or, on the degraded path, to the source material the user
provided). The deck may only *select, restructure, and interpret* what it was
given — it must never introduce data that isn't there.

Check each slide against its record:

- **Every claim maps to a finding ID.** A claim with no record behind it is
  blocking. Cut it or flag the gap; do not source it from your own reasoning.
- **Every quote byte-matches its record.** Read them side by side. Tightening a
  quote to fit the text box is the single most common way a readout becomes
  untrue, and it never feels like fabrication while you're doing it.
- **Every number matches `prevalence` exactly.** "5 of 8" is "5 of 8." Not
  "most," not "the majority," not "~60%."
- **`confidence` and `limits` are stated for every finding shown** — in the
  record and speaker notes always, and on the slide or a clearly-marked notes line
  for an `internal-org` or `external` deck. On an `internal-team` deck the
  weak-signal qualifier may sit in the notes or be left off the deck (Step 4's
  destination carve-out); the record still carries it. A finding shown to people
  who weren't in the room, without its limit, reads as stronger than it is.
- **Recommendations on slides carry the owner, the `depends_on` finding IDs, and
  the `horizon` label** from their record. The owner is a team or role, never a
  person's name (Step 4). A recommendation whose `depends_on` is
  empty is **blocking** — it did not come from the research, and a readout slide
  is the worst place to imply it did. `alternatives_considered` and `reverses_if`
  belong in speaker notes or the appendix rather than the slide, but they ship
  with the deck: they are what the room will ask for.
- **Findings read as customer facts, scoped to their segment.** No slide headline
  frames a finding as study process ("interviews showed…") or as a universal
  ("Customers want…") the record's `scope` doesn't support (Step 4).
- **Verbatim and paraphrase are visually distinct**, and no paraphrase sits in
  quotation marks (Step 4).
- **Every slide's speaker notes open with a plain-language "What this slide means"
  line** (Step 5).

Then confirm the rest:

- **Every number, stat, percentage, and count** (participant n, completion
  rates, ratings, SDs, "13 of 16") appears in or is directly computed from the
  source. No invented or "rounded-up" figures. If you computed a percentage from
  raw counts, the counts must be in the source.
- **Every quote** is verbatim from the source and attributed exactly as the
  source supports — no paraphrase in quotation marks, no fabricated or composite
  quotes, no invented attributions.
- **Every finding, theme, and observation** is grounded in something a user
  actually did or said in the source — not plausible-sounding filler.
- **Interpretations and recommendations are clearly marked as such** and rest on
  a cited finding; they are the *only* place your own reasoning may appear, and
  they must never be presented as measured results.
- **Names, segments, roles, dates, product details, and methodology facts**
  (sample size, cadence, limitations) match the source exactly.

If a slide needs something the source doesn't cover, do **not** invent it:
either cut it, or flag the gap explicitly to the user ("the source didn't
include a completion rate for task 3"). When in doubt, leave it out. Treat any
unverifiable claim as a defect to fix before declaring done.

- Does every finding have evidence behind it? Any unsupported claims?
- Is observation kept separate from interpretation and recommendation?
- Are all quotes verbatim and attributed? No invented quotes?
- Do the recommendations map back to findings?
- Does the summary actually capture the deck (could someone read only it)?
- Are sample size and limitations stated honestly?

Then re-check the **aesthetic guardrails** (in
[references/deck-structure.md](references/deck-structure.md)) on every slide:

- Is the deck **≤ 15 slides** (or only slightly over for a large study)?
- Any text running off-slide, clipped, or touching an edge? Any overflow?
- Does every text/background pair pass AA contrast? No light-slide accent as text
  on a dark fill, no `warning` yellow as text, no gray-on-gray?
- One accent per slide (`primary` on light, `accent-cool` on `primary-darker`),
  light backgrounds dominant, `primary-darker` anchors?
- Public Sans throughout (Roboto Mono only for data that needs a monospace);
  images keeping their proportions inside the margins?

Fix content and layout gaps before declaring done. If you had to assume something the
source didn't cover, surface it to the user rather than burying it in a slide.

## Step 7 — You are not the last check

Your QA pass is the producer checking their own work, which is worth doing and
is not independent. If you're running inside the UX Research Skills suite, the
deck still goes through its gates before it's shared — `research-safety-checker`
first, including speaker notes, then `research-synthesis-checker` in deck mode
(re-verifying every slide against the findings records), then
`research-readability-checker`. `EVALUATION-LOOP.md` has the sequence and the
verdict schema.

Two things to hand off cleanly:

- **The record set you rendered from**, so the deck gate can check slides
  against records rather than re-reading transcripts.
- **The declared destination**, so the safety scan applies the right bar.

Screenshots and embedded file metadata can't be machine-checked. List them for
the user by slide number and say plainly that the deck isn't cleared until a
person has looked at them.

Whatever the gates say, the deck is a draft until the researcher signs off:
they read every slide and every speaker note, make their own edits, and the
sign-off is recorded (§11 of `EVALUATION-LOOP.md` has the block). The deck is
presented under their name, not a gate's. An edit of theirs that moves a
quote, a count, or an attribution re-runs the synthesis gate first.

Outside the suite, the same principle holds in a lighter form: before this deck
gets presented, someone who didn't build it should read it against the source.

## A note on honesty

A readout's value is that the team can trust it. Don't round a "somewhat agree"
into a "strongly agree," don't promote one comment to "users say," and don't
present an interpretation as a measured result. When the data is thin or mixed,
say so on the slide. An honest "we're not sure yet, here's the early signal" is
more useful to a product team than false confidence.
