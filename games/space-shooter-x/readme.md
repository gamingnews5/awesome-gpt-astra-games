# Space Shooter X

> Verified game note.

![Space Shooter X screenshot placeholder](space-shooter-x-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/guetgr/SpaceShooterX](https://github.com/guetgr/SpaceShooterX)
- **Evidence:** [direct model evidence](https://github.com/guetgr/SpaceShooterX/commit/fecb503297b4a384f0e70930222417e900a3bd29)
- **Live demo:** [open demo](https://spaceshooterx-swart.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jeu de tir spatial (type Raiden / Vampire Survivors : runs infinies, boss, arbre de compétences), en Phaser 3, pensé pour Android / Google Play. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/guetgr/SpaceShooterX/blob/main/sources/images-uploads/ui-vrai-jeu.html](https://github.com/guetgr/SpaceShooterX/blob/main/sources/images-uploads/ui-vrai-jeu.html)
- [https://github.com/guetgr/SpaceShooterX/commit/fecb503297b4a384f0e70930222417e900a3bd29](https://github.com/guetgr/SpaceShooterX/commit/fecb503297b4a384f0e70930222417e900a3bd29)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/guetgr/SpaceShooterX

[Back to the awesome list](../../README.md)
