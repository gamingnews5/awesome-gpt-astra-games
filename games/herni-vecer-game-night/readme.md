# Herní večer (Game Night)

> Verified game note.

![Herní večer (Game Night) screenshot placeholder](herni-vecer-game-night-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/HaubertTech/game-night](https://github.com/HaubertTech/game-night)
- **Evidence:** [direct model evidence](https://github.com/HaubertTech/game-night/commit/4aa02272d4ec29fe98e46d763423374c6a9ed78c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Herní večer — domácí herní večery: kvíz pro všechny věky, Řekni-ukaž-nakresli, Město-jméno-zvíře, šachy, prší a žolíky, liga rodiny. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/HaubertTech/game-night/blob/main/src/lib/games/mjz/engine.ts](https://github.com/HaubertTech/game-night/blob/main/src/lib/games/mjz/engine.ts)
- [https://github.com/HaubertTech/game-night/commit/4aa02272d4ec29fe98e46d763423374c6a9ed78c](https://github.com/HaubertTech/game-night/commit/4aa02272d4ec29fe98e46d763423374c6a9ed78c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/HaubertTech/game-night

[Back to the awesome list](../../README.md)
