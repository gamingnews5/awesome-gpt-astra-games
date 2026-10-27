# F1-Retro

> Verified game note.

![F1-Retro screenshot placeholder](f1-retro-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Mino-oss-byte/f1-retro](https://github.com/Mino-oss-byte/f1-retro)
- **Evidence:** [direct model evidence](https://github.com/Mino-oss-byte/f1-retro/commit/5100d1c308fae120413bf0ad6d954b26aaa70849)
- **Live demo:** [open demo](https://mino-oss-byte.github.io/f1-retro/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser 3D retro formula racer (Three.js + Vite). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Mino-oss-byte/f1-retro/blob/main/src/data/tracks/spa.js](https://github.com/Mino-oss-byte/f1-retro/blob/main/src/data/tracks/spa.js)
- [https://github.com/Mino-oss-byte/f1-retro/commit/5100d1c308fae120413bf0ad6d954b26aaa70849](https://github.com/Mino-oss-byte/f1-retro/commit/5100d1c308fae120413bf0ad6d954b26aaa70849)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Mino-oss-byte/f1-retro

[Back to the awesome list](../../README.md)
