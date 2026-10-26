# Dino Runner

> Verified game note.

![Dino Runner screenshot placeholder](dino-runner-nikhilbelwate-dino-runner-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/NikhilBelwate/dino-runner](https://github.com/NikhilBelwate/dino-runner)
- **Evidence:** [direct model evidence](https://github.com/NikhilBelwate/dino-runner/commit/ccf7c64d15bb5a902fc0f87e38ff3e5090a3c2fe)
- **Live demo:** [open demo](https://nikhilbelwate.github.io/dino-runner/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A jumping-dinosaur endless runner in the style of the browser's offline game, built with plain HTML, CSS and JavaScript (no libraries, no build step). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/NikhilBelwate/dino-runner/blob/main/game.js](https://github.com/NikhilBelwate/dino-runner/blob/main/game.js)
- [https://github.com/NikhilBelwate/dino-runner/commit/ccf7c64d15bb5a902fc0f87e38ff3e5090a3c2fe](https://github.com/NikhilBelwate/dino-runner/commit/ccf7c64d15bb5a902fc0f87e38ff3e5090a3c2fe)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/NikhilBelwate/dino-runner

[Back to the awesome list](../../README.md)
