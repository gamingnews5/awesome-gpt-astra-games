# Game Rankings

> Generate these reports with `node scripts/generate-rankings.mjs --as-of=YYYY-MM-DD`.

## Current reports

- [Top games this week](this-week.md) — **10** ranked rows.
- [Top games this month](this-month.md) — **0** ranked rows.
- [Date audit data](date-audit.json) — normalized date fields for every curated game unit.

## Daily rankings

| Date | Ranked rows | Counted units | Report |
| --- | ---: | ---: | --- |
| 2026-10-21 | 0 | 0 | [Open report](daily/2026-10-21.md) |
| 2026-10-22 | 0 | 0 | [Open report](daily/2026-10-22.md) |
| 2026-10-23 | 0 | 0 | [Open report](daily/2026-10-23.md) |
| 2026-10-24 | 0 | 0 | [Open report](daily/2026-10-24.md) |
| 2026-10-25 | 0 | 0 | [Open report](daily/2026-10-25.md) |
| 2026-10-26 | 0 | 0 | [Open report](daily/2026-10-26.md) |
| 2026-10-27 | 0 | 0 | [Open report](daily/2026-10-27.md) |

## Date coverage

| Date signal | Records | Game units | Meaning |
| --- | ---: | ---: | --- |
| Explicit publication date | 152 | 287 | `published_on` |
| Publication or qualifying evidence date | 165 | 325 | `published_on`, `recent_game_evidence_on`, or `fresh_activity_date` |
| Date unknown for ranking | 3208 | 3355 | Exclude from date rankings |
| Repository creation metadata | 3373 | 3680 | Audit context only; not publication |

## Date policy

- Treat `published_on` as the preferred publication date.
- Use recent gameplay evidence or fresh repository activity only when no publication date exists, and label the basis in the report.
- Use game-creation evidence or a labeled repository-creation proxy for the seven-day weekly ranking only.
- Keep repository creation and `verified_on` dates separate from publication.
- Exclude low-quality records below the 7.0 curated-list threshold; keep them in [bad-games.md](../bad-games.md).
- Show unknown dates instead of guessing.
- Regenerate all reports after changing `games.json`.

As of: **2026-10-27**
