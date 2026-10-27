# HarvestChain

> Verified game note.

![HarvestChain screenshot](https://raw.githubusercontent.com/vithushanms/HarvestChain/main/docs/screenshots/farm.png)

## At a glance

- **Score:** 7.0/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/vithushanms/HarvestChain/blob/main/docs/screenshots/farm.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** WebAssembly, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/vithushanms/HarvestChain](https://github.com/vithushanms/HarvestChain)
- **Evidence:** [direct model evidence](https://github.com/vithushanms/HarvestChain/commit/aee2e451d2d3f73d008ee73b423c0379cedce6d8)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/vithushanms/HarvestChain/blob/main/docs/screenshots/farm.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Pixel farm plot under a blue sky with a toolbar; tidy and charming but small.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A strategy game that built using direct web assembly via AI agent skipping all the abstraction needed for human programmers. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/vithushanms/HarvestChain/blob/main/tools/gen-strings.mjs](https://github.com/vithushanms/HarvestChain/blob/main/tools/gen-strings.mjs)
- [https://github.com/vithushanms/HarvestChain/commit/aee2e451d2d3f73d008ee73b423c0379cedce6d8](https://github.com/vithushanms/HarvestChain/commit/aee2e451d2d3f73d008ee73b423c0379cedce6d8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/vithushanms/HarvestChain

[Back to the awesome list](../../README.md)
