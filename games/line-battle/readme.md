# Line Battle

> Verified game note.

![Line Battle screenshot placeholder](line-battle-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/hoangnguyen92/line-battle](https://github.com/hoangnguyen92/line-battle)
- **Evidence:** [direct model evidence](https://github.com/hoangnguyen92/line-battle/commit/0acfa5a931e6b62ad6cd77ff40f15c3c49b817bf)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser falling-block versus game in TypeScript. Phase 1 built the engine. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hoangnguyen92/line-battle/blob/fixes/packages/web/src/main.ts](https://github.com/hoangnguyen92/line-battle/blob/fixes/packages/web/src/main.ts)
- [https://github.com/hoangnguyen92/line-battle/commit/0acfa5a931e6b62ad6cd77ff40f15c3c49b817bf](https://github.com/hoangnguyen92/line-battle/commit/0acfa5a931e6b62ad6cd77ff40f15c3c49b817bf)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/hoangnguyen92/line-battle

[Back to the awesome list](../../README.md)
