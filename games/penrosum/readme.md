# Penrosum

> Verified game note.

![Penrosum screenshot placeholder](penrosum-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/dblevins-3dgfx/penrosum](https://github.com/dblevins-3dgfx/penrosum)
- **Evidence:** [direct model evidence](https://github.com/dblevins-3dgfx/penrosum/commit/78c359dd617855a0682ea82ef2fa346de8ee6876)
- **Live demo:** [open demo](https://dblevins-3dgfx.github.io/penrosum/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Summing game using a Penrose Tiled game board. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dblevins-3dgfx/penrosum/blob/main/src/Game.tsx](https://github.com/dblevins-3dgfx/penrosum/blob/main/src/Game.tsx)
- [https://github.com/dblevins-3dgfx/penrosum/commit/78c359dd617855a0682ea82ef2fa346de8ee6876](https://github.com/dblevins-3dgfx/penrosum/commit/78c359dd617855a0682ea82ef2fa346de8ee6876)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/dblevins-3dgfx/penrosum

[Back to the awesome list](../../README.md)
