# Asteroid Fleet

> Verified game note.

![Asteroid Fleet screenshot placeholder](asteroid-fleet-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/deadronos/asteroid-fleet](https://github.com/deadronos/asteroid-fleet)
- **Evidence:** [direct model evidence](https://github.com/deadronos/asteroid-fleet/commit/161b6f7cb424b3c20709e0da60f74bc5fdc91d25)
- **Live demo:** [open demo](https://deadronos.github.io/asteroid-fleet/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser idle game with an autobattler setup, in full 3D. You are the admiral, not the pilot: outfit a mining carrier's hangars, set stances and rules, and warp outward into richer, more dangerous systems while the fleet works on its own. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/deadronos/asteroid-fleet/blob/main/src/sim/state.ts](https://github.com/deadronos/asteroid-fleet/blob/main/src/sim/state.ts)
- [https://github.com/deadronos/asteroid-fleet/commit/161b6f7cb424b3c20709e0da60f74bc5fdc91d25](https://github.com/deadronos/asteroid-fleet/commit/161b6f7cb424b3c20709e0da60f74bc5fdc91d25)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/deadronos/asteroid-fleet

[Back to the awesome list](../../README.md)
