# Minesweeper 2026

> Verified game note.

![Minesweeper 2026 screenshot placeholder](minesweeper-2026-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/GuillaumeMunsch/minesweeper-2026](https://github.com/GuillaumeMunsch/minesweeper-2026)
- **Evidence:** [direct model evidence](https://github.com/GuillaumeMunsch/minesweeper-2026/commit/0a71840a5ec856db4a68ac7c5e2cde3586ce437e)
- **Live demo:** [open demo](https://guillaumemunsch.github.io/minesweeper-2026/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Classic Minesweeper in the browser, with visual effects on every move. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GuillaumeMunsch/minesweeper-2026/blob/main/src/presentation/particles.ts](https://github.com/GuillaumeMunsch/minesweeper-2026/blob/main/src/presentation/particles.ts)
- [https://github.com/GuillaumeMunsch/minesweeper-2026/commit/0a71840a5ec856db4a68ac7c5e2cde3586ce437e](https://github.com/GuillaumeMunsch/minesweeper-2026/commit/0a71840a5ec856db4a68ac7c5e2cde3586ce437e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/GuillaumeMunsch/minesweeper-2026

[Back to the awesome list](../../README.md)
