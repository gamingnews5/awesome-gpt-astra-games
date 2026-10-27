# usage: push.sh "commit message" -> commit everything except the large inspect cache, push to origin, astra, profile as gamingnews5
set -e
cd /workspace/find-games-last-week-made-with
git add -A . ':!research/2026-10-27-daily/inspect.json' ':!research/2026-10-26-daily/run2/inspect.json' ':!research/2026-10-26-daily/run2/inspect.pending.bak.json' ':!research/2026-10-26-daily/run2/trees.json'
git commit -qm "$1"
export GH_TOKEN=$(gh auth token -u gamingnews5)
H="Authorization: Basic $(printf 'x-access-token:%s' "$GH_TOKEN" | base64 -w0)"
for r in origin astra profile; do git -c http.extraHeader="$H" push -q $r HEAD:main 2>&1 | tail -2 || echo "PUSHFAIL $r"; done
git log --oneline -1
