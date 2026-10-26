# Wonder Royale: online

> Verified game note.

![Wonder Royale: online screenshot](https://raw.githubusercontent.com/wlin84602-pixel/wonder-royale/main/server/test/shot-match.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/wlin84602-pixel/wonder-royale/blob/main/server/test/shot-match.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/wlin84602-pixel/wonder-royale](https://github.com/wlin84602-pixel/wonder-royale)
- **Evidence:** [direct model evidence](https://github.com/wlin84602-pixel/wonder-royale/commit/28dc83e71a9845e143ccdb8d032736fd86c55be7)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/wlin84602-pixel/wonder-royale/blob/main/server/test/shot-match.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Top-down battle royale map with buildings, trees and HUD panels; busy but legible.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Top-down battle royale for 2–6 players per room. Node + Express + Socket.IO server runs the real game rules;. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/wlin84602-pixel/wonder-royale/blob/main/client/game.js](https://github.com/wlin84602-pixel/wonder-royale/blob/main/client/game.js)
- [https://github.com/wlin84602-pixel/wonder-royale/commit/28dc83e71a9845e143ccdb8d032736fd86c55be7](https://github.com/wlin84602-pixel/wonder-royale/commit/28dc83e71a9845e143ccdb8d032736fd86c55be7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/wlin84602-pixel/wonder-royale

[Back to the awesome list](../../README.md)
