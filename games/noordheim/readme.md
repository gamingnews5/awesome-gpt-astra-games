# Noordheim

> Verified game note.

![Noordheim screenshot](https://raw.githubusercontent.com/thijssmudde/noordheim-oss/main/art/concepts/noordheim-gameplay.png)

## At a glance

- **Score:** 8.1/10
- **Screenshot rating:** 7.0/10 ([manually reviewed image](https://github.com/thijssmudde/noordheim-oss/blob/main/art/concepts/noordheim-gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/thijssmudde/noordheim-oss](https://github.com/thijssmudde/noordheim-oss)
- **Evidence:** [direct model evidence](https://github.com/thijssmudde/noordheim-oss/commit/06886ce1955934f1ae066852c0e2557ac2e3fc42)
- **Live demo:** [open demo](https://noordheim.com)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/thijssmudde/noordheim-oss/blob/main/art/concepts/noordheim-gameplay.png) — 📸 7.0/10 · manual visual review · Use this frame for the game-level score. Detailed isometric Nordic village with timber halls and bridge; rich environment.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Cooperative real-time strategy game in the browser: Three.js, React and a Convex server that simulates the battle 4x a second. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/thijssmudde/noordheim-oss/blob/main/lib/tactics.ts](https://github.com/thijssmudde/noordheim-oss/blob/main/lib/tactics.ts)
- [https://github.com/thijssmudde/noordheim-oss/commit/06886ce1955934f1ae066852c0e2557ac2e3fc42](https://github.com/thijssmudde/noordheim-oss/commit/06886ce1955934f1ae066852c0e2557ac2e3fc42)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/thijssmudde/noordheim-oss

[Back to the awesome list](../../README.md)
