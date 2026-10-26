# Group Project

> Verified game note.

![Group Project screenshot](https://raw.githubusercontent.com/b14ck5tar/H4CKBOMB/main/devpost-media/art-audit/after/idea-slam_1366x768.jpg)

## At a glance

- **Score:** 8.0/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/b14ck5tar/H4CKBOMB/blob/main/devpost-media/art-audit/after/idea-slam_1366x768.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/b14ck5tar/H4CKBOMB](https://github.com/b14ck5tar/H4CKBOMB)
- **Evidence:** [direct model evidence](https://github.com/b14ck5tar/H4CKBOMB/commit/d01c7b13301cc5e29738f6c0a6f9ae7f0b5027db)
- **Live demo:** [open demo](https://groupproject-game.vercel.app/tv)
- **Additional live link:** [open demo](https://groupproject-game.vercel.app/play)
- **Additional live link:** [open demo](https://groupproject-game.vercel.app/tv?judge=1)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/b14ck5tar/H4CKBOMB/blob/main/devpost-media/art-audit/after/idea-slam_1366x768.jpg) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Neon round screen with idea cards over a graffiti backdrop; vivid party-game UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A co-op party game for friends in one room. A laptop or TV is the table, phones are the controllers, and Meta's Muse. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/b14ck5tar/H4CKBOMB/blob/main/game/src/lib/host.ts](https://github.com/b14ck5tar/H4CKBOMB/blob/main/game/src/lib/host.ts)
- [https://github.com/b14ck5tar/H4CKBOMB/commit/d01c7b13301cc5e29738f6c0a6f9ae7f0b5027db](https://github.com/b14ck5tar/H4CKBOMB/commit/d01c7b13301cc5e29738f6c0a6f9ae7f0b5027db)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/b14ck5tar/H4CKBOMB

[Back to the awesome list](../../README.md)
