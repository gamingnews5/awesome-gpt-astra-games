# Chess Realms

> Verified game note.

![Chess Realms screenshot](https://raw.githubusercontent.com/kalpeshmahajan21/chess-realms/main/docs/realistic_arenas.jpg)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 6.4/10 ([manually reviewed image](https://github.com/kalpeshmahajan21/chess-realms/blob/main/docs/realistic_arenas.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/kalpeshmahajan21/chess-realms](https://github.com/kalpeshmahajan21/chess-realms)
- **Evidence:** [direct model evidence](https://github.com/kalpeshmahajan21/chess-realms/commit/4bc75ce83a7bc8a5f28850b10791db33b989bf17)
- **Live demo:** [open demo](https://chess-realms.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/kalpeshmahajan21/chess-realms/blob/main/docs/realistic_arenas.jpg) — 📸 6.4/10 · manual visual review · Use this frame for the game-level score. 3D chessboards in several arenas; polished renders.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Cinematic 3D chess in the browser: eight 3D arenas, capture cinematics, five AI levels, local and online play. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kalpeshmahajan21/chess-realms/blob/main/src/graphics/arenas/arenaManager.ts](https://github.com/kalpeshmahajan21/chess-realms/blob/main/src/graphics/arenas/arenaManager.ts)
- [https://github.com/kalpeshmahajan21/chess-realms/commit/4bc75ce83a7bc8a5f28850b10791db33b989bf17](https://github.com/kalpeshmahajan21/chess-realms/commit/4bc75ce83a7bc8a5f28850b10791db33b989bf17)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/kalpeshmahajan21/chess-realms

[Back to the awesome list](../../README.md)
