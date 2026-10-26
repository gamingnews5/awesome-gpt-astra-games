# Puzzles

> Verified game note.

![Puzzles screenshot placeholder](puzzles-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/joclegg/puzzles-android](https://github.com/joclegg/puzzles-android)
- **Evidence:** [direct model evidence](https://github.com/joclegg/puzzles-android/commit/b23b0bd4a893636fbf7958d59db4acb3f3e6f2bf)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Offline puzzle games for Android: sudoku and solitaire. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/joclegg/puzzles-android/blob/main/sudoku/ui/src/main/kotlin/com/joclegg/puzzles/sudoku/core/ui/SudokuBoard.kt](https://github.com/joclegg/puzzles-android/blob/main/sudoku/ui/src/main/kotlin/com/joclegg/puzzles/sudoku/core/ui/SudokuBoard.kt)
- [https://github.com/joclegg/puzzles-android/commit/b23b0bd4a893636fbf7958d59db4acb3f3e6f2bf](https://github.com/joclegg/puzzles-android/commit/b23b0bd4a893636fbf7958d59db4acb3f3e6f2bf)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/joclegg/puzzles-android

[Back to the awesome list](../../README.md)
