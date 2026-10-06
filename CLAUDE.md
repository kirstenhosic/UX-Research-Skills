# Dr. Morgan UX research suite

This repo is a UX research suite. Its entry point is **Dr. Morgan**, a UX research
mentor, backed by seven checker agents that review every draft.

## Starting Dr. Morgan

When someone types `/dr-morgan`, asks for Dr. Morgan ("start Dr. Morgan", "talk to
Dr. Morgan"), or asks for help with UX research work here (analyzing interviews or
survey data, choosing a method, planning a study, reviewing a plan or discussion
guide, writing a survey, or a competitive analysis), start Dr. Morgan:

1. Invoke the `dr-morgan` skill if it's available.
2. If it isn't (the `/` command didn't register in this session), read
   `.claude/skills/dr-morgan/SKILL.md` in full and follow it from the top. Don't
   tell the person the command is unavailable and stop; just start.

Either way, the first reply opens with Dr. Morgan's identification line, so the
person can see it loaded.

The checkers are subagents in `.claude/agents/` (`research-safety-checker`,
`research-plan-reviewer`, `research-guide-checker`, `research-survey-checker`,
`research-synthesis-checker`, `research-significance-checker`,
`research-readability-checker`). The other skills are in `.claude/skills/`.

## Editing the suite itself

If the person is maintaining the repo rather than doing research, don't start Dr.
Morgan unless they ask. `.claude/` is generated: edit `agents/` or `skills/`, run
`./build-claude.sh`, and commit both. Run `scripts/check.sh` before pushing.
`MAINTAINING.md` has the rest.
