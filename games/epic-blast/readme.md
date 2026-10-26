# EPIC BLAST

> Verified game note.

![EPIC BLAST screenshot](https://raw.githubusercontent.com/felixwahner/epic-blast/main/docs/screenshots/storm-citadel.webp)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/felixwahner/epic-blast/blob/main/docs/screenshots/storm-citadel.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, PixiJS, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/felixwahner/epic-blast](https://github.com/felixwahner/epic-blast)
- **Evidence:** [direct model evidence](https://github.com/felixwahner/epic-blast/commit/e1df31c76680f12833b07f3d72d8a0e3de92b75d)
- **Live demo:** [open demo](https://www.o315.de/epic-blast)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/felixwahner/epic-blast/blob/main/docs/screenshots/storm-citadel.webp) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Block puzzle board with neon city backdrop and combo score; polished and readable.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Block Blast–style puzzle game for the browser, built with TypeScript, Pixi.js 7 and Vite. You drag pieces onto an 8×8 board and clear full rows and columns. It has neon "jewel" blocks, 19 themed worlds to collect, a combo system, revives, a recorded stadium… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/felixwahner/epic-blast/blob/main/src/game/game.ts](https://github.com/felixwahner/epic-blast/blob/main/src/game/game.ts)
- [https://github.com/felixwahner/epic-blast/commit/e1df31c76680f12833b07f3d72d8a0e3de92b75d](https://github.com/felixwahner/epic-blast/commit/e1df31c76680f12833b07f3d72d8a0e3de92b75d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/felixwahner/epic-blast

[Back to the awesome list](../../README.md)
