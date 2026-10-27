# CyberSweeper

> Verified game note.

![CyberSweeper screenshot](https://raw.githubusercontent.com/jwelch00/CyberSweeper/main/design/png/gameplay-critical.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/jwelch00/CyberSweeper/blob/main/design/png/gameplay-critical.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/jwelch00/CyberSweeper](https://github.com/jwelch00/CyberSweeper)
- **Evidence:** [direct model evidence](https://github.com/jwelch00/CyberSweeper/commit/06414884160ced1c07c3b015554ef541090281bc)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jwelch00/CyberSweeper/blob/main/design/png/gameplay-critical.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Neon cyberpunk minesweeper grid with score; distinct style.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Cyberpunk-style infinite minesweeper game, made with Claude. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jwelch00/CyberSweeper/blob/main/design/shared/fx.js](https://github.com/jwelch00/CyberSweeper/blob/main/design/shared/fx.js)
- [https://github.com/jwelch00/CyberSweeper/commit/06414884160ced1c07c3b015554ef541090281bc](https://github.com/jwelch00/CyberSweeper/commit/06414884160ced1c07c3b015554ef541090281bc)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/jwelch00/CyberSweeper

[Back to the awesome list](../../README.md)
