# Super Giorgi: Batumi

> Verified game note.

![Super Giorgi: Batumi screenshot](https://raw.githubusercontent.com/gogodzilla/super-giorgi/main/docs/street.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/gogodzilla/super-giorgi/blob/main/docs/street.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/gogodzilla/super-giorgi](https://github.com/gogodzilla/super-giorgi)
- **Evidence:** [direct model evidence](https://github.com/gogodzilla/super-giorgi/commit/1c228bf13061220e72c8a61761c14c3cd14ca51a)
- **Live demo:** [open demo](https://super.malets.by)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/gogodzilla/super-giorgi/blob/main/docs/street.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Pixel city street with towers and HUD in Mario style; cheerful and detailed.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Pixel-art platformer on the streets of Batumi, in the spirit of Super Mario: jump over Prius taxis, befriend stray dogs, eat khachapuri. No build, no assets. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/gogodzilla/super-giorgi/blob/main/game.js](https://github.com/gogodzilla/super-giorgi/blob/main/game.js)
- [https://github.com/gogodzilla/super-giorgi/commit/1c228bf13061220e72c8a61761c14c3cd14ca51a](https://github.com/gogodzilla/super-giorgi/commit/1c228bf13061220e72c8a61761c14c3cd14ca51a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/gogodzilla/super-giorgi

[Back to the awesome list](../../README.md)
