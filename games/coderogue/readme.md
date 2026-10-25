# CodeRogue

> Verified game note.

![CodeRogue screenshot](https://raw.githubusercontent.com/gabrielconlon/coderogue/main/docs/screenshots/wakeup.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/gabrielconlon/coderogue/blob/main/docs/screenshots/wakeup.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Fable 5.1
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/gabrielconlon/coderogue](https://github.com/gabrielconlon/coderogue)
- **Evidence:** [direct model evidence](https://github.com/gabrielconlon/coderogue/commit/4799221abf6b8d40f7c6acfb150a9364b2938d50)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/gabrielconlon/coderogue/blob/main/docs/screenshots/wakeup.png) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. Top-down pixel dungeon room with dialogue box and HUD; cohesive retro RPG look.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

It has never been easier to get code written for you, and never easier to lose the ability to write it yourself. CodeRogue is for people who want the basics in their hands: what a variable is, how a loop ends, why a file has a newline at the end, what git… Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/gabrielconlon/coderogue/blob/main/coderogue/world/scene.py](https://github.com/gabrielconlon/coderogue/blob/main/coderogue/world/scene.py)
- [https://github.com/gabrielconlon/coderogue/commit/4799221abf6b8d40f7c6acfb150a9364b2938d50](https://github.com/gabrielconlon/coderogue/commit/4799221abf6b8d40f7c6acfb150a9364b2938d50)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/gabrielconlon/coderogue

[Back to the awesome list](../../README.md)
