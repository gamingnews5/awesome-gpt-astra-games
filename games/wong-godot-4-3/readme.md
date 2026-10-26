# Wong (Godot 4.3)

> Verified game note.

![Wong (Godot 4.3) screenshot](https://raw.githubusercontent.com/Ipodjockey/pong/main/title_screen.png)

## At a glance

- **Score:** 6.8/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/Ipodjockey/pong/blob/main/title_screen.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Ipodjockey/pong](https://github.com/Ipodjockey/pong)
- **Evidence:** [direct model evidence](https://github.com/Ipodjockey/pong/commit/6f063b08331868b1505bf10ef061e51ea4300d61)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Ipodjockey/pong/blob/main/title_screen.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Black Pong menu with four options; plain but clear.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Open this folder in Godot 4.3+ (project.godot) and press F5. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Ipodjockey/pong/blob/main/tools/store_art.py](https://github.com/Ipodjockey/pong/blob/main/tools/store_art.py)
- [https://github.com/Ipodjockey/pong/commit/6f063b08331868b1505bf10ef061e51ea4300d61](https://github.com/Ipodjockey/pong/commit/6f063b08331868b1505bf10ef061e51ea4300d61)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Ipodjockey/pong

[Back to the awesome list](../../README.md)
