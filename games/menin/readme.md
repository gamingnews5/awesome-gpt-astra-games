# MeNIN

> Verified game note.

![MeNIN screenshot](https://raw.githubusercontent.com/Matusvec/MeNIN/main/docs/figma/hall-arrow-promax.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 4.2/10 ([manually reviewed image](https://github.com/Matusvec/MeNIN/blob/main/docs/figma/hall-arrow-promax.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** Swift, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Matusvec/MeNIN](https://github.com/Matusvec/MeNIN)
- **Evidence:** [direct model evidence](https://github.com/Matusvec/MeNIN/commit/71c1e6d3853719fbed67d280a7f11996206bf4d9)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Matusvec/MeNIN/blob/main/docs/figma/hall-arrow-promax.png) — 📸 4.2/10 · manual visual review · Use this frame for the game-level score. Pale phone screen with a hold-to-nock prompt; minimal.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

MeNIN (Cal Hacks 13.0): Homer teaches you to speak, then you battle. Mirror of the team repo sunya-afrasiabi/MeNIN for judging. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Matusvec/MeNIN/blob/main/homer/scripts/rough_cut.py](https://github.com/Matusvec/MeNIN/blob/main/homer/scripts/rough_cut.py)
- [https://github.com/Matusvec/MeNIN/commit/71c1e6d3853719fbed67d280a7f11996206bf4d9](https://github.com/Matusvec/MeNIN/commit/71c1e6d3853719fbed67d280a7f11996206bf4d9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Matusvec/MeNIN

[Back to the awesome list](../../README.md)
