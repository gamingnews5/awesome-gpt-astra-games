# Cyber City Tactics

> Verified game note.

![Cyber City Tactics screenshot](https://raw.githubusercontent.com/CptNope/Cyber-City-Tactics/main/docs/design/panels/shots/fight.png)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/CptNope/Cyber-City-Tactics/blob/main/docs/design/panels/shots/fight.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/CptNope/Cyber-City-Tactics](https://github.com/CptNope/Cyber-City-Tactics)
- **Evidence:** [direct model evidence](https://github.com/CptNope/Cyber-City-Tactics/commit/e2010223c7f31ff3a2377afe2e3de5b3cc8c3800)
- **Live demo:** [open demo](https://cptnope.github.io/Cyber-City-Tactics/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/CptNope/Cyber-City-Tactics/blob/main/docs/design/panels/shots/fight.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Neon cyberpunk street brawl with two-player HUD; lively.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

It's plain JavaScript with no framework and no runtime dependencies, split into small files by system. It runs in any modern browser and installs as an app (PWA) that plays fully offline. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/CptNope/Cyber-City-Tactics/blob/main/src/js/render/figures.js](https://github.com/CptNope/Cyber-City-Tactics/blob/main/src/js/render/figures.js)
- [https://github.com/CptNope/Cyber-City-Tactics/commit/e2010223c7f31ff3a2377afe2e3de5b3cc8c3800](https://github.com/CptNope/Cyber-City-Tactics/commit/e2010223c7f31ff3a2377afe2e3de5b3cc8c3800)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/CptNope/Cyber-City-Tactics

[Back to the awesome list](../../README.md)
