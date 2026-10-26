# Orbit Rush

> Verified game note.

![Orbit Rush screenshot placeholder](orbit-rush-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Fable 5.1
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/dehanz13/racing-game-orbit-rush](https://github.com/dehanz13/racing-game-orbit-rush)
- **Evidence:** [direct model evidence](https://github.com/dehanz13/racing-game-orbit-rush/commit/84c7b3b59782f17bc2a558539ba1ab677ec719d3)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An arcade drive-and-collect game that runs entirely in the browser. Built with React, React Three Fiber, Three.js, postprocessing (bloom, vignette), Zustand and Vite. No 3D asset files, no audio files, no backend: every model is procedural geometry, every… Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dehanz13/racing-game-orbit-rush/blob/main/src/game/engine.ts](https://github.com/dehanz13/racing-game-orbit-rush/blob/main/src/game/engine.ts)
- [https://github.com/dehanz13/racing-game-orbit-rush/commit/84c7b3b59782f17bc2a558539ba1ab677ec719d3](https://github.com/dehanz13/racing-game-orbit-rush/commit/84c7b3b59782f17bc2a558539ba1ab677ec719d3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/dehanz13/racing-game-orbit-rush

[Back to the awesome list](../../README.md)
