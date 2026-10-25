# yajirushi

> Verified game note.

![yajirushi screenshot placeholder](yajirushi-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** Flutter, Dart
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/Zacherl/yajirushi](https://github.com/Zacherl/yajirushi)
- **Evidence:** [direct model evidence](https://github.com/Zacherl/yajirushi/commit/f4fdb188c42e5dbccc61be3bdcea4b26ba93bbfe)
- **Live demo:** [open demo](https://zacherl.github.io/yajirushi/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Arrow puzzle game: tap the arrows out of the grid without crashing them. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Zacherl/yajirushi/blob/main/lib/game/generator.dart](https://github.com/Zacherl/yajirushi/blob/main/lib/game/generator.dart)
- [https://github.com/Zacherl/yajirushi/commit/f4fdb188c42e5dbccc61be3bdcea4b26ba93bbfe](https://github.com/Zacherl/yajirushi/commit/f4fdb188c42e5dbccc61be3bdcea4b26ba93bbfe)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/Zacherl/yajirushi

[Back to the awesome list](../../README.md)
