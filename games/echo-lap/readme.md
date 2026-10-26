# Echo Lap

> Verified game note.

![Echo Lap screenshot](https://raw.githubusercontent.com/ramcc007/racing-app/main/ci-screens/ipad-pro-13_home.jpg)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/ramcc007/racing-app/blob/main/ci-screens/ipad-pro-13_home.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Swift, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/ramcc007/racing-app](https://github.com/ramcc007/racing-app)
- **Evidence:** [direct model evidence](https://github.com/ramcc007/racing-app/commit/87b92692b7a31b7b2b14a856400d6b3d2007c966)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ramcc007/racing-app/blob/main/ci-screens/ipad-pro-13_home.jpg) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Dark iPhone garage and track menu; tidy but small UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A one-thumb top-down drift racer for iPhone and iPad. The car drives itself; you drag to steer, hold a turn hard to. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ramcc007/racing-app/blob/main/ios/EchoLapCore/Sources/EchoLapCore/Race.swift](https://github.com/ramcc007/racing-app/blob/main/ios/EchoLapCore/Sources/EchoLapCore/Race.swift)
- [https://github.com/ramcc007/racing-app/commit/87b92692b7a31b7b2b14a856400d6b3d2007c966](https://github.com/ramcc007/racing-app/commit/87b92692b7a31b7b2b14a856400d6b3d2007c966)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/ramcc007/racing-app

[Back to the awesome list](../../README.md)
