# Top-Down Arena

> Verified game note.

![Top-Down Arena screenshot placeholder](top-down-arena-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/AleonSC/Top-down-arena](https://github.com/AleonSC/Top-down-arena)
- **Evidence:** [direct model evidence](https://github.com/AleonSC/Top-down-arena/commit/67312ee0887b70a3acbc26a9b0a637ea0cf04942)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A co-op top-down bullet hell for two players over the network, made in Unity 6. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AleonSC/Top-down-arena/blob/main/Assets/Scripts/Core/Game.cs](https://github.com/AleonSC/Top-down-arena/blob/main/Assets/Scripts/Core/Game.cs)
- [https://github.com/AleonSC/Top-down-arena/commit/67312ee0887b70a3acbc26a9b0a637ea0cf04942](https://github.com/AleonSC/Top-down-arena/commit/67312ee0887b70a3acbc26a9b0a637ea0cf04942)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/AleonSC/Top-down-arena

[Back to the awesome list](../../README.md)
