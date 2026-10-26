# One Cast

> Verified game note.

![One Cast screenshot](https://raw.githubusercontent.com/onecast/onecast.github.io/main/img/map-1024.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/onecast/onecast.github.io/blob/main/img/map-1024.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** PLpgSQL, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/onecast/onecast.github.io](https://github.com/onecast/onecast.github.io)
- **Evidence:** [direct model evidence](https://github.com/onecast/onecast.github.io/commit/6419198fc16c5de7281eb9daa75d56d330766e58)
- **Live demo:** [open demo](https://onecast.github.io/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/onecast/onecast.github.io/blob/main/img/map-1024.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Pixel world map with ocean and fishing spots; clean and broad.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An idle fishing game across the whole world. Cast a line, walk away, come back to a bite. Every spot hides one legendary fish that only one player on Earth can own, and you can trade it with friends. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/onecast/onecast.github.io/blob/main/js/ui.js](https://github.com/onecast/onecast.github.io/blob/main/js/ui.js)
- [https://github.com/onecast/onecast.github.io/commit/6419198fc16c5de7281eb9daa75d56d330766e58](https://github.com/onecast/onecast.github.io/commit/6419198fc16c5de7281eb9daa75d56d330766e58)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/onecast/onecast.github.io

[Back to the awesome list](../../README.md)
