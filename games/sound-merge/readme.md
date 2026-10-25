# Sound Merge

> Verified game note.

![Sound Merge screenshot placeholder](sound-merge-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/brodypark/MemeSoundGame](https://github.com/brodypark/MemeSoundGame)
- **Evidence:** [direct model evidence](https://github.com/brodypark/MemeSoundGame/commit/8f3214d102475d85b0f91320b82d3ded06dca851)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser game: record or upload a short sound, the app figures out what it is (YAMNet), generates a 6-stage "glow-up" of that thing, and you play a Suika-style merge game with it. Every merge goes up a tier and plays the sound lower. Lower pitch = more sigma. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/brodypark/MemeSoundGame/blob/main/src/main.js](https://github.com/brodypark/MemeSoundGame/blob/main/src/main.js)
- [https://github.com/brodypark/MemeSoundGame/commit/8f3214d102475d85b0f91320b82d3ded06dca851](https://github.com/brodypark/MemeSoundGame/commit/8f3214d102475d85b0f91320b82d3ded06dca851)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/brodypark/MemeSoundGame

[Back to the awesome list](../../README.md)
