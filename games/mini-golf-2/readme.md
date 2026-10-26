# Mini Golf 2

> Verified game note.

![Mini Golf 2 screenshot placeholder](mini-golf-2-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/heidenreich/mini-golf-2](https://github.com/heidenreich/mini-golf-2)
- **Evidence:** [direct model evidence](https://github.com/heidenreich/mini-golf-2/commit/b920256fc64ac67592fb5fad4618993ec3c90c09)
- **Live demo:** [open demo](https://heidenreich.github.io/mini-golf-2/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

3D mini golf on floating sky islands, played in your phone's browser. The sequel to Mini Golf: the same drag-back-and-release putting, now with real slopes, ramps, a crater and a camera you can swing round the ball. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/heidenreich/mini-golf-2/blob/main/js/render.js](https://github.com/heidenreich/mini-golf-2/blob/main/js/render.js)
- [https://github.com/heidenreich/mini-golf-2/commit/b920256fc64ac67592fb5fad4618993ec3c90c09](https://github.com/heidenreich/mini-golf-2/commit/b920256fc64ac67592fb5fad4618993ec3c90c09)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/heidenreich/mini-golf-2

[Back to the awesome list](../../README.md)
