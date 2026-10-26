# Dino Run

> Verified game note.

![Dino Run screenshot](https://raw.githubusercontent.com/meuse24/DinoRun/master/assets/images/dino.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/meuse24/DinoRun/blob/master/assets/images/dino.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/meuse24/DinoRun](https://github.com/meuse24/DinoRun)
- **Evidence:** [direct model evidence](https://github.com/meuse24/DinoRun/commit/e3c742dc133029371accce674d65f6f9a5c1ae58)
- **Live demo:** [open demo](https://meuse24.info/apps/dino/dino.html)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/meuse24/DinoRun/blob/master/assets/images/dino.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Dino-Pause banner with cartoon dinosaur and play button; simple promo.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Dino Run – arcade take on Chrome's T-Rex runner in one self-contained, offline-capable HTML file: power-ups, rock boss, lives, highscores, PWA and Android TWA. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/meuse24/DinoRun/blob/master/dino.html](https://github.com/meuse24/DinoRun/blob/master/dino.html)
- [https://github.com/meuse24/DinoRun/commit/e3c742dc133029371accce674d65f6f9a5c1ae58](https://github.com/meuse24/DinoRun/commit/e3c742dc133029371accce674d65f6f9a5c1ae58)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/meuse24/DinoRun

[Back to the awesome list](../../README.md)
