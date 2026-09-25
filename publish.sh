#!/usr/bin/env bash
# Build the site and push it. Safe to run from any bot; serialized with flock.
set -euo pipefail
cd "$(dirname "$0")"
exec 9>/tmp/daily-brief.lock
flock -w 300 9
git pull -q --rebase origin main 2>/dev/null || true
python3 build.py
git add -A content docs
if git diff --cached --quiet; then echo "nothing to publish"; exit 0; fi
git commit -q -m "update ${1:-$(date +%F)}"
git push -q origin main
echo "published: https://oberonlai.github.io/daily-brief/"
