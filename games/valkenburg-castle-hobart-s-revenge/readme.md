# Valkenburg Castle: Hobart's Revenge

> Verified game note.

![Valkenburg Castle: Hobart's Revenge screenshot](https://raw.githubusercontent.com/morgan-vanv/Valkenburg-Castle/main/docs/agents/v32-los-bug.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/morgan-vanv/Valkenburg-Castle/blob/main/docs/agents/v32-los-bug.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/morgan-vanv/Valkenburg-Castle](https://github.com/morgan-vanv/Valkenburg-Castle)
- **Evidence:** [direct model evidence](https://github.com/morgan-vanv/Valkenburg-Castle/commit/b167ccec763cee4f12307a8ced39e71476b8723e)
- **Live demo:** [open demo](https://morgan-vanv.github.io/Valkenburg-Castle/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/morgan-vanv/Valkenburg-Castle/blob/main/docs/agents/v32-los-bug.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Hex-tile dungeon map with fog, tokens and a side panel; moody and readable.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

a browser game that is inspired primarily by an old tabletop game from the 1980s called "Valkenburg's Castle". Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/morgan-vanv/Valkenburg-Castle/blob/main/src/view/diorama.ts](https://github.com/morgan-vanv/Valkenburg-Castle/blob/main/src/view/diorama.ts)
- [https://github.com/morgan-vanv/Valkenburg-Castle/commit/b167ccec763cee4f12307a8ced39e71476b8723e](https://github.com/morgan-vanv/Valkenburg-Castle/commit/b167ccec763cee4f12307a8ced39e71476b8723e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/morgan-vanv/Valkenburg-Castle

[Back to the awesome list](../../README.md)
