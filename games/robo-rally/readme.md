# Robo Rally

> Verified game note.

![Robo Rally screenshot](https://raw.githubusercontent.com/IanHovander/RoboRally/main/looks/one/games/robo-rally/img/bot-0.webp)

## At a glance

- **Score:** 8.1/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/IanHovander/RoboRally/blob/main/looks/one/games/robo-rally/img/bot-0.webp)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/IanHovander/RoboRally](https://github.com/IanHovander/RoboRally)
- **Evidence:** [direct model evidence](https://github.com/IanHovander/RoboRally/commit/580a07b6cc79473a066fe09c324d45556473baa7)
- **Live demo:** [open demo](https://ianhovander.github.io/RoboRally/host.html)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/IanHovander/RoboRally/blob/main/looks/one/games/robo-rally/img/bot-0.webp) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Clean 3D render of a toy tank robot; single asset.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Built on Game Night; this edition offers only Robo Rally. Nobody installs an app. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/IanHovander/RoboRally/blob/main/looks/one/games/robo-rally/scene.js](https://github.com/IanHovander/RoboRally/blob/main/looks/one/games/robo-rally/scene.js)
- [https://github.com/IanHovander/RoboRally/commit/580a07b6cc79473a066fe09c324d45556473baa7](https://github.com/IanHovander/RoboRally/commit/580a07b6cc79473a066fe09c324d45556473baa7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/IanHovander/RoboRally

[Back to the awesome list](../../README.md)
