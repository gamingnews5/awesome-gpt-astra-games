# 쇼크 히어로: 몬스터 브레이커

> Verified game note.

![쇼크 히어로: 몬스터 브레이커 screenshot](https://raw.githubusercontent.com/ppakku/shock-hero/main/docs/astranova_scene.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/ppakku/shock-hero/blob/main/docs/astranova_scene.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/ppakku/shock-hero](https://github.com/ppakku/shock-hero)
- **Evidence:** [direct model evidence](https://github.com/ppakku/shock-hero/commit/d7b3e9bd55323f2f827bf8ba48b0da2a086feb18)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ppakku/shock-hero/blob/main/docs/astranova_scene.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Painted red dragon over a lava landscape; vivid key art, not gameplay.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

도시를 부수는 돌연변이 괴물과 싸우는 2D 액션 게임입니다. 브라우저에서 바로 플레이할 수 있습니다. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ppakku/shock-hero/blob/main/src/boss/FrostAstraBoss.js](https://github.com/ppakku/shock-hero/blob/main/src/boss/FrostAstraBoss.js)
- [https://github.com/ppakku/shock-hero/commit/d7b3e9bd55323f2f827bf8ba48b0da2a086feb18](https://github.com/ppakku/shock-hero/commit/d7b3e9bd55323f2f827bf8ba48b0da2a086feb18)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/ppakku/shock-hero

[Back to the awesome list](../../README.md)
