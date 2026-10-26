# Spirit Battle (Roblox)

> Verified game note.

![Spirit Battle (Roblox) screenshot](https://raw.githubusercontent.com/skyler-lab/spirit-battle/main/docs/img/base-island-top.jpg)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/skyler-lab/spirit-battle/blob/main/docs/img/base-island-top.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Roblox, Luau
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/skyler-lab/spirit-battle](https://github.com/skyler-lab/spirit-battle)
- **Evidence:** [direct model evidence](https://github.com/skyler-lab/spirit-battle/commit/62121d3a8dd6faa8440580005c1e4308140777f5)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/skyler-lab/spirit-battle/blob/main/docs/img/base-island-top.jpg) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Top-down arena of green dice-like tiles around a center ring; flat and sparse.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Prodigy-style spirit battle game. The place file is Place1.rbxl, which lives in. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/skyler-lab/spirit-battle/blob/main/src/ReplicatedStorage/BattleFXPack/FX.luau](https://github.com/skyler-lab/spirit-battle/blob/main/src/ReplicatedStorage/BattleFXPack/FX.luau)
- [https://github.com/skyler-lab/spirit-battle/commit/62121d3a8dd6faa8440580005c1e4308140777f5](https://github.com/skyler-lab/spirit-battle/commit/62121d3a8dd6faa8440580005c1e4308140777f5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/skyler-lab/spirit-battle

[Back to the awesome list](../../README.md)
