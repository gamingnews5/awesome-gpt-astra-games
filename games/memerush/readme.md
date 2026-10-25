# Memerush

> Verified game note.

![Memerush screenshot](https://raw.githubusercontent.com/sayinel/MemeRush/main/docs/media/banner.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/sayinel/MemeRush/blob/main/docs/media/banner.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Python, Phaser, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/sayinel/MemeRush](https://github.com/sayinel/MemeRush)
- **Evidence:** [direct model evidence](https://github.com/sayinel/MemeRush/commit/e6755382742c631d8917f27d4138e6fcd28c24e9)
- **Live demo:** [open demo](https://meme-rush-kappa.vercel.app)
- **Additional live link:** [open demo](https://meme-rush-meme-rush.vercel.app/)
- **Additional live link:** [open demo](https://meme-rush-meme-rush.vercel.app/admin)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/sayinel/MemeRush/blob/main/docs/media/banner.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Bold Meme Rush promo banner with phone mock-ups; clean marketing art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Stop the clock as close to the target as you can. Send the result. Beat your friends by 0.01s. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/sayinel/MemeRush/blob/main/web/src/game/TimingStopScene.ts](https://github.com/sayinel/MemeRush/blob/main/web/src/game/TimingStopScene.ts)
- [https://github.com/sayinel/MemeRush/commit/e6755382742c631d8917f27d4138e6fcd28c24e9](https://github.com/sayinel/MemeRush/commit/e6755382742c631d8917f27d4138e6fcd28c24e9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/sayinel/MemeRush

[Back to the awesome list](../../README.md)
