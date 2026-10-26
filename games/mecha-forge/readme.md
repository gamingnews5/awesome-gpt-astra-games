# Mecha Forge

> Verified game note.

![Mecha Forge screenshot placeholder](mecha-forge-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/michaelenew/kids-games](https://github.com/michaelenew/kids-games)
- **Evidence:** [direct model evidence](https://github.com/michaelenew/kids-games/commit/36314fbac71ed0960735a5df12be02b5a0b1dce5)
- **Live demo:** [open demo](https://michaelenew.github.io/kids-games/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D robot action game for a kid going into 3rd grade. You fight an alien invasion in an arcade shooter, blast rust-bots in side-scrolling patrols, collect scrap, transform into a car, forge and repair armor plates, and, if you want to, build upgrades in the… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/michaelenew/kids-games/blob/main/src/three/robot.ts](https://github.com/michaelenew/kids-games/blob/main/src/three/robot.ts)
- [https://github.com/michaelenew/kids-games/commit/36314fbac71ed0960735a5df12be02b5a0b1dce5](https://github.com/michaelenew/kids-games/commit/36314fbac71ed0960735a5df12be02b5a0b1dce5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/michaelenew/kids-games

[Back to the awesome list](../../README.md)
