# Mt. Crankmore

> Verified game note.

![Mt. Crankmore screenshot](https://raw.githubusercontent.com/hermeslohin/mt-crankmore/main/docs/delivery.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 6.6/10 ([manually reviewed image](https://github.com/hermeslohin/mt-crankmore/blob/main/docs/delivery.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/hermeslohin/mt-crankmore](https://github.com/hermeslohin/mt-crankmore)
- **Evidence:** [direct model evidence](https://github.com/hermeslohin/mt-crankmore/commit/19873d25ef76d6ce7b72ea20fe39e87c1f6a15ba)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/hermeslohin/mt-crankmore/blob/main/docs/delivery.png) — 📸 6.6/10 · manual visual review · Use this frame for the game-level score. Isometric pixel town with a cyclist delivering pizza and trainer HUD; detailed and readable.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Mt. Crankmore: an isometric pizza-delivery cycling game in Godot, ridden with a smart trainer and Zwift Ride controllers. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hermeslohin/mt-crankmore/blob/main/scripts/city.gd](https://github.com/hermeslohin/mt-crankmore/blob/main/scripts/city.gd)
- [https://github.com/hermeslohin/mt-crankmore/commit/19873d25ef76d6ce7b72ea20fe39e87c1f6a15ba](https://github.com/hermeslohin/mt-crankmore/commit/19873d25ef76d6ce7b72ea20fe39e87c1f6a15ba)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/hermeslohin/mt-crankmore

[Back to the awesome list](../../README.md)
