# Candy Wall

> Verified game note.

![Candy Wall screenshot](https://raw.githubusercontent.com/etwilliams/candy-wall/main/docs/gameplay.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/etwilliams/candy-wall/blob/main/docs/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/etwilliams/candy-wall](https://github.com/etwilliams/candy-wall)
- **Evidence:** [direct model evidence](https://github.com/etwilliams/candy-wall/commit/bcc8c6db4593d500e92f4b4cde5e4feeb466d4c3)
- **Live demo:** [open demo](https://etwilliams.github.io/candy-wall/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/etwilliams/candy-wall/blob/main/docs/gameplay.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Breakout wall of colourful candy bricks with score; bright and clear.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

It's a wall of candy. A canvas breakout game with 8-bit looks and sound, built with Vite. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/etwilliams/candy-wall/blob/main/src/main.js](https://github.com/etwilliams/candy-wall/blob/main/src/main.js)
- [https://github.com/etwilliams/candy-wall/commit/bcc8c6db4593d500e92f4b4cde5e4feeb466d4c3](https://github.com/etwilliams/candy-wall/commit/bcc8c6db4593d500e92f4b4cde5e4feeb466d4c3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/etwilliams/candy-wall

[Back to the awesome list](../../README.md)
