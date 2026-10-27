# Word Scramble

> Verified game note.

![Word Scramble screenshot placeholder](word-scramble-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Sonnet 5.5
- **Technology:** PLpgSQL, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/GenAK79/WordScramble](https://github.com/GenAK79/WordScramble)
- **Evidence:** [direct model evidence](https://github.com/GenAK79/WordScramble/commit/f53e6f95fcb237eaedde22eecfb05b3c5d495c4d)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Simple implementation of well-known classic word game. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GenAK79/WordScramble/blob/main/src/components/GameScreen.jsx](https://github.com/GenAK79/WordScramble/blob/main/src/components/GameScreen.jsx)
- [https://github.com/GenAK79/WordScramble/commit/f53e6f95fcb237eaedde22eecfb05b3c5d495c4d](https://github.com/GenAK79/WordScramble/commit/f53e6f95fcb237eaedde22eecfb05b3c5d495c4d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/GenAK79/WordScramble

[Back to the awesome list](../../README.md)
