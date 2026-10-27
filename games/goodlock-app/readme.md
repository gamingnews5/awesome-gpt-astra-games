# Goodlock app

> Verified game note.

![Goodlock app screenshot placeholder](goodlock-app-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Flutter, Dart
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Nathleb/Goodlock-client](https://github.com/Nathleb/Goodlock-client)
- **Evidence:** [direct model evidence](https://github.com/Nathleb/Goodlock-client/commit/29a0da76616839ae6195fe977e642e9a5442eb6c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Mobile client (Flutter + Flame) for Goodlock, a tactical PvP dice game. The backend lives in. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Nathleb/Goodlock-client/blob/main/lib/game/resolve_game.dart](https://github.com/Nathleb/Goodlock-client/blob/main/lib/game/resolve_game.dart)
- [https://github.com/Nathleb/Goodlock-client/commit/29a0da76616839ae6195fe977e642e9a5442eb6c](https://github.com/Nathleb/Goodlock-client/commit/29a0da76616839ae6195fe977e642e9a5442eb6c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Nathleb/Goodlock-client

[Back to the awesome list](../../README.md)
