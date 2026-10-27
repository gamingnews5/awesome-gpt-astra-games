# Ramped Up

> Verified game note.

![Ramped Up screenshot placeholder](ramped-up-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/jupixels/rampedup](https://github.com/jupixels/rampedup)
- **Evidence:** [direct model evidence](https://github.com/jupixels/rampedup/commit/7736f9c4dbafc00dd8892c57828ad4de376ed893)
- **Live demo:** [open demo](https://jupixels.github.io/rampedup/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

No install, no accounts, no build step. It runs straight from GitHub Pages. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jupixels/rampedup/blob/main/js/world.js](https://github.com/jupixels/rampedup/blob/main/js/world.js)
- [https://github.com/jupixels/rampedup/commit/7736f9c4dbafc00dd8892c57828ad4de376ed893](https://github.com/jupixels/rampedup/commit/7736f9c4dbafc00dd8892c57828ad4de376ed893)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/jupixels/rampedup

[Back to the awesome list](../../README.md)
