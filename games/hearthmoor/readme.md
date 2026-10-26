# Hearthmoor

> Verified game note.

![Hearthmoor screenshot](https://raw.githubusercontent.com/darkluobo/hearthmoor/master/docs/screenshots/a1-01-fight-with-sound-1280x720.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/darkluobo/hearthmoor/blob/master/docs/screenshots/a1-01-fight-with-sound-1280x720.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/darkluobo/hearthmoor](https://github.com/darkluobo/hearthmoor)
- **Evidence:** [direct model evidence](https://github.com/darkluobo/hearthmoor/commit/31e2f28a258f04af78903a4e1232696c10e12f9e)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/darkluobo/hearthmoor/blob/master/docs/screenshots/a1-01-fight-with-sound-1280x720.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Isometric grassy river map with stone plaza and MMO HUD; tidy 2.5D look.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

炉火荒原 · 原名 ASCII Realms（2026-10-22 改名）。. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/darkluobo/hearthmoor/blob/master/apps/client/src/core/Game.ts](https://github.com/darkluobo/hearthmoor/blob/master/apps/client/src/core/Game.ts)
- [https://github.com/darkluobo/hearthmoor/commit/31e2f28a258f04af78903a4e1232696c10e12f9e](https://github.com/darkluobo/hearthmoor/commit/31e2f28a258f04af78903a4e1232696c10e12f9e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/darkluobo/hearthmoor

[Back to the awesome list](../../README.md)
