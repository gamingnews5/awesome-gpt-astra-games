# Sverigespelet

> Top-list entry: **today** (#10).

![Sverigespelet screenshot](https://raw.githubusercontent.com/hamiltoon/sweden-county-quiz/main/docs/screenshot.png)

## At a glance

- **Score:** 7.9/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/hamiltoon/sweden-county-quiz/blob/main/docs/screenshot.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/hamiltoon/sweden-county-quiz](https://github.com/hamiltoon/sweden-county-quiz)
- **Evidence:** [direct model evidence](https://github.com/hamiltoon/sweden-county-quiz/commit/6f798f365f1c60887580e87fd7ecc9f2abfa50e9)
- **Live demo:** [open demo](https://sverigespelet.hamiltoon.workers.dev)
- **Additional live link:** [open demo](https://sverigespelet-staging.hamiltoon.workers.dev)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/hamiltoon/sweden-county-quiz/blob/main/docs/screenshot.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Sweden county map quiz with highlighted regions; clear educational UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Ett geografispel i webbläsaren om Sveriges 21 län, 25 landskap, 290 kommuner, residensstäder, 75 andra städer och tio största sjöar. Klicka rätt på kartan, samla poäng och ta dig in på topplistan – fungerar lika bra på mobilen som på datorn. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hamiltoon/sweden-county-quiz/blob/main/worker/worker-configuration.d.ts](https://github.com/hamiltoon/sweden-county-quiz/blob/main/worker/worker-configuration.d.ts)
- [https://github.com/hamiltoon/sweden-county-quiz/commit/6f798f365f1c60887580e87fd7ecc9f2abfa50e9](https://github.com/hamiltoon/sweden-county-quiz/commit/6f798f365f1c60887580e87fd7ecc9f2abfa50e9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/hamiltoon/sweden-county-quiz

[Back to the awesome list](../../README.md)
