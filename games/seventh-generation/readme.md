# Seventh Generation

> Verified game note.

![Seventh Generation screenshot](https://raw.githubusercontent.com/bigdevwhale/seventh/main/docs/screenshots/en/1-home.jpg)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/bigdevwhale/seventh/blob/main/docs/screenshots/en/1-home.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/bigdevwhale/seventh](https://github.com/bigdevwhale/seventh)
- **Evidence:** [direct model evidence](https://github.com/bigdevwhale/seventh/commit/6e34b7be403790bd580ade3daacd524a04b5e677)
- **Live demo:** [open demo](https://bigdevwhale.github.io/stillcraft/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/bigdevwhale/seventh/blob/main/docs/screenshots/en/1-home.jpg) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Folk-tale dynasty card with illustrated landscape and stats; stylish parchment UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A family cursed to the seventh generation: a dynasty game told as a folk tale. Rus, medieval Europe and Japan, each drawn in its own style; every deed settled by a bean from a bag. Android, offline, EN/RU. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bigdevwhale/seventh/blob/main/app/src/main/java/app/seventh/domain/JapanMore.kt](https://github.com/bigdevwhale/seventh/blob/main/app/src/main/java/app/seventh/domain/JapanMore.kt)
- [https://github.com/bigdevwhale/seventh/commit/6e34b7be403790bd580ade3daacd524a04b5e677](https://github.com/bigdevwhale/seventh/commit/6e34b7be403790bd580ade3daacd524a04b5e677)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/bigdevwhale/seventh

[Back to the awesome list](../../README.md)
