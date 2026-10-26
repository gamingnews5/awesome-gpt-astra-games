# Maze Tanks

> Verified game note.

![Maze Tanks screenshot placeholder](maze-tanks-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/PolynomialI/maze-tanks](https://github.com/PolynomialI/maze-tanks)
- **Evidence:** [direct model evidence](https://github.com/PolynomialI/maze-tanks/commit/8fbeeaa0791aa2b389c88d96630a7da914f5f482)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Top-down tank battles in a random maze: bullets bounce off walls, power-up crates appear over time, and the last tank standing wins the round. Flat 2D art, no text in the game. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/PolynomialI/maze-tanks/blob/main/shared/game.js](https://github.com/PolynomialI/maze-tanks/blob/main/shared/game.js)
- [https://github.com/PolynomialI/maze-tanks/commit/8fbeeaa0791aa2b389c88d96630a7da914f5f482](https://github.com/PolynomialI/maze-tanks/commit/8fbeeaa0791aa2b389c88d96630a7da914f5f482)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/PolynomialI/maze-tanks

[Back to the awesome list](../../README.md)
