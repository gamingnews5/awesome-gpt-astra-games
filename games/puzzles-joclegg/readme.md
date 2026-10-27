# Puzzles (joclegg)

> Verified game note.

![Puzzles (joclegg) screenshot](https://raw.githubusercontent.com/joclegg/puzzles-web/main/src/views/FiveLettersGameView/__e2e__/__snapshots__/daily-guess-desktop-darwin.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/joclegg/puzzles-web/blob/main/src/views/FiveLettersGameView/__e2e__/__snapshots__/daily-guess-desktop-darwin.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/joclegg/puzzles-web](https://github.com/joclegg/puzzles-web)
- **Evidence:** [direct model evidence](https://github.com/joclegg/puzzles-web/commit/aadfaf9c29f4d8efa92a566f86a4745f4a695544)
- **Live demo:** [open demo](https://joclegg.github.io/puzzles-web/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/joclegg/puzzles-web/blob/main/src/views/FiveLettersGameView/__e2e__/__snapshots__/daily-guess-desktop-darwin.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Wordle-style letter grid and keyboard on dark background; clean but minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Web version of Puzzles: eight offline puzzle games in React and TypeScript. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/joclegg/puzzles-web/blob/main/src/common/sudoku/sudokuGrader.functions.ts](https://github.com/joclegg/puzzles-web/blob/main/src/common/sudoku/sudokuGrader.functions.ts)
- [https://github.com/joclegg/puzzles-web/commit/aadfaf9c29f4d8efa92a566f86a4745f4a695544](https://github.com/joclegg/puzzles-web/commit/aadfaf9c29f4d8efa92a566f86a4745f4a695544)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/joclegg/puzzles-web

[Back to the awesome list](../../README.md)
