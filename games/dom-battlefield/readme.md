# DOM Battlefield

> Verified game note.

![DOM Battlefield screenshot placeholder](dom-battlefield-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/coded-dot-design/dom-battlefield](https://github.com/coded-dot-design/dom-battlefield)
- **Evidence:** [direct model evidence](https://github.com/coded-dot-design/dom-battlefield/commit/1f13826e15215497d84266692a275712825905ae)
- **Live demo:** [open demo](https://coded-dot-design.github.io/dom-virus/battlefield/)
- **Additional live link:** [open demo](https://coded-dot-design.github.io/dom-battlefield/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A separate, lightweight squad-tactics app in the DOM Virus family. Battlefield builds the map, terrain, objectives and platoon simulation. Sherman Bytes owns the tank artwork and its cached renderer. Battlefield adds zero bytes to the Sherman game bundle. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/coded-dot-design/dom-battlefield/blob/main/src/client.ts](https://github.com/coded-dot-design/dom-battlefield/blob/main/src/client.ts)
- [https://github.com/coded-dot-design/dom-battlefield/commit/1f13826e15215497d84266692a275712825905ae](https://github.com/coded-dot-design/dom-battlefield/commit/1f13826e15215497d84266692a275712825905ae)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/coded-dot-design/dom-battlefield

[Back to the awesome list](../../README.md)
