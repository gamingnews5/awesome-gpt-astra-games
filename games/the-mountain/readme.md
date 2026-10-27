# The Mountain

> Verified game note.

![The Mountain screenshot placeholder](the-mountain-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/diquinnyonk/the-mountain](https://github.com/diquinnyonk/the-mountain)
- **Evidence:** [direct model evidence](https://github.com/diquinnyonk/the-mountain/commit/a255931f9eeee5103f5aae319cd43a167c9e5408)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Climb Mount Everest by the South Col route, from Base Camp (5,364 m) to the summit (8,849 m), in three.js. The terrain is real elevation data and the weather is the real weather of the day you choose. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/diquinnyonk/the-mountain/blob/claude/everest-game/src/expedition.ts](https://github.com/diquinnyonk/the-mountain/blob/claude/everest-game/src/expedition.ts)
- [https://github.com/diquinnyonk/the-mountain/commit/a255931f9eeee5103f5aae319cd43a167c9e5408](https://github.com/diquinnyonk/the-mountain/commit/a255931f9eeee5103f5aae319cd43a167c9e5408)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/diquinnyonk/the-mountain

[Back to the awesome list](../../README.md)
