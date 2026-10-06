#!/usr/bin/env python3
"""
Check that every artifact in the EVALUATION-LOOP.md §3 gate matrix has a row
in the gate table of agents/dr-morgan.agent.md.

Source rows: the first table headed "| Artifact |" in the "## 3." section of
EVALUATION-LOOP.md,
rows starting "| **" (artifact name in bold in the first cell). "Theme set"
is skipped: it is a human checkpoint, not an agent gate.

Agent rows: the first table headed "| Artifact |" in the "### Which gates
run" section of agents/dr-morgan.agent.md, first cell of each body row.

Names are compared after normalizing: lower-case, parenthetical asides
dropped, "on its own" treated as "standalone", punctuation collapsed. So
"Findings report" matches "Findings report (written)", and "Survey
instrument, standalone" matches "Survey instrument, on its own".

Only checks one direction (matrix -> agent). Gate *order* is not compared:
the two tables name gates differently (`plan-reviewer` vs
`research-plan-reviewer`) and the agent adds mode notes; read them by eye.
Stdlib only. Exits 1 if any row is missing.
"""

import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {"theme set"}


def norm(name):
    s = name.lower()
    s = re.sub(r"\([^)]*\)", " ", s)
    s = s.replace("on its own", "standalone")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return s.strip()


def table_after(path, heading_re):
    """First table whose header's first cell is "Artifact", inside the section
    that starts at the heading matching heading_re (up to the next heading of
    the same or a higher level). Subsections inside it are searched too, so
    the table can move within the section without breaking the check."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    for i, line in enumerate(lines):
        if re.match(heading_re, line):
            level = len(line) - len(line.lstrip("#"))
            break
    else:
        return None
    tables, cur = [], []
    for line in lines[i + 1:] + [""]:
        m = re.match(r"^(#+)\s", line)
        if m and len(m.group(1)) <= level:
            break
        if line.startswith("|"):
            cur.append(line)
            continue
        if cur:
            tables.append(cur)
            cur = []
    if cur:
        tables.append(cur)
    for t in tables:
        if first_cell(t[0]).lower() == "artifact":
            return t
    return None


def first_cell(row):
    return row.strip().strip("|").split("|")[0].strip()


def main():
    src = os.path.join(REPO, "EVALUATION-LOOP.md")
    agent = os.path.join(REPO, "agents", "dr-morgan.agent.md")
    matrix = table_after(src, r"^## 3\.")
    gates = table_after(agent, r"^#+ Which gates run")
    if not matrix:
        print("FAIL gate-rows: no table headed '| Artifact |' in the '## 3.' section of EVALUATION-LOOP.md")
        return 1
    if not gates:
        print("FAIL gate-rows: no table headed '| Artifact |' in the 'Which gates run' section of agents/dr-morgan.agent.md")
        return 1

    wanted = []
    for row in matrix:
        if row.startswith("| **"):
            name = first_cell(row).replace("**", "").strip()
            if norm(name) not in SKIP:
                wanted.append(name)
    have = {norm(first_cell(r)) for r in gates[2:]}  # skip header + separator

    missing = [w for w in wanted if norm(w) not in have]
    for m in missing:
        print("FAIL gate-rows: EVALUATION-LOOP.md §3 artifact \"%s\" has no row in the "
              "'Which gates run' table of agents/dr-morgan.agent.md" % m)
    if missing:
        return 1
    print("ok   gate-rows: all %d §3 gate-matrix artifacts have a row in agents/dr-morgan.agent.md"
          % len(wanted))
    return 0


if __name__ == "__main__":
    sys.exit(main())
