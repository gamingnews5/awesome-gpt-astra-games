# Expandia HQ (hosted build)

> Verified game note.

![Expandia HQ (hosted build) screenshot placeholder](expandia-hq-hosted-build-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/sroblempolver/expandia-hq-game](https://github.com/sroblempolver/expandia-hq-game)
- **Evidence:** [direct model evidence](https://github.com/sroblempolver/expandia-hq-game/commit/d1b3a16e7d58c89f012c464d4711ce66ae41949f)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The built game (one file, index.html) that Vercel serves. It is built from the game source with node tools/build.mjs; do not edit index.html by hand. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/sroblempolver/expandia-hq-game/blob/main/index.html](https://github.com/sroblempolver/expandia-hq-game/blob/main/index.html)
- [https://github.com/sroblempolver/expandia-hq-game/commit/d1b3a16e7d58c89f012c464d4711ce66ae41949f](https://github.com/sroblempolver/expandia-hq-game/commit/d1b3a16e7d58c89f012c464d4711ce66ae41949f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/sroblempolver/expandia-hq-game

[Back to the awesome list](../../README.md)
