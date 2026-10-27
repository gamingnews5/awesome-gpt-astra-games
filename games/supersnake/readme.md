# SuperSnake

> Verified game note.

![SuperSnake screenshot placeholder](supersnake-placeholder.svg)

## At a glance

- **Score:** 6.7/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/EastwoodNo1/SuperSnake](https://github.com/EastwoodNo1/SuperSnake)
- **Evidence:** [direct model evidence](https://github.com/EastwoodNo1/SuperSnake/commit/e900708cc4f44893ea4a5bc379244cc8dae63dcd)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A neon, classic Snake game for Android phones and tablets (minSdk 31). The rules are in docs/game-rules.md. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/EastwoodNo1/SuperSnake/blob/main/scripts/github/apply-repo-settings.sh](https://github.com/EastwoodNo1/SuperSnake/blob/main/scripts/github/apply-repo-settings.sh)
- [https://github.com/EastwoodNo1/SuperSnake/commit/e900708cc4f44893ea4a5bc379244cc8dae63dcd](https://github.com/EastwoodNo1/SuperSnake/commit/e900708cc4f44893ea4a5bc379244cc8dae63dcd)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/EastwoodNo1/SuperSnake

[Back to the awesome list](../../README.md)
