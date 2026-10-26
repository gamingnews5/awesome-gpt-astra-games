# System Design Quest

> Verified game note.

![System Design Quest screenshot placeholder](system-design-quest-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/congluat/300-bai-design-thieunhi](https://github.com/congluat/300-bai-design-thieunhi)
- **Evidence:** [direct model evidence](https://github.com/congluat/300-bai-design-thieunhi/commit/644af9c84c275ebeb80733ae7a0563be01a18ba9)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A hand-drawn system design game that runs in the browser — 100 challenges from 20 req/s to millions of req/s with a 10M req/s DDoS on top. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/congluat/300-bai-design-thieunhi/blob/main/src/game/levels.ts](https://github.com/congluat/300-bai-design-thieunhi/blob/main/src/game/levels.ts)
- [https://github.com/congluat/300-bai-design-thieunhi/commit/644af9c84c275ebeb80733ae7a0563be01a18ba9](https://github.com/congluat/300-bai-design-thieunhi/commit/644af9c84c275ebeb80733ae7a0563be01a18ba9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/congluat/300-bai-design-thieunhi

[Back to the awesome list](../../README.md)
