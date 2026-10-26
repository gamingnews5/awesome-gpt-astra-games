# MasterWorld

> Verified game note.

![MasterWorld screenshot placeholder](masterworld-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/ArndRosemeier/MasterWorld](https://github.com/ArndRosemeier/MasterWorld)
- **Evidence:** [direct model evidence](https://github.com/ArndRosemeier/MasterWorld/commit/9a3b4730738121b59fbc4873ebfb51a413ed0eae)
- **Live demo:** [open demo](https://arndrosemeier.github.io/MasterWorld/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A classic fantasy roleplaying game in the browser (TypeScript, three.js) with a virtual game master that watches play and builds the world as it is needed. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ArndRosemeier/MasterWorld/blob/main/tools/duplicate-candidates/find-duplicate-candidates.mjs](https://github.com/ArndRosemeier/MasterWorld/blob/main/tools/duplicate-candidates/find-duplicate-candidates.mjs)
- [https://github.com/ArndRosemeier/MasterWorld/commit/9a3b4730738121b59fbc4873ebfb51a413ed0eae](https://github.com/ArndRosemeier/MasterWorld/commit/9a3b4730738121b59fbc4873ebfb51a413ed0eae)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/ArndRosemeier/MasterWorld

[Back to the awesome list](../../README.md)
