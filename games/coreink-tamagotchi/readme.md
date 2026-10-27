# CoreInk Tamagotchi

> Verified game note.

![CoreInk Tamagotchi screenshot](https://raw.githubusercontent.com/cmaranes/coreink-tamagotchi/main/docs/screenshots/home.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.2/10 ([manually reviewed image](https://github.com/cmaranes/coreink-tamagotchi/blob/main/docs/screenshots/home.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/cmaranes/coreink-tamagotchi](https://github.com/cmaranes/coreink-tamagotchi)
- **Evidence:** [direct model evidence](https://github.com/cmaranes/coreink-tamagotchi/commit/12db76cfc9f3c4a7807c571052b95a6d6af885e0)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/cmaranes/coreink-tamagotchi/blob/main/docs/screenshots/home.png) — 📸 5.2/10 · manual visual review · Use this frame for the game-level score. 1-bit e-ink pet with icons bar; charming monochrome look.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Tamagotchi-style virtual pet for the M5Stack CoreInk e-ink board, with a PC simulator. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cmaranes/coreink-tamagotchi/blob/main/src/ui/render.cpp](https://github.com/cmaranes/coreink-tamagotchi/blob/main/src/ui/render.cpp)
- [https://github.com/cmaranes/coreink-tamagotchi/commit/12db76cfc9f3c4a7807c571052b95a6d6af885e0](https://github.com/cmaranes/coreink-tamagotchi/commit/12db76cfc9f3c4a7807c571052b95a6d6af885e0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/cmaranes/coreink-tamagotchi

[Back to the awesome list](../../README.md)
