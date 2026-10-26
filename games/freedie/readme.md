# Freedie

> Verified game note.

![Freedie screenshot](https://raw.githubusercontent.com/Shumtugle/freedie/main/docs/freedie.webp)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/Shumtugle/freedie/blob/main/docs/freedie.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Java
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Shumtugle/freedie](https://github.com/Shumtugle/freedie)
- **Evidence:** [direct model evidence](https://github.com/Shumtugle/freedie/commit/a7c7eddbd72c1c609bd178e9897f719cc9bd6e84)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Shumtugle/freedie/blob/main/docs/freedie.webp) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Voxel giant in a maid outfit render; quirky character asset.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A game for Android about knocking down buildings with a hammer, on a summer street of a. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Shumtugle/freedie/blob/main/src/com/shumtugle/freedie/Game.java](https://github.com/Shumtugle/freedie/blob/main/src/com/shumtugle/freedie/Game.java)
- [https://github.com/Shumtugle/freedie/commit/a7c7eddbd72c1c609bd178e9897f719cc9bd6e84](https://github.com/Shumtugle/freedie/commit/a7c7eddbd72c1c609bd178e9897f719cc9bd6e84)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Shumtugle/freedie

[Back to the awesome list](../../README.md)
