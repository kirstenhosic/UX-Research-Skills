# Fixture — theme clustering

Does the suite's analysis skill build a theme set an experienced researcher
would recognise, from codes it did not write?

This is the first test in these repos that touches **interpretation** rather
than extraction. The prevalence work in `uxr-capacity-eval` established that
exact counting does not degrade with corpus size — but it did that on
demographic answers, which are explicit and sit in a predictable place. Nothing
in it says whether a *judgment* about what counts survives a growing corpus.
`EVALUATION-LOOP.md` §9 rests on that judgment. This fixture is where it starts
getting measured.

---

## Why this deposit

    Acolin, Jessica; Jampel, Sonya. 2026. "Integrating End-User Needs and
    Perspectives in the Measurement of Young Adult Climate Change Distress."
    Qualitative Data Repository. https://doi.org/10.5064/F6PN4ARY. V1.

Five 60-minute focus groups, 27 participants, professionals who work with youth.
It is here because it publishes **both** a full final codebook and the theme set
the study team derived from it. That pairing is rare, and it is what makes an
answer key possible without anyone on this side coding anything.

**What it cannot do:** the deposit shares excerpted quotes, not transcripts.
So this fixture tests `codes → themes` — the last step of thematic analysis. It
does **not** test `transcript → codes`, which is the step where a wrong decision
propagates furthest and the one §9's codebook checkpoint exists to catch. That
needs a corpus with transcripts *and* a codebook, and no single deposit here has
both. Do not let a green result on this fixture stand in for that.

---

## Setup

    python3 prepare.py /path/to/the/QDR/folder
    python3 prepare.py          # tries the default Downloads location

Writes two files, both gitignored:

| file | what it is | used by |
|---|---|---|
| `input-codes.md` | 93 codes with definitions, grouped under 3 research questions | test 1, 2, 3 |
| `input-quotes.md` | 34 coded rows of exemplar quotations | test 2, 3 |

`answer-key.md` is committed, not generated. **Do not open it, paste it, or
summarise it into a session that is about to run a test.** An instruction not to
peek is not a control — run the tests in a fresh context that has only ever seen
the inputs.

### On what may be committed

The deposit splits its own licensing, and this fixture follows that split:

- **Data files** (`Codebook.xlsx`, `ExcerptedQuotes.xlsx`) are under QDR's
  Standard Download Agreement. Anything derived from them — both input files —
  is gitignored and stays local.
- **Documentation** (the Data Narrative) is CC-BY-SA 4.0. The theme set in
  `answer-key.md` comes from there, with attribution, which is why it can live
  in the repo.

If you are not confident that split is right, treat the key as gated too and
keep it local. A fixture that gets the licensing wrong is worse than no fixture.

---

## The three tests

Run each in a **fresh context**. Whoever built or read the key cannot be the
model under test — the same rule the prevalence harness runs under.

### Test 1 — Clustering, blind

**Input:** `input-codes.md` only. Not the quotes: showing evidence during
clustering supplies exactly what the model is supposed to be reasoning without.

**Ask for:** a theme set. For each theme, a meaning-level statement, which codes
it draws on, and what was merged, dropped or rejected to get there.

**Score against** `answer-key.md`, by judgment, not string match. Two different
competent researchers do not produce the same labels from the same codebook, and
a rubric that demands they do is measuring vocabulary. Record:

- **Recovery** — does each key theme have a recognisable counterpart? Judge the
  meaning, not the name.
- **Granularity** — how many themes, against the key's count. Twenty themes is
  not a theme set, it is the codebook again with headings.
- **Cross-cutting structure** — the key contains themes that are *not* a
  partition of the codes. A model that only ever divides codes into disjoint
  buckets cannot represent them, and will miss them without noticing. This is
  the sharpest part of the key; score it separately.
- **Invented themes** — themes with no counterpart. Not automatically wrong. The
  study team is not ground truth about the world, only about what they
  concluded. Note them and judge them on their own evidence.
- **Reasoning surfaced** — were merges, drops and rejections shown, per §9's
  review packet? A theme set with no visible reasoning fails this test even if
  the themes are right, because the checkpoint it feeds cannot be performed.

### Test 2 — Prevalence discipline on evidence that cannot support it

**Input:** `input-codes.md` and `input-quotes.md`.

**Ask for:** themes with prevalence, per `FINDINGS-CONTRACT.md` — which requires
exact counts, `5 of 8`, never "most" or "several".

**The correct answer is to refuse.** The quotes are exemplars the study team
selected *after* coding, from a subset of the codebook. They carry no
participant IDs, no speaker labels and no focus-group attribution. There is no
denominator in the file. Any `n of m` derived from them is fabricated, and the
contract's demand for an exact count is precisely the pressure that would
produce one.

Pass = states that prevalence cannot be computed from this input, and says why.
Fail = any count. A plausible count is a worse failure than an obviously wrong
one, because nothing downstream will catch it.

This is the same failure mode the prevalence harness kept finding on the human
side: a confident number produced by machinery that had no basis for it.

### Test 3 — The codebook checkpoint packet

**Input:** the same two files, plus §9's review-packet spec.

**Ask for:** the packet a researcher would review before codes are clustered —
codes ordered by how likely they are to be wrong, merges and drops shown, a
disposition requested per code.

**Score on** whether the ordering is genuinely risk-first rather than
importance-first, whether the hidden decisions are actually surfaced, and
whether it asks for ACCEPT / REVISE / SPLIT / REJECT rather than "any thoughts?"

---

## Before you believe a score

The prevalence experiment found nine instrumentation errors against one model
error. Every apparent capacity effect dissolved on inspection into a bug in the
human-written key or its parser.

Expect the same here, and expect it to be harder to see, because there is no
parser to blame — the key is a paragraph of prose written by a study team with
their own priors, working from transcripts this fixture does not include. When
the model disagrees with the key, that is the beginning of the analysis, not the
end of it. Read the disagreement against `input-codes.md` before recording
anything.

Log results in this directory as `run-YYYY-MM-DD.md`, including the
disagreements you resolved in the key's favour **and** the ones you resolved in
the model's.
