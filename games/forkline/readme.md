# Forkline

> Verified game note.

![Forkline screenshot](https://raw.githubusercontent.com/bartbasi/forkline/main/docs/art/cover_actual_size.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/bartbasi/forkline/blob/main/docs/art/cover_actual_size.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/bartbasi/forkline](https://github.com/bartbasi/forkline)
- **Evidence:** [direct model evidence](https://github.com/bartbasi/forkline/commit/e0099d7d78a9dcdcd51bf6b608e7609365dec0fe)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/bartbasi/forkline/blob/main/docs/art/cover_actual_size.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Pixel creature and tower sprite sheet on cream; tidy asset art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Forkline: a tower defense game for Android, built in Godot. Free, offline, no ads, no tracking. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/bartbasi/forkline/blob/main/src/sim/battle.gd](https://github.com/bartbasi/forkline/blob/main/src/sim/battle.gd)
- [https://github.com/bartbasi/forkline/commit/e0099d7d78a9dcdcd51bf6b608e7609365dec0fe](https://github.com/bartbasi/forkline/commit/e0099d7d78a9dcdcd51bf6b608e7609365dec0fe)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/bartbasi/forkline

[Back to the awesome list](../../README.md)
