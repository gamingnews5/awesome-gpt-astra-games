# Minesweeper: Something Moves

> Verified game note.

![Minesweeper: Something Moves screenshot](https://raw.githubusercontent.com/LuisCa32/minesweeper-something-moves/main/preview.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/LuisCa32/minesweeper-something-moves/blob/main/preview.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/LuisCa32/minesweeper-something-moves](https://github.com/LuisCa32/minesweeper-something-moves)
- **Evidence:** [direct model evidence](https://github.com/LuisCa32/minesweeper-something-moves/commit/b2f6a0a50a162b3aa6815af871afcf1ce6fb56e9)
- **Live demo:** [open demo](https://luisca32.github.io/minesweeper-something-moves/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/LuisCa32/minesweeper-something-moves/blob/main/preview.png) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. Halloween minesweeper title with numbered board and mine monster; crisp pixel style.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A mobile-first Halloween Minesweeper where the mines move. Under the tiles crawl Mine Monsters: each one counts as a mine wherever it is, so every time they move, the numbers next to them change. Lure them out, then use TNT to launch them into pumpkins. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/LuisCa32/minesweeper-something-moves/blob/main/index.html](https://github.com/LuisCa32/minesweeper-something-moves/blob/main/index.html)
- [https://github.com/LuisCa32/minesweeper-something-moves/commit/b2f6a0a50a162b3aa6815af871afcf1ce6fb56e9](https://github.com/LuisCa32/minesweeper-something-moves/commit/b2f6a0a50a162b3aa6815af871afcf1ce6fb56e9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/LuisCa32/minesweeper-something-moves

[Back to the awesome list](../../README.md)
