# Weird Games

> Verified game note.

![Weird Games screenshot placeholder](weird-games-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/ardie0727/weird-games](https://github.com/ardie0727/weird-games)
- **Evidence:** [direct model evidence](https://github.com/ardie0727/weird-games/commit/6e1e9186ee94687086c495fe5d1ff2005452b4ba)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Odd little browser games. The first one is Query Arcade: a fast, retro arcade for SQL and PySpark. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ardie0727/weird-games/blob/main/src/components/rbm/RubberBulletMan.tsx](https://github.com/ardie0727/weird-games/blob/main/src/components/rbm/RubberBulletMan.tsx)
- [https://github.com/ardie0727/weird-games/commit/6e1e9186ee94687086c495fe5d1ff2005452b4ba](https://github.com/ardie0727/weird-games/commit/6e1e9186ee94687086c495fe5d1ff2005452b4ba)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/ardie0727/weird-games

[Back to the awesome list](../../README.md)
