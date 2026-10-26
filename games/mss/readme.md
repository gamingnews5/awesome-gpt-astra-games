# MSS

> Verified game note.

![MSS screenshot placeholder](mss-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/HermanRas/MobileSpaceShooter](https://github.com/HermanRas/MobileSpaceShooter)
- **Evidence:** [direct model evidence](https://github.com/HermanRas/MobileSpaceShooter/commit/340f8056b201f790f54957fa9435672898f48c82)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Mobile Space Shooter is a triditional Space Arcade Shooter. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/HermanRas/MobileSpaceShooter/blob/main/game/src/ui/hangar/hangar.gd](https://github.com/HermanRas/MobileSpaceShooter/blob/main/game/src/ui/hangar/hangar.gd)
- [https://github.com/HermanRas/MobileSpaceShooter/commit/340f8056b201f790f54957fa9435672898f48c82](https://github.com/HermanRas/MobileSpaceShooter/commit/340f8056b201f790f54957fa9435672898f48c82)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/HermanRas/MobileSpaceShooter

[Back to the awesome list](../../README.md)
