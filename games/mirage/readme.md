# Mirage

> Verified game note.

![Mirage screenshot](https://raw.githubusercontent.com/nulljosh/mirage/main/docs/shots/canyon.png)

## At a glance

- **Score:** 6.9/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/nulljosh/mirage/blob/main/docs/shots/canyon.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Swift, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/nulljosh/mirage](https://github.com/nulljosh/mirage)
- **Evidence:** [direct model evidence](https://github.com/nulljosh/mirage/commit/da9b8d945c62277255aab601fccd89615f1f04dc)
- **Live demo:** [open demo](https://mirage.jaybulb.com)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/nulljosh/mirage/blob/main/docs/shots/canyon.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Pixel desert town with cactus and adobe houses; coherent warm palette.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A small desert platformer that runs inside Joshua Tree, a computer built from scratch. Play it on the page. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nulljosh/mirage/blob/main/landing/index.html](https://github.com/nulljosh/mirage/blob/main/landing/index.html)
- [https://github.com/nulljosh/mirage/commit/da9b8d945c62277255aab601fccd89615f1f04dc](https://github.com/nulljosh/mirage/commit/da9b8d945c62277255aab601fccd89615f1f04dc)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/nulljosh/mirage

[Back to the awesome list](../../README.md)
