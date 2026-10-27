# Token Rider

> Verified game note.

![Token Rider screenshot placeholder](token-rider-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Tetriss22/token-rider](https://github.com/Tetriss22/token-rider)
- **Evidence:** [direct model evidence](https://github.com/Tetriss22/token-rider/commit/74688426e5c74ccea4bab60397383a8efca0f43f)
- **Live demo:** [open demo](https://tetriss22.github.io/token-rider/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D game that runs in your browser tab. 5 levels, 5 bosses, 5 rewards: every boss drops a prompt or a skill for Claude, and the last one drops the prompt of the whole game. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Tetriss22/token-rider/blob/main/game.js](https://github.com/Tetriss22/token-rider/blob/main/game.js)
- [https://github.com/Tetriss22/token-rider/commit/74688426e5c74ccea4bab60397383a8efca0f43f](https://github.com/Tetriss22/token-rider/commit/74688426e5c74ccea4bab60397383a8efca0f43f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Tetriss22/token-rider

[Back to the awesome list](../../README.md)
