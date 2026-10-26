# felt

> Verified game note.

![felt screenshot placeholder](felt-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/zacker3310/felt](https://github.com/zacker3310/felt)
- **Evidence:** [direct model evidence](https://github.com/zacker3310/felt/commit/1b23091b8c4c9b4daa384c2a5aecf2ee009143b5)
- **Live demo:** [open demo](https://zacker3310.github.io/felt/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

8-ball and 9-ball pool in one HTML file, deterministic physics from puttX. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/zacker3310/felt/blob/main/index.html](https://github.com/zacker3310/felt/blob/main/index.html)
- [https://github.com/zacker3310/felt/commit/1b23091b8c4c9b4daa384c2a5aecf2ee009143b5](https://github.com/zacker3310/felt/commit/1b23091b8c4c9b4daa384c2a5aecf2ee009143b5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/zacker3310/felt

[Back to the awesome list](../../README.md)
