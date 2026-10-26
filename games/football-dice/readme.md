# Football Dice

> Verified game note.

![Football Dice screenshot placeholder](football-dice-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/evanstom273/Claude-test-III](https://github.com/evanstom273/Claude-test-III)
- **Evidence:** [direct model evidence](https://github.com/evanstom273/Claude-test-III/commit/2401fae6dafce9e585ba14a8f38f6dca84ebf6c8)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A football game where you play as one player in a fully simulated match. Every player on the pitch, on both sides, has the same ten stats and goes through the same dice. When the play reaches you, the clock stops and you make the call. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/evanstom273/Claude-test-III/blob/main/src/game/match.ts](https://github.com/evanstom273/Claude-test-III/blob/main/src/game/match.ts)
- [https://github.com/evanstom273/Claude-test-III/commit/2401fae6dafce9e585ba14a8f38f6dca84ebf6c8](https://github.com/evanstom273/Claude-test-III/commit/2401fae6dafce9e585ba14a8f38f6dca84ebf6c8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/evanstom273/Claude-test-III

[Back to the awesome list](../../README.md)
