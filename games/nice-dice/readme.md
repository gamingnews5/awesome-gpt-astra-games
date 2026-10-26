# Nice Dice

> Verified game note.

![Nice Dice screenshot placeholder](nice-dice-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Fable 5.1
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/humainasger/nice-dice](https://github.com/humainasger/nice-dice)
- **Evidence:** [direct model evidence](https://github.com/humainasger/nice-dice/commit/a60a84502badda53e3c946b35a41183777f06bbd)
- **Live demo:** [open demo](https://humainasger.github.io/nice-dice/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Nice Dice, a browser dice incremental game built mostly with Claude Code. Commit carries an exact Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/humainasger/nice-dice/blob/main/src/app/selectors.ts](https://github.com/humainasger/nice-dice/blob/main/src/app/selectors.ts)
- [https://github.com/humainasger/nice-dice/commit/a60a84502badda53e3c946b35a41183777f06bbd](https://github.com/humainasger/nice-dice/commit/a60a84502badda53e3c946b35a41183777f06bbd)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/humainasger/nice-dice

[Back to the awesome list](../../README.md)
