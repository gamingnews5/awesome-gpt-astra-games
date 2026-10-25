# Shape Inventory

> Verified game note.

![Shape Inventory screenshot placeholder](shape-inventory-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/DaniilCoolUkraine/minijam_222](https://github.com/DaniilCoolUkraine/minijam_222)
- **Evidence:** [direct model evidence](https://github.com/DaniilCoolUkraine/minijam_222/commit/d1cafe4219b6349acc44aee6076cb4f54771691e)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A small Unity (uGUI, C#, WebGL only) puzzle game built around Tetris-shaped items. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/DaniilCoolUkraine/minijam_222/blob/main/Tools/verify_levels.py](https://github.com/DaniilCoolUkraine/minijam_222/blob/main/Tools/verify_levels.py)
- [https://github.com/DaniilCoolUkraine/minijam_222/commit/d1cafe4219b6349acc44aee6076cb4f54771691e](https://github.com/DaniilCoolUkraine/minijam_222/commit/d1cafe4219b6349acc44aee6076cb4f54771691e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/DaniilCoolUkraine/minijam_222

[Back to the awesome list](../../README.md)
