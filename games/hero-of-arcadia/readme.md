# Hero of Arcadia

> Verified game note.

![Hero of Arcadia screenshot](https://raw.githubusercontent.com/bhimio1/hero-of-arcadia/main/docs/screenshots/combat-preview.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/bhimio1/hero-of-arcadia/blob/main/docs/screenshots/combat-preview.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/bhimio1/hero-of-arcadia](https://github.com/bhimio1/hero-of-arcadia)
- **Evidence:** [direct model evidence](https://github.com/bhimio1/hero-of-arcadia/commit/b35c7f51d5480fcfbc2081fd11ec04e3489f319d)
- **Live demo:** [open demo](https://bhimio1.github.io/hero-of-arcadia/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/bhimio1/hero-of-arcadia/blob/main/docs/screenshots/combat-preview.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Pixel tactics map with river and unit stat panels; clear retro strategy look.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A retro pixel-art, turn-based tactics game for the browser and desktop. Lead the Cobalt. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bhimio1/hero-of-arcadia/blob/main/src/game/scenes/BattleScene.ts](https://github.com/bhimio1/hero-of-arcadia/blob/main/src/game/scenes/BattleScene.ts)
- [https://github.com/bhimio1/hero-of-arcadia/commit/b35c7f51d5480fcfbc2081fd11ec04e3489f319d](https://github.com/bhimio1/hero-of-arcadia/commit/b35c7f51d5480fcfbc2081fd11ec04e3489f319d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/bhimio1/hero-of-arcadia

[Back to the awesome list](../../README.md)
