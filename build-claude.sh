#!/bin/sh
# Build .claude/ (Claude Code agents and skills) from agents/ and skills/.
# Generated: edit the sources, run this, commit both. See scripts/build_claude.py.
set -e
cd "$(dirname "$0")"
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_claude.py
