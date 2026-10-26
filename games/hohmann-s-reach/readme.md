# Hohmann's Reach

> Verified game note.

![Hohmann's Reach screenshot](https://raw.githubusercontent.com/JonasMerrell/space-rts/master/assets/preview/bodies.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/JonasMerrell/space-rts/blob/master/assets/preview/bodies.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/JonasMerrell/space-rts](https://github.com/JonasMerrell/space-rts)
- **Evidence:** [direct model evidence](https://github.com/JonasMerrell/space-rts/commit/1232159ab37fe32307bb630d0e84dde9e11a349a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/JonasMerrell/space-rts/blob/master/assets/preview/bodies.png) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. Grid of rendered planets on navy; attractive asset sheet.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A slow, multiplayer real-time strategy game set in a single star system, written in Rust for Android. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/JonasMerrell/space-rts/blob/master/crates/sim/src/game.rs](https://github.com/JonasMerrell/space-rts/blob/master/crates/sim/src/game.rs)
- [https://github.com/JonasMerrell/space-rts/commit/1232159ab37fe32307bb630d0e84dde9e11a349a](https://github.com/JonasMerrell/space-rts/commit/1232159ab37fe32307bb630d0e84dde9e11a349a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/JonasMerrell/space-rts

[Back to the awesome list](../../README.md)
