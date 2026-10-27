# Ratland Defense

> Verified game note.

![Ratland Defense screenshot](https://raw.githubusercontent.com/MisterRat/Ratland-Defense/main/screenshots/gameplay.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/MisterRat/Ratland-Defense/blob/main/screenshots/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/MisterRat/Ratland-Defense](https://github.com/MisterRat/Ratland-Defense)
- **Evidence:** [direct model evidence](https://github.com/MisterRat/Ratland-Defense/commit/b87193ab7c6e50793e7c3afbfb0e1730c52fb11a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/MisterRat/Ratland-Defense/blob/main/screenshots/gameplay.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Top-down tower-defense path on grass with towers and dense side panels; clear but busy UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

In a tower defense game, enemies walk along a fixed path from a spawn point to your base. You can't move the enemies — you can only stop them by building towers on the tiles around the path. Towers shoot (or slow, burn, poison) enemies for as long as they're… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/MisterRat/Ratland-Defense/blob/main/js/ui.js](https://github.com/MisterRat/Ratland-Defense/blob/main/js/ui.js)
- [https://github.com/MisterRat/Ratland-Defense/commit/b87193ab7c6e50793e7c3afbfb0e1730c52fb11a](https://github.com/MisterRat/Ratland-Defense/commit/b87193ab7c6e50793e7c3afbfb0e1730c52fb11a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/MisterRat/Ratland-Defense

[Back to the awesome list](../../README.md)
