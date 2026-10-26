# amade-hover-cab-game

> Verified game note.

![amade-hover-cab-game screenshot](https://raw.githubusercontent.com/datazuul/amade-hover-cab-game/develop/docs/screenshots/amade-hover-cab-game.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 6.3/10 ([manually reviewed image](https://github.com/datazuul/amade-hover-cab-game/blob/develop/docs/screenshots/amade-hover-cab-game.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Java
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/datazuul/amade-hover-cab-game](https://github.com/datazuul/amade-hover-cab-game)
- **Evidence:** [direct model evidence](https://github.com/datazuul/amade-hover-cab-game/commit/27159097c56b53fa5619b05b223789f4c3ae7b25)
- **Live demo:** [open demo](https://datazuul.github.io/amade-game-engine/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/datazuul/amade-hover-cab-game/blob/develop/docs/screenshots/amade-hover-cab-game.png) — 📸 6.3/10 · manual visual review · Use this frame for the game-level score. Night city stage with neon buildings, a hover cab and HUD bar; tidy pixel layout.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The keys can be changed in ~/.config/amadeos/hovercab/hovercab.properties, with the names Java gives them, several separated by spaces. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/datazuul/amade-hover-cab-game/blob/develop/src/main/java/eu/amadeos/games/hovercab/ui/game/Scenery.java](https://github.com/datazuul/amade-hover-cab-game/blob/develop/src/main/java/eu/amadeos/games/hovercab/ui/game/Scenery.java)
- [https://github.com/datazuul/amade-hover-cab-game/commit/27159097c56b53fa5619b05b223789f4c3ae7b25](https://github.com/datazuul/amade-hover-cab-game/commit/27159097c56b53fa5619b05b223789f4c3ae7b25)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/datazuul/amade-hover-cab-game

[Back to the awesome list](../../README.md)
