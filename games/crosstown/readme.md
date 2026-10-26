# Crosstown

> Verified game note.

![Crosstown screenshot](https://raw.githubusercontent.com/jmzidek9/GTA-taxi-game/main/media/screenshot-night.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/jmzidek9/GTA-taxi-game/blob/main/media/screenshot-night.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/jmzidek9/GTA-taxi-game](https://github.com/jmzidek9/GTA-taxi-game)
- **Evidence:** [direct model evidence](https://github.com/jmzidek9/GTA-taxi-game/commit/ade96f186169e098c0b809a7ce40a5c14345fb01)
- **Live demo:** [open demo](https://jmzidek9.github.io/GTA-taxi-game/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jmzidek9/GTA-taxi-game/blob/main/media/screenshot-night.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Night 3D city street driving a taxi with minimap and speedometer HUD; polished.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D taxi game set in a city that never sees daylight. Take a fare from dispatch, stop by your passenger, watch them climb in, then beat the meter to their destination — without picking up a wanted level on the way. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jmzidek9/GTA-taxi-game/blob/main/js/world.js](https://github.com/jmzidek9/GTA-taxi-game/blob/main/js/world.js)
- [https://github.com/jmzidek9/GTA-taxi-game/commit/ade96f186169e098c0b809a7ce40a5c14345fb01](https://github.com/jmzidek9/GTA-taxi-game/commit/ade96f186169e098c0b809a7ce40a5c14345fb01)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/jmzidek9/GTA-taxi-game

[Back to the awesome list](../../README.md)
