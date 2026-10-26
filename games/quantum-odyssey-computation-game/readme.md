# Quantum Odyssey (computation game)

> Verified game note.

![Quantum Odyssey (computation game) screenshot placeholder](quantum-odyssey-computation-game-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Soren-O/computation-game](https://github.com/Soren-O/computation-game)
- **Evidence:** [direct model evidence](https://github.com/Soren-O/computation-game/commit/93041836333844e271b6cddcd36e6c905307e11e)
- **Live demo:** [open demo](https://soren-o.github.io/computation-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Quantum puzzle game: states on a hypercube, amplitudes as arrows. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Soren-O/computation-game/blob/main/src/components/GameLevelScreen.tsx](https://github.com/Soren-O/computation-game/blob/main/src/components/GameLevelScreen.tsx)
- [https://github.com/Soren-O/computation-game/commit/93041836333844e271b6cddcd36e6c905307e11e](https://github.com/Soren-O/computation-game/commit/93041836333844e271b6cddcd36e6c905307e11e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Soren-O/computation-game

[Back to the awesome list](../../README.md)
