# Migdal games

> Verified game note.

![Migdal games screenshot placeholder](migdal-games-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/eyals/migdal-games](https://github.com/eyals/migdal-games)
- **Evidence:** [direct model evidence](https://github.com/eyals/migdal-games/commit/261742cfc213cc04177b4271d7e50dbc5a9a553c)
- **Live demo:** [open demo](https://migdal-quiz.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Family games. Each game lives in its own folder and is deployed as its own Vercel project (Root Directory = the folder). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/eyals/migdal-games/blob/main/quiz/app/page.tsx](https://github.com/eyals/migdal-games/blob/main/quiz/app/page.tsx)
- [https://github.com/eyals/migdal-games/commit/261742cfc213cc04177b4271d7e50dbc5a9a553c](https://github.com/eyals/migdal-games/commit/261742cfc213cc04177b4271d7e50dbc5a9a553c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/eyals/migdal-games

[Back to the awesome list](../../README.md)
