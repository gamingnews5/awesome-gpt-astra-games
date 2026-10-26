# Scrap Droid

> Verified game note.

![Scrap Droid screenshot placeholder](scrap-droid-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/kelleyblackmore/scrap-droid](https://github.com/kelleyblackmore/scrap-droid)
- **Evidence:** [direct model evidence](https://github.com/kelleyblackmore/scrap-droid/commit/3f788bc5ea0ce597539fcc172ce1bd4e2c76b4b2)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A slither.io-style arena game, except you're a droid and you eat scrap. Single-player against AI droids. It runs entirely in the browser, with no build step and no server. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kelleyblackmore/scrap-droid/blob/ccr-f8e3c9c1-te59sf/game.js](https://github.com/kelleyblackmore/scrap-droid/blob/ccr-f8e3c9c1-te59sf/game.js)
- [https://github.com/kelleyblackmore/scrap-droid/commit/3f788bc5ea0ce597539fcc172ce1bd4e2c76b4b2](https://github.com/kelleyblackmore/scrap-droid/commit/3f788bc5ea0ce597539fcc172ce1bd4e2c76b4b2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/kelleyblackmore/scrap-droid

[Back to the awesome list](../../README.md)
