# Word Shake

> Verified game note.

![Word Shake screenshot placeholder](word-shake-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/schrjacob/word-shake](https://github.com/schrjacob/word-shake)
- **Evidence:** [direct model evidence](https://github.com/schrjacob/word-shake/commit/baccc6c1774da6e449a044d0c90a62a165c23eeb)
- **Live demo:** [open demo](https://schrjacob.github.io/word-shake/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Multiplayer word-dice game: trace words on a shared board, race the timer, compare scores. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/schrjacob/word-shake/blob/main/app.js](https://github.com/schrjacob/word-shake/blob/main/app.js)
- [https://github.com/schrjacob/word-shake/commit/baccc6c1774da6e449a044d0c90a62a165c23eeb](https://github.com/schrjacob/word-shake/commit/baccc6c1774da6e449a044d0c90a62a165c23eeb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/schrjacob/word-shake

[Back to the awesome list](../../README.md)
