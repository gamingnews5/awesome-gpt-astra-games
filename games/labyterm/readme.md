# LabyTerm

> Verified game note.

![LabyTerm screenshot](https://raw.githubusercontent.com/SCharchian/LabyTerm/main/docs/images/desktop-robco.jpg)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/SCharchian/LabyTerm/blob/main/docs/images/desktop-robco.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/SCharchian/LabyTerm](https://github.com/SCharchian/LabyTerm)
- **Evidence:** [direct model evidence](https://github.com/SCharchian/LabyTerm/commit/5beb2eedfd82c028922d766db9d10503f722f994)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/SCharchian/LabyTerm/blob/main/docs/images/desktop-robco.jpg) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Text-mode dungeon crawler in terminal panes with ASCII first-person view; niche but cohesive.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A first-person dungeon crawler for Omarchy with a text-mode look: every cell is a colored character, in its own window. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/SCharchian/LabyTerm/blob/main/third_party/stb/stb_image.h](https://github.com/SCharchian/LabyTerm/blob/main/third_party/stb/stb_image.h)
- [https://github.com/SCharchian/LabyTerm/commit/5beb2eedfd82c028922d766db9d10503f722f994](https://github.com/SCharchian/LabyTerm/commit/5beb2eedfd82c028922d766db9d10503f722f994)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/SCharchian/LabyTerm

[Back to the awesome list](../../README.md)
