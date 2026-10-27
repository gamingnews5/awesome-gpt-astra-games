# TheCoffeeSixSense

> Verified game note.

![TheCoffeeSixSense screenshot](https://raw.githubusercontent.com/phamdinhthanhcntt6/NewGame/dev/docs/screenshots/m1-idle.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/phamdinhthanhcntt6/NewGame/blob/dev/docs/screenshots/m1-idle.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/phamdinhthanhcntt6/NewGame](https://github.com/phamdinhthanhcntt6/NewGame)
- **Evidence:** [direct model evidence](https://github.com/phamdinhthanhcntt6/NewGame/commit/53488fb06c1410782ef71cffce7b655fce9fdea1)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/phamdinhthanhcntt6/NewGame/blob/dev/docs/screenshots/m1-idle.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Isometric placeholder blocks on a tiled board with debug text; early prototype.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

2.5D isometric coffee farming + café management game (Phaser 4, TypeScript, Vite). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/phamdinhthanhcntt6/NewGame/blob/dev/src/gameplay/cafe/CafeService.ts](https://github.com/phamdinhthanhcntt6/NewGame/blob/dev/src/gameplay/cafe/CafeService.ts)
- [https://github.com/phamdinhthanhcntt6/NewGame/commit/53488fb06c1410782ef71cffce7b655fce9fdea1](https://github.com/phamdinhthanhcntt6/NewGame/commit/53488fb06c1410782ef71cffce7b655fce9fdea1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/phamdinhthanhcntt6/NewGame

[Back to the awesome list](../../README.md)
