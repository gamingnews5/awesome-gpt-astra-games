# Tetris (zanhlahtet)

> Verified game note.

![Tetris (zanhlahtet) screenshot placeholder](tetris-zanhlahtet-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/zanhlahtet/tetris](https://github.com/zanhlahtet/tetris)
- **Evidence:** [direct model evidence](https://github.com/zanhlahtet/tetris/commit/0a29b9b812eb2db3952474dc2c9116289ad56bd0)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A faithful Tetris Guideline-style clone for iOS and Android, built with Godot 4.7. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/zanhlahtet/tetris/blob/main/src/session/game_session.gd](https://github.com/zanhlahtet/tetris/blob/main/src/session/game_session.gd)
- [https://github.com/zanhlahtet/tetris/commit/0a29b9b812eb2db3952474dc2c9116289ad56bd0](https://github.com/zanhlahtet/tetris/commit/0a29b9b812eb2db3952474dc2c9116289ad56bd0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/zanhlahtet/tetris

[Back to the awesome list](../../README.md)
