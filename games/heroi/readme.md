# Heroi (ГЕРОЇ)

> Verified game note.

![Heroi (ГЕРОЇ) screenshot](https://raw.githubusercontent.com/aleszorc/heroi/main/docs/screenshots/battle.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/aleszorc/heroi/blob/main/docs/screenshots/battle.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Fable 5.1
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/aleszorc/heroi](https://github.com/aleszorc/heroi)
- **Evidence:** [direct model evidence](https://github.com/aleszorc/heroi/commit/909e381b98cd6a5bea1126a27318fde0ffbde779)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/aleszorc/heroi/blob/main/docs/screenshots/battle.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Isometric war-zone farmstead with unit HUD; detailed tactics view.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Mobile isometric real-time tactics in the Russo-Ukrainian war — Godot 4.7, fully procedural. Dedicated to Ukrainian heroes. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/aleszorc/heroi/blob/main/scripts/art/mesh_factory.gd](https://github.com/aleszorc/heroi/blob/main/scripts/art/mesh_factory.gd)
- [https://github.com/aleszorc/heroi/commit/909e381b98cd6a5bea1126a27318fde0ffbde779](https://github.com/aleszorc/heroi/commit/909e381b98cd6a5bea1126a27318fde0ffbde779)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/aleszorc/heroi

[Back to the awesome list](../../README.md)
