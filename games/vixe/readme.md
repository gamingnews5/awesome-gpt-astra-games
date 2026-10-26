# VIXE

> Verified game note.

![VIXE screenshot](https://raw.githubusercontent.com/thdtr/vixe/main/docs/trailer.gif)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/thdtr/vixe/blob/main/docs/trailer.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/thdtr/vixe](https://github.com/thdtr/vixe)
- **Evidence:** [direct model evidence](https://github.com/thdtr/vixe/commit/385fdb18d30fed0c025f5bad559197d5911c0679)
- **Live demo:** [open demo](https://vixe.online)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/thdtr/vixe/blob/main/docs/trailer.gif) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. ASCII platformer with @ hero over a hash floor; deliberately minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An ASCII platformer that doesn't play fair. ~240 KB, no images, no libraries. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/thdtr/vixe/blob/main/assets/js/scenes/play.js](https://github.com/thdtr/vixe/blob/main/assets/js/scenes/play.js)
- [https://github.com/thdtr/vixe/commit/385fdb18d30fed0c025f5bad559197d5911c0679](https://github.com/thdtr/vixe/commit/385fdb18d30fed0c025f5bad559197d5911c0679)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/thdtr/vixe

[Back to the awesome list](../../README.md)
