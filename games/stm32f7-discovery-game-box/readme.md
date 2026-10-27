# STM32F7 Discovery GAME BOX

> Top-list entry: **today** (#6).

![STM32F7 Discovery GAME BOX screenshot](https://raw.githubusercontent.com/onurkepenek/stm32f7disco_gamebox/main/docs/menu.png)

## At a glance

- **Score:** 8.2/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/onurkepenek/stm32f7disco_gamebox/blob/main/docs/menu.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/onurkepenek/stm32f7disco_gamebox](https://github.com/onurkepenek/stm32f7disco_gamebox)
- **Evidence:** [direct model evidence](https://github.com/onurkepenek/stm32f7disco_gamebox/commit/5ab1a208d50a794c4a7b02ca1c91ff15aa5b7c58)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/onurkepenek/stm32f7disco_gamebox/blob/main/docs/menu.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Neon GAME BOX selection screen with colourful game tiles; bright and clear.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

STM32F746G-DISCO kartının 4.3" dokunmatik ekranı için oyun koleksiyonu. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/onurkepenek/stm32f7disco_gamebox/blob/main/Drivers/CMSIS/Device/ST/STM32F7xx/Include/stm32f746xx.h](https://github.com/onurkepenek/stm32f7disco_gamebox/blob/main/Drivers/CMSIS/Device/ST/STM32F7xx/Include/stm32f746xx.h)
- [https://github.com/onurkepenek/stm32f7disco_gamebox/commit/5ab1a208d50a794c4a7b02ca1c91ff15aa5b7c58](https://github.com/onurkepenek/stm32f7disco_gamebox/commit/5ab1a208d50a794c4a7b02ca1c91ff15aa5b7c58)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/onurkepenek/stm32f7disco_gamebox

[Back to the awesome list](../../README.md)
