# Color Rush

> Verified game note.

![Color Rush screenshot placeholder](color-rush-salmanabdallah89-color-rush-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/salmanabdallah89/Color-Rush](https://github.com/salmanabdallah89/Color-Rush)
- **Evidence:** [direct model evidence](https://github.com/salmanabdallah89/Color-Rush/commit/db7d99dba2f03adc6d565c82052ab3a34e9e1dd9)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An original drop-and-chain color puzzle for Android (iOS-ready architecture), built in Unity 6 (6000.0 LTS or newer). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/salmanabdallah89/Color-Rush/blob/main/Assets/ColorRush/Scripts/Runtime/UI/Screens/GameScreen.cs](https://github.com/salmanabdallah89/Color-Rush/blob/main/Assets/ColorRush/Scripts/Runtime/UI/Screens/GameScreen.cs)
- [https://github.com/salmanabdallah89/Color-Rush/commit/db7d99dba2f03adc6d565c82052ab3a34e9e1dd9](https://github.com/salmanabdallah89/Color-Rush/commit/db7d99dba2f03adc6d565c82052ab3a34e9e1dd9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/salmanabdallah89/Color-Rush

[Back to the awesome list](../../README.md)
