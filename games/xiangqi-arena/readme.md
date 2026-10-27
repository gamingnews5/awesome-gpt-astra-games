# Xiangqi Arena 象棋競技場

> Verified game note.

![Xiangqi Arena 象棋競技場 screenshot placeholder](xiangqi-arena-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/YisoTsao/xiangqi-arena](https://github.com/YisoTsao/xiangqi-arena)
- **Evidence:** [direct model evidence](https://github.com/YisoTsao/xiangqi-arena/commit/c954f9c643adfb0cdbafed84093bb238d5126ed4)
- **Live demo:** [open demo](https://web-rose-sigma-54.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

精緻的 2.5D 線上雙人象棋競技場，支援傳統大盤象棋與台灣暗棋，. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/YisoTsao/xiangqi-arena/blob/main/apps/game-server/src/room/RoomController.ts](https://github.com/YisoTsao/xiangqi-arena/blob/main/apps/game-server/src/room/RoomController.ts)
- [https://github.com/YisoTsao/xiangqi-arena/commit/c954f9c643adfb0cdbafed84093bb238d5126ed4](https://github.com/YisoTsao/xiangqi-arena/commit/c954f9c643adfb0cdbafed84093bb238d5126ed4)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/YisoTsao/xiangqi-arena

[Back to the awesome list](../../README.md)
