# Derby Day

> Verified game note.

![Derby Day screenshot placeholder](derby-day-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/zuzivian/derby-day](https://github.com/zuzivian/derby-day)
- **Evidence:** [direct model evidence](https://github.com/zuzivian/derby-day/commit/9998150c224aeb5c347657de2dfb444ad6510a06)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser football club manager where you also play the matches yourself, mouse-first. You run a generated club (squad, transfers, training, an Elo ladder) and play eleven-a-side matches in real time against the CPU, under the Laws of the Game: throw-ins,… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/zuzivian/derby-day/blob/main/src/sim/ai.ts](https://github.com/zuzivian/derby-day/blob/main/src/sim/ai.ts)
- [https://github.com/zuzivian/derby-day/commit/9998150c224aeb5c347657de2dfb444ad6510a06](https://github.com/zuzivian/derby-day/commit/9998150c224aeb5c347657de2dfb444ad6510a06)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/zuzivian/derby-day

[Back to the awesome list](../../README.md)
