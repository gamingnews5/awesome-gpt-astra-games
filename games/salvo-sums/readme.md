# Salvo Sums

> Verified game note.

![Salvo Sums screenshot](https://raw.githubusercontent.com/Geodude117/BattleShips/main/docs/screenshots/ipad-13/1-battle.png)

## At a glance

- **Score:** 7.0/10
- **Screenshot rating:** 4.4/10 ([manually reviewed image](https://github.com/Geodude117/BattleShips/blob/main/docs/screenshots/ipad-13/1-battle.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Swift
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Geodude117/BattleShips](https://github.com/Geodude117/BattleShips)
- **Evidence:** [direct model evidence](https://github.com/Geodude117/BattleShips/commit/8a4e150d9e59bd1e9736a0f8da424699f2863c32)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Geodude117/BattleShips/blob/main/docs/screenshots/ipad-13/1-battle.png) — 📸 4.4/10 · manual visual review · Use this frame for the game-level score. Battleship grids on white page; basic but legible.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A single-player Battleships game for iPhone and iPad where every shot is earned by answering a GCSE maths question. Play against the computer, sink its fleet, and learn from a worked explanation every time you get one wrong. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Geodude117/BattleShips/blob/main/BattleMaths/Game/GameViewModel.swift](https://github.com/Geodude117/BattleShips/blob/main/BattleMaths/Game/GameViewModel.swift)
- [https://github.com/Geodude117/BattleShips/commit/8a4e150d9e59bd1e9736a0f8da424699f2863c32](https://github.com/Geodude117/BattleShips/commit/8a4e150d9e59bd1e9736a0f8da424699f2863c32)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Geodude117/BattleShips

[Back to the awesome list](../../README.md)
