# air-hockey

> Verified game note.

![air-hockey screenshot placeholder](air-hockey-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/korial29/air-hockey](https://github.com/korial29/air-hockey)
- **Evidence:** [direct model evidence](https://github.com/korial29/air-hockey/commit/ee2d5a415612759ef779084200fd7462fb69ec7b)
- **Live demo:** [open demo](https://korial29.github.io/air-hockey/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Tiny multiplayer air hockey for the browser: zero runtime deps, WebSocket or same-browser multi-tab play, pluggable into any JS app. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/korial29/air-hockey/blob/master/src/client/render.ts](https://github.com/korial29/air-hockey/blob/master/src/client/render.ts)
- [https://github.com/korial29/air-hockey/commit/ee2d5a415612759ef779084200fd7462fb69ec7b](https://github.com/korial29/air-hockey/commit/ee2d5a415612759ef779084200fd7462fb69ec7b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/korial29/air-hockey

[Back to the awesome list](../../README.md)
