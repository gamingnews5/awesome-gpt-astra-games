# Jetstrike

> Verified game note.

![Jetstrike screenshot placeholder](jetstrike-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Xcluice/Jetstrike](https://github.com/Xcluice/Jetstrike)
- **Evidence:** [direct model evidence](https://github.com/Xcluice/Jetstrike/commit/d56b2cc789216f75f3eaa781733f10a0360e3ec5)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jetstrike Original jetpack deathmatch for Android. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Xcluice/Jetstrike/blob/main/app/src/main/java/com/xcluice/jetstrike/GameView.kt](https://github.com/Xcluice/Jetstrike/blob/main/app/src/main/java/com/xcluice/jetstrike/GameView.kt)
- [https://github.com/Xcluice/Jetstrike/commit/d56b2cc789216f75f3eaa781733f10a0360e3ec5](https://github.com/Xcluice/Jetstrike/commit/d56b2cc789216f75f3eaa781733f10a0360e3ec5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Xcluice/Jetstrike

[Back to the awesome list](../../README.md)
