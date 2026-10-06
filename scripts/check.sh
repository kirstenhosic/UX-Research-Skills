#!/usr/bin/env bash
# Repo consistency checks. Run from anywhere:
#
#   scripts/check.sh              all checks, including rebuilding generated files
#   scripts/check.sh --no-build   skip the rebuild (fast; no python-docx/openpyxl needed)
#
# Exits non-zero if any check fails; prints one line per failure, and
# "All checks passed" at the end on success. CI runs this on every push and
# pull request (.github/workflows/checks.yml). What each check does, and why,
# is in MAINTAINING.md under "Automated checks".
#
# Runs on macOS (bash 3.2, BSD tools) and Ubuntu. Needs git, python3, zip.
set -u
cd "$(dirname "$0")/.." || exit 2
export PYTHONDONTWRITEBYTECODE=1

BUILD=1
for arg in "$@"; do
  case "$arg" in
    --no-build) BUILD=0 ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown option: $arg (try --help)" >&2; exit 2 ;;
  esac
done

FAILED=0
fail() { echo "FAIL $*"; FAILED=1; }
ok()   { echo "ok   $*"; }

SCENARIOS="analyze_your_data.md ux_plan_from_scratch.md challenge_and_refine_plan.md select_best_method.md competitive_analysis.md"

if command -v md5sum >/dev/null 2>&1; then
  md5of() { md5sum | cut -d' ' -f1; }
else
  md5of() { md5 -q; }
fi

# --- a. Shared blocks are byte-identical (MAINTAINING.md, "Shared blocks are
# duplicated on purpose"). Same extraction as the manual check(): from the line
# starting with $1 to the line starting with $2 (or EOF), across top-level *.md.
# Added beyond the manual check: every scenario file must carry the block, so a
# file that loses it entirely can't pass by silence.
block_check() {
  label=$1 start=$2 end=$3
  tmp=$(mktemp)
  for f in *.md; do
    b=$(awk -v s="$start" -v e="$end" 'index($0,s)==1{p=1} e!="" && index($0,e)==1{p=0} p' "$f")
    [ -n "$b" ] && printf '%s  %s\n' "$(printf '%s' "$b" | md5of)" "$f"
  done | sort > "$tmp"
  n=$(cut -d' ' -f1 "$tmp" | sort -u | wc -l | tr -d ' ')
  files=$(wc -l < "$tmp" | tr -d ' ')
  missing=""
  for f in $SCENARIOS; do
    grep -q "  $f\$" "$tmp" || missing="$missing $f"
  done
  if [ -n "$missing" ]; then
    fail "blocks: $label block is missing from:$missing"
  elif [ "$n" != 1 ]; then
    # Name the files that differ from the most common hash.
    common=$(cut -d' ' -f1 "$tmp" | sort | uniq -c | sort -rn | awk 'NR==1{print $2}')
    odd=$(awk -v c="$common" '$1!=c{printf " %s", $2}' "$tmp")
    fail "blocks: $label differs across files ($n variants); out of step:$odd"
  else
    ok "blocks: $label identical across $files files"
  fi
  rm -f "$tmp"
}
block_check 'OPERATING PRINCIPLES' 'OPERATING PRINCIPLES (apply throughout' 'MENTORING RULES'
block_check 'RELEASE GATE' 'RELEASE GATE (apply to every artifact' ''

# --- b. Product-context spine (MAINTAINING.md, "The product-context spine").
# Whitespace-normalized fixed-string match in each scenario file.
spine_fail=0
spine() {
  for f in $SCENARIOS; do
    if ! tr -s ' \n' ' ' < "$f" | grep -qF "$1"; then
      fail "spine: $f is missing: $1"
      spine_fail=1
    fi
  done
}
spine '[PRODUCT NAME] — [one-line description of what it does].'
spine 'Core personas include [PERSONA A], [PERSONA B], and [PERSONA C] ([what they do or manage])'
[ "$spine_fail" = 0 ] && ok "spine: product one-liner and personas sentence present in all 5 scenario files"

# --- c. Relative links and anchors.
python3 scripts/check_links.py || FAILED=1

# --- d. Count claims (readability rubric size; number of checkers).
python3 scripts/check_counts.py || FAILED=1

# --- e. Every §3 gate-matrix artifact has a row in the agent's gate table.
python3 scripts/check_gate_rows.py || FAILED=1

# --- f. Generated files are current.
GENERATED="rubrics *.skill templates/docx templates/06-participant-tracker.xlsx templates/UX-Research-Templates.zip .claude/agents .claude/skills"
if [ "$BUILD" = 1 ]; then
  build_ok=1
  log=$(mktemp)
  for step in "./build-rubrics.sh" "./build-skill.sh" "./build-claude.sh" \
              "python3 templates/build-tracker.py" "python3 templates/build-docx.py"; do
    if ! $step > "$log" 2>&1; then
      fail "generated: '$step' failed:"
      sed 's/^/       /' "$log"
      build_ok=0
    fi
  done
  rm -f "$log"
  if [ "$build_ok" = 1 ]; then
    # A rebuilt archive can be byte-different from the committed one with the
    # same content inside, purely because it was built on another platform
    # (zip entry order follows the filesystem; zlib builds vary). Compare
    # content for those and restore the committed bytes when nothing changed,
    # so only a genuinely stale file is reported.
    stale=""
    noise=""
    cmp_tmp=$(mktemp)
    while IFS= read -r line; do
      [ -z "$line" ] && continue
      st=${line:0:2}
      path=${line:3}
      case "$st:$path" in
        " M:"*.skill|" M:"*.docx|" M:"*.xlsx|" M:"*.zip)
          if git show "HEAD:$path" > "$cmp_tmp" 2>/dev/null \
             && python3 scripts/zip_same.py "$cmp_tmp" "$path"; then
            git checkout -q -- "$path"
            noise="$noise $path"
            continue
          fi ;;
      esac
      stale="$stale
       $st $path"
    done <<EOF
$(git status --porcelain -- $GENERATED)
EOF
    rm -f "$cmp_tmp"
    [ -n "$noise" ] && echo "note generated: byte-different but same content (platform zip differences), restored:$noise"
    if [ -n "$stale" ]; then
      fail "generated: these files differ from a fresh build — run the build scripts and commit the results:$stale"
    else
      ok "generated: rubrics/, *.skill, templates/docx, tracker, and bundle match a fresh build"
    fi
  fi
else
  echo "skip generated: --no-build given (CI always runs it)"
fi

echo
if [ "$FAILED" = 0 ]; then
  echo "All checks passed"
else
  echo "Some checks FAILED (see FAIL lines above)"
  exit 1
fi
