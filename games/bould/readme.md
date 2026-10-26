# BOULD

> Verified game note.

![BOULD screenshot placeholder](bould-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/dwavid/boulder-game](https://github.com/dwavid/boulder-game)
- **Evidence:** [direct model evidence](https://github.com/dwavid/boulder-game/commit/8d96c5e3ff13880b20d5e5f2e173a24c93898ebb)
- **Live demo:** [open demo](https://dwavid.github.io/boulder-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

You're a boulder. Roll around, run over people, and don't land on spikes. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dwavid/boulder-game/blob/main/game.js](https://github.com/dwavid/boulder-game/blob/main/game.js)
- [https://github.com/dwavid/boulder-game/commit/8d96c5e3ff13880b20d5e5f2e173a24c93898ebb](https://github.com/dwavid/boulder-game/commit/8d96c5e3ff13880b20d5e5f2e173a24c93898ebb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/dwavid/boulder-game

[Back to the awesome list](../../README.md)
