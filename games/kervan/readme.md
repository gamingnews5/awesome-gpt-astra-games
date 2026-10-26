# Kervan

> Verified game note.

![Kervan screenshot](https://raw.githubusercontent.com/kdrgny-dev/kervan/main/docs/design/stage4/mockups/hero_select.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 6.5/10 ([manually reviewed image](https://github.com/kdrgny-dev/kervan/blob/main/docs/design/stage4/mockups/hero_select.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/kdrgny-dev/kervan](https://github.com/kdrgny-dev/kervan)
- **Evidence:** [direct model evidence](https://github.com/kdrgny-dev/kervan/commit/b38b5c2b7e4cd0b46cb859fe7713f4c6e2b54727)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/kdrgny-dev/kervan/blob/main/docs/design/stage4/mockups/hero_select.png) — 📸 6.5/10 · manual visual review · Use this frame for the game-level score. Hero-select screen with four illustrated character cards and stats; polished mobile UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Nimble Quest tarzı snake + otomatik savaş roguelite (Phaser + Tauri). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kdrgny-dev/kervan/blob/main/src/scenes/GameScene.ts](https://github.com/kdrgny-dev/kervan/blob/main/src/scenes/GameScene.ts)
- [https://github.com/kdrgny-dev/kervan/commit/b38b5c2b7e4cd0b46cb859fe7713f4c6e2b54727](https://github.com/kdrgny-dev/kervan/commit/b38b5c2b7e4cd0b46cb859fe7713f4c6e2b54727)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/kdrgny-dev/kervan

[Back to the awesome list](../../README.md)
