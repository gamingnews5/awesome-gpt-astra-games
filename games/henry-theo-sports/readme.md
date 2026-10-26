# Henry & Theo Sports

> Verified game note.

![Henry & Theo Sports screenshot placeholder](henry-theo-sports-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/awjudd/theo-sports](https://github.com/awjudd/theo-sports)
- **Evidence:** [direct model evidence](https://github.com/awjudd/theo-sports/commit/337a8f920726ee663e12c815c2bc8c403d2f3789)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser game — no build step, no dependencies. Open index.html (or serve the folder with any static server, e.g. python3 -m http.server). Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/awjudd/theo-sports/blob/main/js/characters.js](https://github.com/awjudd/theo-sports/blob/main/js/characters.js)
- [https://github.com/awjudd/theo-sports/commit/337a8f920726ee663e12c815c2bc8c403d2f3789](https://github.com/awjudd/theo-sports/commit/337a8f920726ee663e12c815c2bc8c403d2f3789)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/awjudd/theo-sports

[Back to the awesome list](../../README.md)
