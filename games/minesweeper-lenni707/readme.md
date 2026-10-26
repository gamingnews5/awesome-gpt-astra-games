# Minesweeper (Lenni707)

> Verified game note.

![Minesweeper (Lenni707) screenshot placeholder](minesweeper-lenni707-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Lenni707/minesweeper-clean](https://github.com/Lenni707/minesweeper-clean)
- **Evidence:** [direct model evidence](https://github.com/Lenni707/minesweeper-clean/commit/21e3fdbf2ac79a470ddb8327473886271206a4d6)
- **Live demo:** [open demo](https://lenni707.github.io/minesweeper-clean/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A clean, animated Minesweeper PWA. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Lenni707/minesweeper-clean/blob/main/src/ui/boardView.ts](https://github.com/Lenni707/minesweeper-clean/blob/main/src/ui/boardView.ts)
- [https://github.com/Lenni707/minesweeper-clean/commit/21e3fdbf2ac79a470ddb8327473886271206a4d6](https://github.com/Lenni707/minesweeper-clean/commit/21e3fdbf2ac79a470ddb8327473886271206a4d6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Lenni707/minesweeper-clean

[Back to the awesome list](../../README.md)
