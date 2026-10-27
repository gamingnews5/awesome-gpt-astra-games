# Laddle

> Verified game note.

![Laddle screenshot placeholder](laddle-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** Roblox, Luau
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/appiemaster/laddle](https://github.com/appiemaster/laddle)
- **Evidence:** [direct model evidence](https://github.com/appiemaster/laddle/commit/ce010b7730e49f5ac85e9fa8a855d523393ad8fa)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A daily word-ladder game for the browser, based on the Roblox game "Change a Letter". Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/appiemaster/laddle/blob/main/src/game/words4.ts](https://github.com/appiemaster/laddle/blob/main/src/game/words4.ts)
- [https://github.com/appiemaster/laddle/commit/ce010b7730e49f5ac85e9fa8a855d523393ad8fa](https://github.com/appiemaster/laddle/commit/ce010b7730e49f5ac85e9fa8a855d523393ad8fa)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/appiemaster/laddle

[Back to the awesome list](../../README.md)
