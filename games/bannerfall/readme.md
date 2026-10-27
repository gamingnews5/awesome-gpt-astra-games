# Bannerfall

> Verified game note.

![Bannerfall screenshot](https://raw.githubusercontent.com/alakrim/NewGa/claude/2.5d-hero-tower-defense-odusfc/docs/screenshots/gameplay.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.6/10 ([manually reviewed image](https://github.com/alakrim/NewGa/blob/claude/2.5d-hero-tower-defense-odusfc/docs/screenshots/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/alakrim/NewGa](https://github.com/alakrim/NewGa)
- **Evidence:** [direct model evidence](https://github.com/alakrim/NewGa/commit/218d83b3fed8d06f88228771e5990c5db6ad6986)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/alakrim/NewGa/blob/claude/2.5d-hero-tower-defense-odusfc/docs/screenshots/gameplay.png) — 📸 6.6/10 · manual visual review · Use this frame for the game-level score. Top-down battle on a dirt path with trees, units and skill bar; lively.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Runs in the browser. One small Node server hosts rooms for you and your friends. Empty seats are filled by bots, and there is an offline practice mode. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/alakrim/NewGa/blob/claude/2.5d-hero-tower-defense-odusfc/src/shared/sim/game.ts](https://github.com/alakrim/NewGa/blob/claude/2.5d-hero-tower-defense-odusfc/src/shared/sim/game.ts)
- [https://github.com/alakrim/NewGa/commit/218d83b3fed8d06f88228771e5990c5db6ad6986](https://github.com/alakrim/NewGa/commit/218d83b3fed8d06f88228771e5990c5db6ad6986)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/alakrim/NewGa

[Back to the awesome list](../../README.md)
