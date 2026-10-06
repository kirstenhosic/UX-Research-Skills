#!/usr/bin/env python3
"""
Check that relative Markdown links and #anchors in this repo resolve.

Scans every Markdown file git knows about (tracked, plus untracked files that
are not ignored). For each inline link [text](target), image ![alt](target),
and reference definition [label]: target, it checks:

  - the target file or directory exists, with exact case (macOS is
    case-insensitive and Linux CI is not, so a case-only mismatch fails here
    rather than only in CI);
  - a #fragment exists as a heading slug or an explicit id/name anchor in the
    target Markdown file (or in the current file for a bare #fragment).

Skipped: any target with a URL scheme (http:, https:, mailto:, ...), links in
fenced code blocks, and links inside backtick code spans. Anchors on
non-Markdown targets are not checked.

Heading slugs follow GitHub's rule: lower-case, drop every character that is
not a letter, digit, underscore, hyphen, or space, turn spaces into hyphens,
and suffix repeats with -1, -2, ...

Usage: python3 scripts/check_links.py   (from anywhere; exits 1 on failure)
Stdlib only.
"""

import os
import re
import subprocess
import sys
from urllib.parse import unquote

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
ATX = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
SETEXT = re.compile(r"^\s{0,3}(=+|-+)\s*$")
CODE_SPAN = re.compile(r"(`+)(.+?)\1", re.S)
# ](target) or ](<target>) with an optional "title"
INLINE_LINK = re.compile(
    r"\]\(\s*(<[^>\n]*>|[^\s)]+)(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)")
REF_DEF = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]*>|\S+)")
HTML_ID = re.compile(r"<[a-zA-Z][^>]*\s(?:id|name)\s*=\s*[\"']([^\"']+)[\"']")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")


def markdown_files():
    try:
        out = subprocess.run(
            ["git", "ls-files", "-co", "--exclude-standard", "-z", "--", "*.md"],
            cwd=REPO, capture_output=True, check=True).stdout.decode()
        files = [f for f in out.split("\0") if f]
    except (OSError, subprocess.CalledProcessError):
        files = []
        for root, dirs, names in os.walk(REPO):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for n in names:
                if n.endswith(".md"):
                    files.append(os.path.relpath(os.path.join(root, n), REPO))
    return sorted(f for f in files if os.path.isfile(os.path.join(REPO, f)))


def strip_inline_markup(text):
    """Approximate the rendered heading text GitHub slugs."""
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)   # links/images
    text = re.sub(r"<[^>]+>", "", text)                       # inline HTML
    text = text.replace("`", "")
    text = re.sub(r"(\*\*|__)(.+?)\1", r"\2", text)
    text = re.sub(r"(?<!\w)[*_](.+?)[*_](?!\w)", r"\1", text)
    return text


def slugify(text):
    text = strip_inline_markup(text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def split_code(lines):
    """Yield (lineno, line, in_fence) for each line."""
    fence = None
    for i, line in enumerate(lines, 1):
        m = FENCE.match(line)
        if fence is None and m:
            fence = m.group(1)[0] * len(m.group(1))
            yield i, line, True
            continue
        if fence is not None:
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) \
                    and line.strip() == m.group(1):
                fence = None
            yield i, line, True
            continue
        yield i, line, False


_anchor_cache = {}


def anchors_for(path):
    if path in _anchor_cache:
        return _anchor_cache[path]
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    seen = {}
    anchors = set()

    def add(heading):
        base = slugify(heading)
        n = seen.get(base, 0)
        anchors.add(base if n == 0 else "%s-%d" % (base, n))
        seen[base] = n + 1

    prev = None  # previous non-code line, for setext headings
    for _, line, in_code in split_code(lines):
        if in_code:
            prev = None
            continue
        for m in HTML_ID.finditer(line):
            anchors.add(m.group(1).lower())
        m = ATX.match(line)
        if m:
            add(m.group(2))
            prev = None
            continue
        s = SETEXT.match(line)
        if s and prev is not None and prev.strip() and not prev.lstrip().startswith(("|", "-", "*", ">")) \
                and not ATX.match(prev):
            add(prev.strip())
            prev = None
            continue
        prev = line
    _anchor_cache[path] = anchors
    return anchors


def exists_exact_case(abspath):
    """os.path.exists, but case-sensitive on case-insensitive filesystems."""
    if not os.path.exists(abspath):
        return False
    rel = os.path.relpath(abspath, REPO)
    if rel.startswith(".."):
        return True  # outside the repo; don't second-guess
    cur = REPO
    for part in rel.split(os.sep):
        if part in ("", "."):
            continue
        if part == "..":
            cur = os.path.dirname(cur)
            continue
        try:
            if part not in os.listdir(cur):
                return False
        except OSError:
            return False
        cur = os.path.join(cur, part)
    return True


def link_targets(lines):
    """Yield (lineno, target) for links outside code."""
    for lineno, line, in_code in split_code(lines):
        if in_code:
            continue
        # Blank out code spans, keeping length so nothing else shifts.
        clean = CODE_SPAN.sub(lambda m: " " * len(m.group(0)), line)
        if clean.count("`") % 2:
            # An unclosed span here likely closes on a later line; drop the
            # tail rather than misread code as a link.
            clean = clean[:clean.index("`")]
        for m in INLINE_LINK.finditer(clean):
            yield lineno, m.group(1)
        m = REF_DEF.match(clean)
        if m:
            yield lineno, m.group(1)


def main():
    failures = []
    files = markdown_files()
    checked = 0
    for rel in files:
        src = os.path.join(REPO, rel)
        with open(src, encoding="utf-8") as fh:
            lines = fh.read().splitlines()
        for lineno, target in link_targets(lines):
            target = target.strip("<>").strip()
            if not target or SCHEME.match(target) or target.startswith("//"):
                continue
            checked += 1
            path, _, frag = target.partition("#")
            path = unquote(path.split("?", 1)[0])
            frag = unquote(frag)
            if path:
                base = REPO if path.startswith("/") else os.path.dirname(src)
                dest = os.path.normpath(os.path.join(base, path.lstrip("/")))
                if not exists_exact_case(dest):
                    failures.append("%s:%d: broken link: %s (no such file)" % (rel, lineno, target))
                    continue
            else:
                dest = src
            if frag and dest.endswith(".md") and os.path.isfile(dest):
                if frag.lower() not in anchors_for(dest):
                    failures.append("%s:%d: broken anchor: %s (no heading or id '#%s' in %s)"
                                    % (rel, lineno, target, frag, os.path.relpath(dest, REPO)))
    for f in failures:
        print("FAIL links: " + f)
    if failures:
        return 1
    print("ok   links: %d relative links in %d Markdown files resolve" % (checked, len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
