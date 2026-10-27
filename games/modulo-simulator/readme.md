# Modulo Simulator

> Verified game note.

![Modulo Simulator screenshot placeholder](modulo-simulator-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/leiffurthersocial-rgb/modulo-simulator](https://github.com/leiffurthersocial-rgb/modulo-simulator)
- **Evidence:** [direct model evidence](https://github.com/leiffurthersocial-rgb/modulo-simulator/commit/d36efda0f60d3bf46c8987a7cd50678fe108215a)
- **Live demo:** [open demo](https://modulo-simulator.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A text-based life simulator in the spirit of BitLife: be born, grow up, go to school, fall in love, build a career (or a criminal empire), and see how it all ends. It runs entirely in the browser. There's no backend, saves live in localStorage, and the game… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/leiffurthersocial-rgb/modulo-simulator/blob/main/data/events/school.ts](https://github.com/leiffurthersocial-rgb/modulo-simulator/blob/main/data/events/school.ts)
- [https://github.com/leiffurthersocial-rgb/modulo-simulator/commit/d36efda0f60d3bf46c8987a7cd50678fe108215a](https://github.com/leiffurthersocial-rgb/modulo-simulator/commit/d36efda0f60d3bf46c8987a7cd50678fe108215a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/leiffurthersocial-rgb/modulo-simulator

[Back to the awesome list](../../README.md)
