# VibeWars

> Top-list entry: **today** (#7).

![VibeWars screenshot](https://raw.githubusercontent.com/Enteee/VibeWars/main/docs/media/readme-arena.png)

## At a glance

- **Score:** 8.2/10
- **Screenshot rating:** 4.2/10 ([manually reviewed image](https://github.com/Enteee/VibeWars/blob/main/docs/media/readme-arena.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Enteee/VibeWars](https://github.com/Enteee/VibeWars)
- **Evidence:** [direct model evidence](https://github.com/Enteee/VibeWars/commit/9699f3a29a24bb40d9fd62ae9f7b239198bac01d)
- **Live demo:** [open demo](https://enteee.github.io/VibeWars/next/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Enteee/VibeWars/blob/main/docs/media/readme-arena.png) — 📸 4.2/10 · manual visual review · Use this frame for the game-level score. Dark debug-style character builder panels; readable but mostly UI text.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Minimalist browser PvP arena game for LAN parties, inspired by Guild Wars 1 PvP. Original code and geometric art; one host runs the server, friends join with a lobby code. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Enteee/VibeWars/blob/main/scripts/bots/hubd.mjs](https://github.com/Enteee/VibeWars/blob/main/scripts/bots/hubd.mjs)
- [https://github.com/Enteee/VibeWars/commit/9699f3a29a24bb40d9fd62ae9f7b239198bac01d](https://github.com/Enteee/VibeWars/commit/9699f3a29a24bb40d9fd62ae9f7b239198bac01d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Enteee/VibeWars

[Back to the awesome list](../../README.md)
