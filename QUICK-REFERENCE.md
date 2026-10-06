# Dr. Morgan — quick reference

One page for using the suite. The full guide is [`README.md`](README.md).

---

## Start

1. **Give it your product.** A file in [`product-context/`](product-context/), the
   `PRODUCT CONTEXT` block in the agent, or answer Dr. Morgan's five questions.
2. **Start Dr. Morgan** and say what you're working on in a sentence. In Claude
   in VS Code, open the repo folder and type **`/dr-morgan`**, or just say
   "Start Dr. Morgan". In other tools, select the Dr. Morgan agent by name.
3. **Swap names, emails, and phone numbers for P1, P2…** before you paste anything.

Every reply opens with a status line, like `Dr. Morgan · Scenario A · Draft mode
· Verification: synthesis ✅ · readability ⏳ pending`. No status line means
you're talking to the plain assistant, not Dr. Morgan.

## Which checker, when

Drafts get checked before anyone else sees them. **The safety checker always runs
first**, then these, in order:

| What Dr. Morgan drafted | Checkers after safety |
|---|---|
| Research plan | plan reviewer → readability |
| Plan with a discussion guide | plan reviewer → guide checker → readability |
| Discussion guide on its own | guide checker → readability |
| Plan with a survey | plan reviewer → survey checker → readability |
| Survey on its own | survey checker → readability |
| Findings | synthesis → significance → readability |
| Competitive analysis | synthesis → significance → readability |
| Readout deck, findings report, participant email, participant card | synthesis → readability |

You don't have to remember this. Dr. Morgan tells you which one is next.

## How to run a checker

- **If your tool lets Dr. Morgan launch agents**, it runs them itself and shows
  you each result.
- **Otherwise it gives you a checker packet.** Open a **new chat**, load the
  checker it names, paste the packet, and attach the original transcripts or
  notes if the packet lists them. Bring the result back to Dr. Morgan.
- **Always a new chat.** A checker opened inside Dr. Morgan's conversation can
  read the whole thing, so it's no longer an independent check.
- **Read the top of the result:** *What this means for you* says whether it's
  ready, the one thing to fix, and what happens next.

## When to start a new chat with Dr. Morgan

Long conversations quietly get worse. Watch for:

- a quote that's *close to* your transcript but not exact (the one to worry about)
- Dr. Morgan asking for something you already gave it
- a count or a theme that's drifted from what you agreed

Good moments to move on: after you've decided on the themes, after a checker's
verdict, when you switch to a different kind of task, and **before** you paste a
big batch of transcripts. Say **"handoff"** and Dr. Morgan writes a short summary
to paste into the new chat. Re-attach your transcripts there; the summary doesn't
carry them, on purpose.

## Your calls

| When | What Dr. Morgan asks | A good answer |
|---|---|---|
| Before the study | Four quick questions for whoever owns the decision | Short answers, or "don't know" |
| After it groups your data into themes | Keep, change, split, or drop each theme | "Keep 1, 2 and 4, drop 3, split 5 into…" |
| After the checks pass | Give it a full read and change what you'd say differently | "Done, no changes" or "Done, reworded slide 4" |

Passing the checks isn't approval. The output goes out under your name, so the
full read is the step that matters most.
