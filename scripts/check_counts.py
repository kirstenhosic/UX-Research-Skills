#!/usr/bin/env python3
"""
Check that numbers the docs state about the suite match the suite.

Deliberately narrow: a count check that cries wolf gets ignored, so each rule
only matches phrasings that unambiguously refer to the thing being counted.
When you introduce a new phrasing for one of these counts, add it here.

1. Readability rubric size. The real count is the number of numbered items
   ("N. ...") in VOICE-AND-STYLE.md "## Part 4", which must run 1..N with no
   gaps. Claims checked, whitespace-normalized so line wraps don't hide them:
     - "N-item readability rubric"                anywhere
     - "N-item rubric"                            in a sentence that mentions
                                                  readability or VOICE-AND-STYLE
     - "Score all N items" / "All N items"        anywhere in
                                                  agents/research-readability-checker.agent.md,
                                                  or in a sentence that mentions
                                                  readability or VOICE-AND-STYLE
   Context is per sentence, not per paragraph: "A guide can otherwise clear
   all 29 items above" in EVALUATION-LOOP.md §4.6 is a different rubric that
   sits in a numbered list which also names readability-checker.

2. Checker count. The real count is the number of agents/research-*.agent.md
   files. Claims checked: a spelled-out number word (one..twenty) directly
   before "checkers", "evaluators", "checker agents", "evaluator agents", or
   "separate/independent [evaluator|checker] agents". Digits are not checked
   ("5 evaluators" elsewhere means human heuristic evaluators), and a number
   word right after "plus" is a partial count and is skipped ("one pre-flight
   plus six evaluators" is seven in total).

Scans tracked and untracked-not-ignored *.md files plus CITATION.cff, except
rubrics/ (generated from EVALUATION-LOOP.md; checked at the source) and
.claude/ (generated from agents/ and skills/ by build-claude.sh).
Stdlib only. Exits 1 on any mismatch.
"""

import glob
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
NUM_WORD = r"\b(" + "|".join(WORDS) + r")"

CHECKER_CLAIM = re.compile(
    r"(?<!\bplus )" + NUM_WORD + r"\s+(?:(?:separate|independent)\s+(?:(?:evaluator|checker)\s+)?agents"
    r"|(?:evaluator|checker)\s+agents|checkers|evaluators)\b", re.I)
RUBRIC_READ = re.compile(r"\b(\d+)-item\s+readability\s+rubric\b", re.I)
RUBRIC_PLAIN = re.compile(r"\b(\d+)-item\s+rubric\b", re.I)
ALL_ITEMS = re.compile(r"\b(?:score\s+)?all\s+(\d+)\s+items\b", re.I)
READABILITY_CONTEXT = re.compile(r"readability|VOICE-AND-STYLE", re.I)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
READABILITY_AGENT = "agents/research-readability-checker.agent.md"


def scanned_files():
    try:
        out = subprocess.run(
            ["git", "ls-files", "-co", "--exclude-standard", "-z", "--", "*.md"],
            cwd=REPO, capture_output=True, check=True).stdout.decode()
        files = [f for f in out.split("\0") if f]
    except (OSError, subprocess.CalledProcessError):
        files = [os.path.relpath(p, REPO)
                 for p in glob.glob(os.path.join(REPO, "**", "*.md"), recursive=True)]
    files = [f for f in files if not f.startswith(("rubrics/", ".claude/"))]
    if os.path.isfile(os.path.join(REPO, "CITATION.cff")):
        files.append("CITATION.cff")
    return sorted(f for f in files if os.path.isfile(os.path.join(REPO, f)))


def paragraphs(text):
    """Yield (first_lineno, whitespace-normalized paragraph)."""
    start, buf = 1, []
    for i, line in enumerate(text.splitlines() + [""], 1):
        if line.strip():
            if not buf:
                start = i
            buf.append(line.strip())
        elif buf:
            yield start, " ".join(buf)
            buf = []


def rubric_size():
    path = os.path.join(REPO, "VOICE-AND-STYLE.md")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    nums, inside = [], False
    for line in lines:
        if line.startswith("## "):
            inside = line.startswith("## Part 4")
            continue
        if inside:
            m = re.match(r"^(\d+)\.\s", line)
            if m:
                nums.append(int(m.group(1)))
    if not nums:
        return None, "no numbered items found under '## Part 4' in VOICE-AND-STYLE.md"
    if nums != list(range(1, len(nums) + 1)):
        return None, "VOICE-AND-STYLE.md Part 4 items are not numbered 1..N: %s" % nums
    return len(nums), None


def main():
    fails = []
    n_items, err = rubric_size()
    if err:
        fails.append(err)
    n_checkers = len(glob.glob(os.path.join(REPO, "agents", "research-*.agent.md")))
    checker_word = WORDS[n_checkers] if n_checkers < len(WORDS) else str(n_checkers)

    rubric_claims = checker_claims = 0
    for rel in scanned_files():
        with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
            text = fh.read()
        for lineno, para in paragraphs(text):
            if n_items is not None:
                found = [int(m.group(1)) for m in RUBRIC_READ.finditer(para)]
                for sentence in SENTENCE_END.split(para):
                    if READABILITY_CONTEXT.search(sentence):
                        found += [int(m.group(1)) for m in RUBRIC_PLAIN.finditer(sentence)]
                    if rel == READABILITY_AGENT or READABILITY_CONTEXT.search(sentence):
                        found += [int(m.group(1)) for m in ALL_ITEMS.finditer(sentence)]
                for n in found:
                    rubric_claims += 1
                    if n != n_items:
                        fails.append("%s:~%d: says %d readability rubric items; "
                                     "VOICE-AND-STYLE.md Part 4 has %d"
                                     % (rel, lineno, n, n_items))
            for m in CHECKER_CLAIM.finditer(para):
                checker_claims += 1
                if m.group(1).lower() != checker_word:
                    fails.append("%s:~%d: says \"%s\"; there are %d agents/research-*.agent.md "
                                 "files (%s)" % (rel, lineno, m.group(0), n_checkers, checker_word))
    for f in fails:
        print("FAIL counts: " + f)
    if fails:
        return 1
    print("ok   counts: %d readability-rubric claims match %d items; "
          "%d checker-count claims match %d checkers"
          % (rubric_claims, n_items, checker_claims, n_checkers))
    return 0


if __name__ == "__main__":
    sys.exit(main())
