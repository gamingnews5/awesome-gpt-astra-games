# Pika Jump

> Verified game note.

![Pika Jump screenshot](https://raw.githubusercontent.com/matthewjack/pika-jump/main/docs/images/2-win-screen.png)

## At a glance

- **Score:** 6.9/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/matthewjack/pika-jump/blob/main/docs/images/2-win-screen.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/matthewjack/pika-jump](https://github.com/matthewjack/pika-jump)
- **Evidence:** [direct model evidence](https://github.com/matthewjack/pika-jump/commit/c853e8fe38380fc6335f8c1a8dcefb03a45c907b)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/matthewjack/pika-jump/blob/main/docs/images/2-win-screen.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Mario-style level with brick staircase, flag and Pikachu; clear retro look with HUD.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A Mario-style platformer with Pokémon battles, catching and evolution — built by vibe coding with a 10-year-old. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/matthewjack/pika-jump/blob/main/src/scenes/BattleScene.ts](https://github.com/matthewjack/pika-jump/blob/main/src/scenes/BattleScene.ts)
- [https://github.com/matthewjack/pika-jump/commit/c853e8fe38380fc6335f8c1a8dcefb03a45c907b](https://github.com/matthewjack/pika-jump/commit/c853e8fe38380fc6335f8c1a8dcefb03a45c907b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/matthewjack/pika-jump

[Back to the awesome list](../../README.md)
