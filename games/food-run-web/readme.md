# Food Run (web)

> Verified game note.

![Food Run (web) screenshot placeholder](food-run-web-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/yeledpele/food-run](https://github.com/yeledpele/food-run)
- **Evidence:** [direct model evidence](https://github.com/yeledpele/food-run/commit/7e95ca6d8312d98d0f637e12156ae59ffa21b03b)
- **Live demo:** [open demo](https://yeledpele.github.io/food-run/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Food Run - a PICO-8 style platformer in the browser, with a sprite and level editor. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/yeledpele/food-run/blob/main/public/js/game.js](https://github.com/yeledpele/food-run/blob/main/public/js/game.js)
- [https://github.com/yeledpele/food-run/commit/7e95ca6d8312d98d0f637e12156ae59ffa21b03b](https://github.com/yeledpele/food-run/commit/7e95ca6d8312d98d0f637e12156ae59ffa21b03b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/yeledpele/food-run

[Back to the awesome list](../../README.md)
