# Takeoff: Reign Version

> Verified game note.

![Takeoff: Reign Version screenshot](https://raw.githubusercontent.com/damienlethiec/takeoff-reign-version/main/docs/screenshots/phone-03-card.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/damienlethiec/takeoff-reign-version/blob/main/docs/screenshots/phone-03-card.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/damienlethiec/takeoff-reign-version](https://github.com/damienlethiec/takeoff-reign-version)
- **Evidence:** [direct model evidence](https://github.com/damienlethiec/takeoff-reign-version/commit/cc49fe4ca1f73a4ab8235ca1898bf08324c93a74)
- **Live demo:** [open demo](https://damienlethiec.github.io/takeoff-reign-version/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/damienlethiec/takeoff-reign-version/blob/main/docs/screenshots/phone-03-card.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Swipe-card character prompt on phone layout; readable but plain.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A short, replayable swipe game about AI governance. You are the EU's AI Envoy: people bring you requests one at a time, and you answer left or right. Every answer moves the world, on the same gauges as Takeoff: Middle Power v3: AI power (the clock),… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/damienlethiec/takeoff-reign-version/blob/main/src/data/cards/requests.ts](https://github.com/damienlethiec/takeoff-reign-version/blob/main/src/data/cards/requests.ts)
- [https://github.com/damienlethiec/takeoff-reign-version/commit/cc49fe4ca1f73a4ab8235ca1898bf08324c93a74](https://github.com/damienlethiec/takeoff-reign-version/commit/cc49fe4ca1f73a4ab8235ca1898bf08324c93a74)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/damienlethiec/takeoff-reign-version

[Back to the awesome list](../../README.md)
