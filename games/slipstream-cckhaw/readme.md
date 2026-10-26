# Slipstream (cckhaw)

> Verified game note.

![Slipstream (cckhaw) screenshot placeholder](slipstream-cckhaw-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/cckhaw/slipstream](https://github.com/cckhaw/slipstream)
- **Evidence:** [direct model evidence](https://github.com/cckhaw/slipstream/commit/e8596eb735e8008b28c9d0e48b0126ba21fa1f3d)
- **Live demo:** [open demo](https://slipstream-theta-seven.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A one-touch mobile arcade game for the browser: React + Vite + Tailwind, HTML5 Canvas (2D worlds), three.js (3D worlds) and Web Audio. The UI mixes Apple HIG basics (44pt+ touch targets, safe areas, system fonts, Reduce Motion) with a chunky, bevelled,… Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cckhaw/slipstream/blob/main/src/game/render3d.js](https://github.com/cckhaw/slipstream/blob/main/src/game/render3d.js)
- [https://github.com/cckhaw/slipstream/commit/e8596eb735e8008b28c9d0e48b0126ba21fa1f3d](https://github.com/cckhaw/slipstream/commit/e8596eb735e8008b28c9d0e48b0126ba21fa1f3d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/cckhaw/slipstream

[Back to the awesome list](../../README.md)
