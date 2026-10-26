# Solitaire

> Verified game note.

![Solitaire screenshot](https://raw.githubusercontent.com/ThomasVanRiel/solitaire/main/docs/screenshots/klondike.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 4.8/10 ([manually reviewed image](https://github.com/ThomasVanRiel/solitaire/blob/main/docs/screenshots/klondike.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Kotlin
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/ThomasVanRiel/solitaire](https://github.com/ThomasVanRiel/solitaire)
- **Evidence:** [direct model evidence](https://github.com/ThomasVanRiel/solitaire/commit/febee3e77039ae90a552e18c7a7d35affa04cf84)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ThomasVanRiel/solitaire/blob/main/docs/screenshots/klondike.png) — 📸 4.8/10 · manual visual review · Use this frame for the game-level score. Classic solitaire tableau on green felt, phone layout; clean but plain.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An open-source patience (solitaire) game for Android, with Klondike, Spider, Scorpion II, Yukon, Russian. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ThomasVanRiel/solitaire/blob/main/app/src/main/kotlin/io/github/thomasvanriel/solitaire/game/GameViewModel.kt](https://github.com/ThomasVanRiel/solitaire/blob/main/app/src/main/kotlin/io/github/thomasvanriel/solitaire/game/GameViewModel.kt)
- [https://github.com/ThomasVanRiel/solitaire/commit/febee3e77039ae90a552e18c7a7d35affa04cf84](https://github.com/ThomasVanRiel/solitaire/commit/febee3e77039ae90a552e18c7a7d35affa04cf84)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/ThomasVanRiel/solitaire

[Back to the awesome list](../../README.md)
