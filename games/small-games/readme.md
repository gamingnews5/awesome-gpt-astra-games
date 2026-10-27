# Small Games

> Verified game note.

![Small Games screenshot](https://raw.githubusercontent.com/ghostinmachinefr/small-games/main/site/images/snake.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 4.4/10 ([manually reviewed image](https://github.com/ghostinmachinefr/small-games/blob/main/site/images/snake.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/ghostinmachinefr/small-games](https://github.com/ghostinmachinefr/small-games)
- **Evidence:** [direct model evidence](https://github.com/ghostinmachinefr/small-games/commit/7081f126c3579d98b0156299b195f943c496f54c)
- **Live demo:** [open demo](https://gandalfgames.netlify.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ghostinmachinefr/small-games/blob/main/site/images/snake.png) — 📸 4.4/10 · manual visual review · Use this frame for the game-level score. Simple snake on dark grid with score; minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

2D games built in Python + Pygame, playable in the browser, with a suggestion box for the next game. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ghostinmachinefr/small-games/blob/main/site/games/flappy_bird/index.html](https://github.com/ghostinmachinefr/small-games/blob/main/site/games/flappy_bird/index.html)
- [https://github.com/ghostinmachinefr/small-games/commit/7081f126c3579d98b0156299b195f943c496f54c](https://github.com/ghostinmachinefr/small-games/commit/7081f126c3579d98b0156299b195f943c496f54c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/ghostinmachinefr/small-games

[Back to the awesome list](../../README.md)
