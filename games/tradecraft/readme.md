# TRADECRAFT

> Verified game note.

![TRADECRAFT screenshot](https://raw.githubusercontent.com/mramad3us/tradecraft/main/samples/000-toolchain/shots/close.jpg)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 4.8/10 ([manually reviewed image](https://github.com/mramad3us/tradecraft/blob/main/samples/000-toolchain/shots/close.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/mramad3us/tradecraft](https://github.com/mramad3us/tradecraft)
- **Evidence:** [direct model evidence](https://github.com/mramad3us/tradecraft/commit/2d46cb8ca4333a7a2d760672847ab93cbeaeaaf3)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/mramad3us/tradecraft/blob/main/samples/000-toolchain/shots/close.jpg) — 📸 4.8/10 · manual visual review · Use this frame for the game-level score. Close-up 3D suited agent on a plain grey background; early prototype look.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A spy game in the browser: a CIA officer in Moscow, pixel art, tradecraft over reflexes. The design is settled in docs/DESIGN.md; the game is being built toward its first playable (0.1.0), a mechanic at a time. Today it opens on the free walk (generated… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mramad3us/tradecraft/blob/main/src/sim/scenarios/tail.js](https://github.com/mramad3us/tradecraft/blob/main/src/sim/scenarios/tail.js)
- [https://github.com/mramad3us/tradecraft/commit/2d46cb8ca4333a7a2d760672847ab93cbeaeaaf3](https://github.com/mramad3us/tradecraft/commit/2d46cb8ca4333a7a2d760672847ab93cbeaeaaf3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/mramad3us/tradecraft

[Back to the awesome list](../../README.md)
