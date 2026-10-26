# Shikaku

> Verified game note.

![Shikaku screenshot placeholder](shikaku-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/dqyi11/shikaku](https://github.com/dqyi11/shikaku)
- **Evidence:** [direct model evidence](https://github.com/dqyi11/shikaku/commit/ee6d262c7a0363ba2a4f36d40d368142e65f8f2a)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser Shikaku puzzle (四角に切れ, "divide by squares"). Split the grid into rectangles so that each rectangle holds exactly one number, and that number is the rectangle's area. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dqyi11/shikaku/blob/main/index.html](https://github.com/dqyi11/shikaku/blob/main/index.html)
- [https://github.com/dqyi11/shikaku/commit/ee6d262c7a0363ba2a4f36d40d368142e65f8f2a](https://github.com/dqyi11/shikaku/commit/ee6d262c7a0363ba2a4f36d40d368142e65f8f2a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/dqyi11/shikaku

[Back to the awesome list](../../README.md)
