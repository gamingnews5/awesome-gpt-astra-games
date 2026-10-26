set -e
cd /workspace/find-games-last-week-made-with
node scripts/validate-games.mjs | tail -1
node scripts/generate-game-notes.mjs >/dev/null
node scripts/generate-rankings.mjs >/dev/null
node scripts/generate-awesome-readme.mjs >/dev/null
node scripts/generate-organization-profile.mjs >/dev/null
node scripts/validate-games.mjs | tail -1
