# Prime Trail

> Verified game note.

![Prime Trail screenshot](https://raw.githubusercontent.com/jyyan/game-prime-trail/main/docs/design/illustrations/hero.png)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/jyyan/game-prime-trail/blob/main/docs/design/illustrations/hero.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/jyyan/game-prime-trail](https://github.com/jyyan/game-prime-trail)
- **Evidence:** [direct model evidence](https://github.com/jyyan/game-prime-trail/commit/a621a76f7362867d35bae03ed9ec3f0bfc28c4e3)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jyyan/game-prime-trail/blob/main/docs/design/illustrations/hero.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Cute dragon mascot illustration with number tiles; promo art, not gameplay.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

單人益智網頁遊戲。棋盤為 10×10，從邊緣的「龍頭」（1）出發，沿上下左右相鄰的格子依序填入 1 到 100，每格恰好走一次。灰底的格子是質數格，也是唯一的推理線索。. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jyyan/game-prime-trail/blob/main/src/composables/usePlaySession.ts](https://github.com/jyyan/game-prime-trail/blob/main/src/composables/usePlaySession.ts)
- [https://github.com/jyyan/game-prime-trail/commit/a621a76f7362867d35bae03ed9ec3f0bfc28c4e3](https://github.com/jyyan/game-prime-trail/commit/a621a76f7362867d35bae03ed9ec3f0bfc28c4e3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/jyyan/game-prime-trail

[Back to the awesome list](../../README.md)
