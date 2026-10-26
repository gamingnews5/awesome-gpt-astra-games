# Schwarzerpeter

> Verified game note.

![Schwarzerpeter screenshot](https://raw.githubusercontent.com/GrowingRui/SchwarzerPeter/main/docs/images/alpine-deck.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/GrowingRui/SchwarzerPeter/blob/main/docs/images/alpine-deck.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/GrowingRui/SchwarzerPeter](https://github.com/GrowingRui/SchwarzerPeter)
- **Evidence:** [direct model evidence](https://github.com/GrowingRui/SchwarzerPeter/commit/fc2c48937f482807c8c5e1f3252e7cf26c332f6a)
- **Live demo:** [open demo](https://schwarzerpeter.vercel.app)
- **Additional live link:** [open demo](https://schwarzerpeter.vercel.app/play)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/GrowingRui/SchwarzerPeter/blob/main/docs/images/alpine-deck.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Grid of illustrated animal cards on dark felt; coherent card art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The classic card game from Germany and Switzerland, now online. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GrowingRui/SchwarzerPeter/blob/main/apps/web/src/cards.js](https://github.com/GrowingRui/SchwarzerPeter/blob/main/apps/web/src/cards.js)
- [https://github.com/GrowingRui/SchwarzerPeter/commit/fc2c48937f482807c8c5e1f3252e7cf26c332f6a](https://github.com/GrowingRui/SchwarzerPeter/commit/fc2c48937f482807c8c5e1f3252e7cf26c332f6a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/GrowingRui/SchwarzerPeter

[Back to the awesome list](../../README.md)
