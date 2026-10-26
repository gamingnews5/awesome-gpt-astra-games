# Hover Tank Arena

> Verified game note.

![Hover Tank Arena screenshot placeholder](hover-tank-arena-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/LilDayne30/hovertank-arena](https://github.com/LilDayne30/hovertank-arena)
- **Evidence:** [direct model evidence](https://github.com/LilDayne30/hovertank-arena/commit/66ed351ecb97236f3836748a82e53b5fbd50b7ec)
- **Live demo:** [open demo](https://hovertank-arena.danaoki30.workers.dev)
- **Additional live link:** [open demo](https://h4kor.itch.io/low-poly-desert-arena)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Lightweight 3D hover-tank web arena for up to 4 players (PlayCanvas + Colyseus). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/LilDayne30/hovertank-arena/blob/main/client/main.js](https://github.com/LilDayne30/hovertank-arena/blob/main/client/main.js)
- [https://github.com/LilDayne30/hovertank-arena/commit/66ed351ecb97236f3836748a82e53b5fbd50b7ec](https://github.com/LilDayne30/hovertank-arena/commit/66ed351ecb97236f3836748a82e53b5fbd50b7ec)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/LilDayne30/hovertank-arena

[Back to the awesome list](../../README.md)
