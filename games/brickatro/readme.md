# Brickatro

> Verified game note.

![Brickatro screenshot](https://raw.githubusercontent.com/drschizzo/brickatro/main/docs/screenshots/gameplay.jpg)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/drschizzo/brickatro/blob/main/docs/screenshots/gameplay.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/drschizzo/brickatro](https://github.com/drschizzo/brickatro)
- **Evidence:** [direct model evidence](https://github.com/drschizzo/brickatro/commit/094179af667c7848c12f1a45715768badfd46dd3)
- **Live demo:** [open demo](https://drschizzo.github.io/brickatro/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/drschizzo/brickatro/blob/main/docs/screenshots/gameplay.jpg) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Neon brick-breaker field with ball trail and side upgrade panels.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Casse-briques roguelike inspiré de Balatro : chaque brique est une carte (couleur et valeur de 1 à 10), et les briques cassées forment une main de poker qui rapporte des points. Le jeu tourne dans le navigateur, sur ordinateur et sur mobile. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/drschizzo/brickatro/blob/main/bench/bot.ts](https://github.com/drschizzo/brickatro/blob/main/bench/bot.ts)
- [https://github.com/drschizzo/brickatro/commit/094179af667c7848c12f1a45715768badfd46dd3](https://github.com/drschizzo/brickatro/commit/094179af667c7848c12f1a45715768badfd46dd3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/drschizzo/brickatro

[Back to the awesome list](../../README.md)
