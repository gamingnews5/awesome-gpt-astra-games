# Operation Blueprint: AI Edition

> Verified game note.

![Operation Blueprint: AI Edition screenshot](https://raw.githubusercontent.com/alokomkar/Blue/main/docs/img/bunker-dark.jpg)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/alokomkar/Blue/blob/main/docs/img/bunker-dark.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/alokomkar/Blue](https://github.com/alokomkar/Blue)
- **Evidence:** [direct model evidence](https://github.com/alokomkar/Blue/commit/6a5c6c4380db2209659b02f63ae8d06013ce0f5a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/alokomkar/Blue/blob/main/docs/img/bunker-dark.jpg) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Dim 3D corridor with glowing blueprint table and objective HUD; moody.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D heist game for meta hackathon. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/alokomkar/Blue/blob/main/src/client/game.ts](https://github.com/alokomkar/Blue/blob/main/src/client/game.ts)
- [https://github.com/alokomkar/Blue/commit/6a5c6c4380db2209659b02f63ae8d06013ce0f5a](https://github.com/alokomkar/Blue/commit/6a5c6c4380db2209659b02f63ae8d06013ce0f5a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/alokomkar/Blue

[Back to the awesome list](../../README.md)
