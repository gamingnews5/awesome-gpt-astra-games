# 인생게임 웹

> Verified game note.

![인생게임 웹 screenshot](https://raw.githubusercontent.com/selfer08/life-game/main/docs/screenshots/3-game.png)

## At a glance

- **Score:** 7.0/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/selfer08/life-game/blob/main/docs/screenshots/3-game.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/selfer08/life-game](https://github.com/selfer08/life-game)
- **Evidence:** [direct model evidence](https://github.com/selfer08/life-game/commit/31e827f58b9916702e0dec010bdbfb9cb292ac5a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/selfer08/life-game/blob/main/docs/screenshots/3-game.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Colourful life board path with spinner and side panels; busy but clear.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

보드게임 "인생게임"을 웹으로 옮긴 프로젝트입니다. 방을 만들고 코드로 친구를 초대해 실시간으로 함께 플레이할 수 있어요. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/selfer08/life-game/blob/main/server/src/game/engine.ts](https://github.com/selfer08/life-game/blob/main/server/src/game/engine.ts)
- [https://github.com/selfer08/life-game/commit/31e827f58b9916702e0dec010bdbfb9cb292ac5a](https://github.com/selfer08/life-game/commit/31e827f58b9916702e0dec010bdbfb9cb292ac5a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/selfer08/life-game

[Back to the awesome list](../../README.md)
