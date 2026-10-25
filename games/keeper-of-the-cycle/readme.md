# Keeper of the Cycle

> Verified game note.

![Keeper of the Cycle screenshot placeholder](keeper-of-the-cycle-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/bliksa/keeper](https://github.com/bliksa/keeper)
- **Evidence:** [direct model evidence](https://github.com/bliksa/keeper/commit/465f4c9d8cbb20916fe23bcd6c2ed8b4df362af9)
- **Live demo:** [open demo](https://bliksa.github.io/keeper/)
- **Additional live link:** [open demo](https://bliksa.github.io/keeper/original/)
- **Additional live link:** [open demo](https://bliksa.github.io/keeper/v1/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Hra o cykle, kŕčoch a dýchaní. Pôvodný webový prototyp (web-export/) je. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bliksa/keeper/blob/claude/lucid-meitner-byi1m0/web-export/index.html](https://github.com/bliksa/keeper/blob/claude/lucid-meitner-byi1m0/web-export/index.html)
- [https://github.com/bliksa/keeper/commit/465f4c9d8cbb20916fe23bcd6c2ed8b4df362af9](https://github.com/bliksa/keeper/commit/465f4c9d8cbb20916fe23bcd6c2ed8b4df362af9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/bliksa/keeper

[Back to the awesome list](../../README.md)
