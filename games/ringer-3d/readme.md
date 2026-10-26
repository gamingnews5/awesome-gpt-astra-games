# Ringer 3D

> Verified game note.

![Ringer 3D screenshot placeholder](ringer-3d-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/BorisThoris/ringer3d](https://github.com/BorisThoris/ringer3d)
- **Evidence:** [direct model evidence](https://github.com/BorisThoris/ringer3d/commit/05411d6dbd780a6781ded6361c98af27a0ac429e)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The classic playground marble game — Ringer — rebuilt as a modern 3D game for web, iOS, Android and desktop. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/BorisThoris/ringer3d/blob/main/src/render/GameView.ts](https://github.com/BorisThoris/ringer3d/blob/main/src/render/GameView.ts)
- [https://github.com/BorisThoris/ringer3d/commit/05411d6dbd780a6781ded6361c98af27a0ac429e](https://github.com/BorisThoris/ringer3d/commit/05411d6dbd780a6781ded6361c98af27a0ac429e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/BorisThoris/ringer3d

[Back to the awesome list](../../README.md)
