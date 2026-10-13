# Co-design workshop

> **Maintainer:** Kirsten Hosic · **Last reviewed:** 2026-10 · **Status:** draft
>
> Format: [`../METHODS.md`](../METHODS.md). Shared question rules: `EVALUATION-LOOP.md` §4.6.
> Session design: `EVALUATION-LOOP.md` §4.11 and [`../workshop_design.md`](../workshop_design.md).

**Gating — three gates, three different objects.** This is research with external
participants, run as a group, so it touches more of the loop than any other
method here. The **study plan** goes to `research-plan-reviewer` (§4.1): research
questions, who is recruited and why, consent. The **session plan** goes to
`research-workshop-checker` (§4.11), which reads the group design, and here every
board is external and every customer in the room is a participant. Any
**one-to-one segment** goes to `research-guide-checker` (§4.6) on its own. Don't
send the whole thing to one gate; each refuses the others' objects by name.

**One sentence:** Customers or design partners work alongside the team in a
facilitated group session, making things (maps, rankings, sketches) that show
how they think about a problem, so the team learns their framing rather than
testing its own.

## What it can tell you

- How participants frame the problem: their categories, their vocabulary, and
  what they put first, made visible in the artifacts they build. Making
  externalizes thinking that saying alone often doesn't (Sanders & Stappers)
- What they prioritize when they have to trade one thing against another, among
  peers who face the same constraints
- Where participants from different roles or accounts agree and where they split.
  Differences surface when people work side by side on the same artifact
- What the team's own model is missing: whatever participants add to the board
  that the team didn't put there
- Directions worth testing, as candidates

## What it cannot tell you

Use this verbatim in the plan's methodology section.

- **What any one participant does.** It is a group, and groups converge: on the
  most senior customer in the room, the most articulate one, or the first idea on
  the board. For individual behavior, interview or observe.
- **How widespread anything is.** A session holds 6 to 10 people from a few
  accounts, chosen partly for their willingness to co-design. They are
  enthusiasts, not a sample. And the outputs of one group are one data point, not
  several, however many sticky notes they produced.
- **Whether they would adopt what they designed.** People value what they helped
  make more than an equivalent they didn't (the IKEA effect; Norton, Mochon &
  Ariely, 2012). A co-designed concept arrives with its makers already attached
  to it.
- **Anything about people who weren't in the room**, most of all the daily user
  when the room was configurers, or the reverse.

**Every finding from this method is labeled as group-generated in the readout,**
and every design that came out of it is labeled a candidate, not a validated
direction.

## Session shape

| Section | Time (3 hours) | Purpose |
|---|---|---|
| Welcome, consent, norms | 15 min | Recording, what happens to their ideas, who sees what, and what the team will not do: no roadmap answers in the room |
| Individual warm-up | 15 min | Each person maps the last time they did the thing, alone. This is the only individual-level data the session produces |
| Share in small groups | 20 min | Groups of 3–4, each person walks through their own map |
| Group making task 1 | 40 min | Map, sort, or rank, as a group |
| Break | 10 min | |
| Group making task 2 | 40 min | Sketch or assemble, from a kit of parts |
| Private reflection | 10 min | Each person ranks or comments alone, so the group's answer can be compared with what each thinks |
| Close | 10 min | What happens to their input next, and when they will hear back |

Pre-session sensitizing (a short individual workbook in the week before) makes
the warm-up richer. Sanders & Stappers describe it; it is optional, and worth it
when participants haven't thought about the topic recently.

## Counts

Rule of thumb. Assumes a 3-hour session with participants who have done the work
being studied.

| Session length | Participants | Group making tasks |
|---|---|---|
| 2 hours | 6–8 | 1 |
| 3 hours | 6–10, in groups of 3–4 | 2 |
| Full day | not recommended remotely | 3, with a long break |

More than two group tasks in three hours leaves no time for the talk about the
artifacts, and an artifact without its narration can't be interpreted afterwards.

## Instrument craft

**Individual before group, and keep the individual artifacts.** The warm-up map
is the one place each person's own account exists before the group bends it.
Collect it separately, labeled with the participant ID.

**Give them a toolkit, not your prototype.** Blank maps, component cards, and
open frames. Showing the team's design turns the session into a concept test with
a group's worth of conformity on top; if that is what you need, use
[`concept-test.md`](concept-test.md) one to one.

**The team observes and does not make.** No designer sketches on a participant's
behalf, and no engineer corrects what a participant assumes the system does. Both
replace the participant's model with the team's, which is the thing you came to
learn.

**Script the answer to "will you build this?"** Someone will ask. Write the reply
before the day, along the lines of: "We're here to learn how you think about it,
not to decide. We'll tell you what we heard and what we did with it." The
participant summary skills own what that later message can say.

**Customers from different companies see each other's work.** Where the product
touches infrastructure, security, or anything a customer treats as confidential,
that is not a formality: one account's architecture or incident details on a
shared board are confidential to that account. Decide before the session
whether groups mix accounts, tell participants what others will see, and get
consent for that specifically. When in doubt, group by account.

**Record the talk about the artifacts, not only the artifacts.** With consent,
capture what participants say while they make and present. A photo of a map with
no narration is uninterpretable a week later.

**Consent covers more than an interview's.** Recording; who sees the artifacts;
cross-participant visibility; quote use; and what happens to the ideas
themselves. Ownership of ideas that come out of a co-design session is a legal
question, not a research one. Flag it to whoever owns customer agreements before
the session, not after.

## Sample size

Two or three sessions per segment, as a rule of thumb, and treat each session's
group outputs as one unit. The individual warm-up artifacts can be counted per
person; the group artifacts cannot.

## Logistics

- **Compensation.** Many customer organizations don't let staff accept it.
  Check, and offer what the participant can accept, such as early access or a
  summary of what was learned.
- **design partner agreements**, where they exist, usually cover confidentiality
  and participation terms. Check them before inviting anyone.
- **Remote.** A prepared board with one frame per person for the individual work,
  and tested access. Shorter blocks than in person.
- **Keep it separate from internal decision workshops.** Partners can't negotiate
  trade-offs honestly in front of customers, and customers hear a brainstorm as a
  promise.

## Analysis note

Analyze the artifacts together with the narration. Code the individual warm-up
artifacts separately from the group ones: the first are individual accounts, the
second are consensus records. Compare each person's private reflection with the
group's output; where they diverge, the group converged, and the private view is
usually the better evidence.

## Common failure

The readout says "customers designed X," and the roadmap treats that as demand.
It was a handful of enthusiasts, in a group, designing a thing they now feel
ownership of. Write the finding so it can't be read that way, and test the
candidate with people who didn't make it.
