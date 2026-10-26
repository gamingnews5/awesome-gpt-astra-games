# Off Carrom

> Verified game note.

![Off Carrom screenshot placeholder](off-carrom-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Lucky6400/off-carrom](https://github.com/Lucky6400/off-carrom)
- **Evidence:** [direct model evidence](https://github.com/Lucky6400/off-carrom/commit/3e0fa3ed5b47288a3317f6f25ca47c989e113096)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A landscape-only arcade carrom game built on the Off Pool engine: Vite + TypeScript, Canvas 2D (everything drawn in code, no image assets), a pure-TS carrom physics engine,. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Lucky6400/off-carrom/blob/main/src/gfx/portrait.ts](https://github.com/Lucky6400/off-carrom/blob/main/src/gfx/portrait.ts)
- [https://github.com/Lucky6400/off-carrom/commit/3e0fa3ed5b47288a3317f6f25ca47c989e113096](https://github.com/Lucky6400/off-carrom/commit/3e0fa3ed5b47288a3317f6f25ca47c989e113096)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Lucky6400/off-carrom

[Back to the awesome list](../../README.md)
