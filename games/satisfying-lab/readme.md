# Satisfying Lab

> Verified game note.

![Satisfying Lab screenshot placeholder](satisfying-lab-placeholder.svg)

## At a glance

- **Score:** 6.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/jpetree331/game-3d-physics-fun](https://github.com/jpetree331/game-3d-physics-fun)
- **Evidence:** [direct model evidence](https://github.com/jpetree331/game-3d-physics-fun/commit/1da0fb0cc084460f9a1f52840544caaeab4dbf00)
- **Live demo:** [open demo](https://game-3d-physics-fun.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A colorful browser physics playground built with Three.js and Rapier. All rendering and simulation run locally in the browser. There is no game backend or account requirement in the application itself. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jpetree331/game-3d-physics-fun/blob/main/server.mjs](https://github.com/jpetree331/game-3d-physics-fun/blob/main/server.mjs)
- [https://github.com/jpetree331/game-3d-physics-fun/commit/1da0fb0cc084460f9a1f52840544caaeab4dbf00](https://github.com/jpetree331/game-3d-physics-fun/commit/1da0fb0cc084460f9a1f52840544caaeab4dbf00)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/jpetree331/game-3d-physics-fun

[Back to the awesome list](../../README.md)
