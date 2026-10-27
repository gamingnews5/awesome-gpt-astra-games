# CHarth

> Verified game note.

![CHarth screenshot](https://raw.githubusercontent.com/jadflat/CHarth/main/docs/gameplay.gif)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/jadflat/CHarth/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/jadflat/CHarth](https://github.com/jadflat/CHarth)
- **Evidence:** [direct model evidence](https://github.com/jadflat/CHarth/commit/7900ca23c5a5b2f73511726b32e17003d6135f7a)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jadflat/CHarth/blob/main/docs/gameplay.gif) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Green-on-black terminal title with pixel CHARTH logo.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

CHarth: an original block-shooting puzzle game for CHGame. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jadflat/CHarth/blob/main/chgame/platform/board/arduino/CHGame/libraries/CHGfx/src/CHGfx.h](https://github.com/jadflat/CHarth/blob/main/chgame/platform/board/arduino/CHGame/libraries/CHGfx/src/CHGfx.h)
- [https://github.com/jadflat/CHarth/commit/7900ca23c5a5b2f73511726b32e17003d6135f7a](https://github.com/jadflat/CHarth/commit/7900ca23c5a5b2f73511726b32e17003d6135f7a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/jadflat/CHarth

[Back to the awesome list](../../README.md)
