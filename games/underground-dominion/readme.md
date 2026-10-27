# Underground Dominion

> Top-list entry: **today** (#5).

![Underground Dominion screenshot](https://raw.githubusercontent.com/ChibisC/WIP/main/docs/multiplayer/teams-lobby-host.png)

## At a glance

- **Score:** 8.2/10
- **Screenshot rating:** 4.4/10 ([manually reviewed image](https://github.com/ChibisC/WIP/blob/main/docs/multiplayer/teams-lobby-host.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/ChibisC/WIP](https://github.com/ChibisC/WIP)
- **Evidence:** [direct model evidence](https://github.com/ChibisC/WIP/commit/01a998199bac1d4f36ecb1b638b29ce10db812a9)
- **Live demo:** [open demo](https://chibisc.github.io/WIP/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ChibisC/WIP/blob/main/docs/multiplayer/teams-lobby-host.png) — 📸 4.4/10 · manual visual review · Use this frame for the game-level score. Dark multiplayer lobby list with small map thumbnails; mostly UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D ant-colony real-time strategy game in the spirit of Empires of the Undergrowth, built with TypeScript, Three.js and Vite. Everything is procedural: terrain, nests, ants, creatures, sounds and UI art. Species and behaviour follow real ant biology; the… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ChibisC/WIP/blob/main/src/game/session.ts](https://github.com/ChibisC/WIP/blob/main/src/game/session.ts)
- [https://github.com/ChibisC/WIP/commit/01a998199bac1d4f36ecb1b638b29ce10db812a9](https://github.com/ChibisC/WIP/commit/01a998199bac1d4f36ecb1b638b29ce10db812a9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/ChibisC/WIP

[Back to the awesome list](../../README.md)
