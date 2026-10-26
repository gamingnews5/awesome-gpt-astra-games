# Герои

> Verified game note.

![Герои screenshot](https://raw.githubusercontent.com/ShubbeLeontij/heroes/master/docs/boards/elementals.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/ShubbeLeontij/heroes/blob/master/docs/boards/elementals.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Python, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/ShubbeLeontij/heroes](https://github.com/ShubbeLeontij/heroes)
- **Evidence:** [direct model evidence](https://github.com/ShubbeLeontij/heroes/commit/42aed7c3182612bda4564bfd515a8067ab8596f3)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ShubbeLeontij/heroes/blob/master/docs/boards/elementals.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Board-game map and card layout on parchment; detailed but small and hard to read.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Компьютерная версия настольной игры «Герои» (Hobby World) с ИИ-игроками. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ShubbeLeontij/heroes/blob/master/heroes/web/static/js/panels.js](https://github.com/ShubbeLeontij/heroes/blob/master/heroes/web/static/js/panels.js)
- [https://github.com/ShubbeLeontij/heroes/commit/42aed7c3182612bda4564bfd515a8067ab8596f3](https://github.com/ShubbeLeontij/heroes/commit/42aed7c3182612bda4564bfd515a8067ab8596f3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/ShubbeLeontij/heroes

[Back to the awesome list](../../README.md)
