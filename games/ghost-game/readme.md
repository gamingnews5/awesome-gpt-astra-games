# Ghost Game

> Verified game note.

![Ghost Game screenshot](https://raw.githubusercontent.com/alexmbrown/ghost-game/main/public/ui/crest_demons.webp)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 3.2/10 ([manually reviewed image](https://github.com/alexmbrown/ghost-game/blob/main/public/ui/crest_demons.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/alexmbrown/ghost-game](https://github.com/alexmbrown/ghost-game)
- **Evidence:** [direct model evidence](https://github.com/alexmbrown/ghost-game/commit/53cf7cf69e9f5334f0592db44fc3c77c5411cf86)
- **Live demo:** [open demo](https://alexmbrown.github.io/ghost-game/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/alexmbrown/ghost-game/blob/main/public/ui/crest_demons.webp) — 📸 3.2/10 · manual visual review · Use this frame for the game-level score. Devil shield logo on magenta; icon only.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D, browser-based party game inspired by Google's Halloween Doodle. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/alexmbrown/ghost-game/blob/main/src/game/core/engine.ts](https://github.com/alexmbrown/ghost-game/blob/main/src/game/core/engine.ts)
- [https://github.com/alexmbrown/ghost-game/commit/53cf7cf69e9f5334f0592db44fc3c77c5411cf86](https://github.com/alexmbrown/ghost-game/commit/53cf7cf69e9f5334f0592db44fc3c77c5411cf86)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/alexmbrown/ghost-game

[Back to the awesome list](../../README.md)
