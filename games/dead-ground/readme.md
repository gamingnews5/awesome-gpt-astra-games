# Dead Ground

> Verified game note.

![Dead Ground screenshot placeholder](dead-ground-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/GreenMachine414/dead-ground](https://github.com/GreenMachine414/dead-ground)
- **Evidence:** [direct model evidence](https://github.com/GreenMachine414/dead-ground/commit/a37ddb9a95a5f7b5e901479513bdc4653ce32a91)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Top-down co-op zombie survival game (Electron). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GreenMachine414/dead-ground/blob/main/src/game/sim.js](https://github.com/GreenMachine414/dead-ground/blob/main/src/game/sim.js)
- [https://github.com/GreenMachine414/dead-ground/commit/a37ddb9a95a5f7b5e901479513bdc4653ce32a91](https://github.com/GreenMachine414/dead-ground/commit/a37ddb9a95a5f7b5e901479513bdc4653ce32a91)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/GreenMachine414/dead-ground

[Back to the awesome list](../../README.md)
