# Extraction Tycoon

> Verified game note.

![Extraction Tycoon screenshot placeholder](extraction-tycoon-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/BirkleyG/Extraction](https://github.com/BirkleyG/Extraction)
- **Evidence:** [direct model evidence](https://github.com/BirkleyG/Extraction/commit/fb846d6b75462ead3998c70612979ed096bf3b9c)
- **Live demo:** [open demo](https://birkleyg.github.io/Extraction/play/)
- **Additional live link:** [open demo](https://birkleyg.github.io/Extraction/prototype/)
- **Additional live link:** [open demo](https://birkleyg.github.io/Extraction/play/?mode=online)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A miner tycoon game that can be played by a bunch of friends! Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/BirkleyG/Extraction/blob/main/js/game.js](https://github.com/BirkleyG/Extraction/blob/main/js/game.js)
- [https://github.com/BirkleyG/Extraction/commit/fb846d6b75462ead3998c70612979ed096bf3b9c](https://github.com/BirkleyG/Extraction/commit/fb846d6b75462ead3998c70612979ed096bf3b9c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/BirkleyG/Extraction

[Back to the awesome list](../../README.md)
