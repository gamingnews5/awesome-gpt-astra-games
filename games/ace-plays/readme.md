# Ace Plays!

> Verified game note.

![Ace Plays! screenshot](https://raw.githubusercontent.com/d3bug21/ace-plays/main/docs/screenshots/title.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/d3bug21/ace-plays/blob/main/docs/screenshots/title.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/d3bug21/ace-plays](https://github.com/d3bug21/ace-plays)
- **Evidence:** [direct model evidence](https://github.com/d3bug21/ace-plays/commit/287327b2e02824561e8c349d575968d5fb107cf3)
- **Live demo:** [open demo](https://ace-plays.ace-plays.workers.dev)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/d3bug21/ace-plays/blob/main/docs/screenshots/title.png) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Soft 3D title with a kid by a tree and Play button; charming.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Ace Plays! — a gentle, kid-friendly first-person bubble & ball adventure for Windows, macOS and Linux (Electron + Three.js). Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/d3bug21/ace-plays/blob/main/src/stages/dino/creatures.ts](https://github.com/d3bug21/ace-plays/blob/main/src/stages/dino/creatures.ts)
- [https://github.com/d3bug21/ace-plays/commit/287327b2e02824561e8c349d575968d5fb107cf3](https://github.com/d3bug21/ace-plays/commit/287327b2e02824561e8c349d575968d5fb107cf3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/d3bug21/ace-plays

[Back to the awesome list](../../README.md)
