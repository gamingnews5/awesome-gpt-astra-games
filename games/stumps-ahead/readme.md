# Stumps Ahead

> Verified game note.

![Stumps Ahead screenshot placeholder](stumps-ahead-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Ptalati015/Stumps_Ahead](https://github.com/Ptalati015/Stumps_Ahead)
- **Evidence:** [direct model evidence](https://github.com/Ptalati015/Stumps_Ahead/commit/e26c8e12fce4e461e2d4b52129498ed00ef68feb)
- **Live demo:** [open demo](https://ptalati015.github.io/Stumps_Ahead/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A short-format cricket game for mobile browsers, inspired by EA Sports Cricket and Real Cricket 20 but much simpler. You play one T20-style match against the computer. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Ptalati015/Stumps_Ahead/blob/main/js/ui/scene/scene.js](https://github.com/Ptalati015/Stumps_Ahead/blob/main/js/ui/scene/scene.js)
- [https://github.com/Ptalati015/Stumps_Ahead/commit/e26c8e12fce4e461e2d4b52129498ed00ef68feb](https://github.com/Ptalati015/Stumps_Ahead/commit/e26c8e12fce4e461e2d4b52129498ed00ef68feb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Ptalati015/Stumps_Ahead

[Back to the awesome list](../../README.md)
