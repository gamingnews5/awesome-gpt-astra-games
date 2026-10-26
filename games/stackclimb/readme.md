# StackClimb

> Verified game note.

![StackClimb screenshot](https://raw.githubusercontent.com/GaaamJ/StackClimb/main/docs/images/09-climbed-height.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/GaaamJ/StackClimb/blob/main/docs/images/09-climbed-height.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/GaaamJ/StackClimb](https://github.com/GaaamJ/StackClimb)
- **Evidence:** [direct model evidence](https://github.com/GaaamJ/StackClimb/commit/023a31682565633f3f8fac0811815100e2531cd0)
- **Live demo:** [open demo](https://gaaamj.github.io/StackClimb/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/GaaamJ/StackClimb/blob/main/docs/images/09-climbed-height.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Low-poly coloured block stack with height counter; simple prototype.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

떨어지는 테트리미노 블록을 피하면서, 쌓인 블록을 밟고 최대한 높이 올라가는 Unity 프로토타입입니다. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/GaaamJ/StackClimb/blob/main/Assets/Scripts/FallingBlock.cs](https://github.com/GaaamJ/StackClimb/blob/main/Assets/Scripts/FallingBlock.cs)
- [https://github.com/GaaamJ/StackClimb/commit/023a31682565633f3f8fac0811815100e2531cd0](https://github.com/GaaamJ/StackClimb/commit/023a31682565633f3f8fac0811815100e2531cd0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/GaaamJ/StackClimb

[Back to the awesome list](../../README.md)
