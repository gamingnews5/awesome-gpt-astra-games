# Shoot

> Verified game note.

![Shoot screenshot placeholder](shoot-placeholder.svg)

## At a glance

- **Score:** 6.8/10
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/davejef/shooter](https://github.com/davejef/shooter)
- **Evidence:** [direct model evidence](https://github.com/davejef/shooter/commit/dfd6cee99a072e61109d18fc6a61682f75d54e95)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A two-player, Asteroids-style ship duel written in Python with pygame. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/davejef/shooter/blob/main/shoot/game.py](https://github.com/davejef/shooter/blob/main/shoot/game.py)
- [https://github.com/davejef/shooter/commit/dfd6cee99a072e61109d18fc6a61682f75d54e95](https://github.com/davejef/shooter/commit/dfd6cee99a072e61109d18fc6a61682f75d54e95)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/davejef/shooter

[Back to the awesome list](../../README.md)
