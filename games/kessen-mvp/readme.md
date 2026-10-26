# 決戰（Kessen）— MVP

> Verified game note.

![決戰（Kessen）— MVP screenshot placeholder](kessen-mvp-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Fable 5.1
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/kuanhuasu-source/kessen](https://github.com/kuanhuasu-source/kessen)
- **Evidence:** [direct model evidence](https://github.com/kuanhuasu-source/kessen/commit/c9e1172db2005b968e268b03961a577f769c4506)
- **Live demo:** [open demo](https://kuanhuasu-source.github.io/kessen/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

網頁即時戰略遊戲。技術：TypeScript + Vite + Three.js。戰鬥核心（src/sim）沿用士氣模擬器，規則為設計文件 v2 士氣調整＋ v3 忍者調整（src/sim/game-rules.ts）。. Commit carries an exact Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kuanhuasu-source/kessen/blob/main/src/game/main.ts](https://github.com/kuanhuasu-source/kessen/blob/main/src/game/main.ts)
- [https://github.com/kuanhuasu-source/kessen/commit/c9e1172db2005b968e268b03961a577f769c4506](https://github.com/kuanhuasu-source/kessen/commit/c9e1172db2005b968e268b03961a577f769c4506)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/kuanhuasu-source/kessen

[Back to the awesome list](../../README.md)
