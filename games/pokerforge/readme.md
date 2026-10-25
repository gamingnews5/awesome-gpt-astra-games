# Pokerforge

> Verified game note.

![Pokerforge screenshot placeholder](pokerforge-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, PixiJS, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/saveriobanchi/Pokerforge](https://github.com/saveriobanchi/Pokerforge)
- **Evidence:** [direct model evidence](https://github.com/saveriobanchi/Pokerforge/commit/994d112d1944d596a5351af2aa782a231abb4e61)
- **Live demo:** [open demo](https://saveriobanchi.github.io/Pokerforge/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A mobile-first sky-casino game built on the Aetherforge engine: the same. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/saveriobanchi/Pokerforge/blob/claude/pokerforge-casino/src/render/blocks/models/buildings.ts](https://github.com/saveriobanchi/Pokerforge/blob/claude/pokerforge-casino/src/render/blocks/models/buildings.ts)
- [https://github.com/saveriobanchi/Pokerforge/commit/994d112d1944d596a5351af2aa782a231abb4e61](https://github.com/saveriobanchi/Pokerforge/commit/994d112d1944d596a5351af2aa782a231abb4e61)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/saveriobanchi/Pokerforge

[Back to the awesome list](../../README.md)
