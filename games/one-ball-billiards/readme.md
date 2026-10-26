# One-Ball Billiards

> Verified game note.

![One-Ball Billiards screenshot](https://raw.githubusercontent.com/bederson/learn-to-code/main/docs/screenshot.png)

## At a glance

- **Score:** 6.8/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/bederson/learn-to-code/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/bederson/learn-to-code](https://github.com/bederson/learn-to-code)
- **Evidence:** [direct model evidence](https://github.com/bederson/learn-to-code/commit/3d5728319fc9125971916b233250c39ed0d03278)
- **Live demo:** [open demo](https://bederson.github.io/learn-to-code/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/bederson/learn-to-code/blob/main/docs/screenshot.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Plain green billiards table with one ball and aim line; minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A simple billiards game you play in your web browser. Pull back, let go, and watch the ball roll, bounce off the cushions and drop into the pockets. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bederson/learn-to-code/blob/main/src/main.ts](https://github.com/bederson/learn-to-code/blob/main/src/main.ts)
- [https://github.com/bederson/learn-to-code/commit/3d5728319fc9125971916b233250c39ed0d03278](https://github.com/bederson/learn-to-code/commit/3d5728319fc9125971916b233250c39ed0d03278)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/bederson/learn-to-code

[Back to the awesome list](../../README.md)
