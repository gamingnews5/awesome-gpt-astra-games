# Ascent Flight

> Top-list entry: **today** (#2).

![Ascent Flight screenshot](https://raw.githubusercontent.com/calebschalesky-ops/ascent/main/docs/flight.jpg)

## At a glance

- **Score:** 8.2/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/calebschalesky-ops/ascent/blob/main/docs/flight.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/calebschalesky-ops/ascent](https://github.com/calebschalesky-ops/ascent)
- **Evidence:** [direct model evidence](https://github.com/calebschalesky-ops/ascent/commit/506c6a853a2bc806b692188e432f6d27d1239f7a)
- **Live demo:** [open demo](https://calebschalesky-ops.github.io/ascent/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/calebschalesky-ops/ascent/blob/main/docs/flight.jpg) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. 3D spaceship flight scene with rich HUD panels; detailed but cluttered.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

3D space game (React, TypeScript, three.js) built by a studio of Claude Code agents. 947 tests. Playable in the browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/calebschalesky-ops/ascent/blob/main/src/components/Voyage.tsx](https://github.com/calebschalesky-ops/ascent/blob/main/src/components/Voyage.tsx)
- [https://github.com/calebschalesky-ops/ascent/commit/506c6a853a2bc806b692188e432f6d27d1239f7a](https://github.com/calebschalesky-ops/ascent/commit/506c6a853a2bc806b692188e432f6d27d1239f7a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/calebschalesky-ops/ascent

[Back to the awesome list](../../README.md)
