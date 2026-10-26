# Zomb Survive

> Verified game note.

![Zomb Survive screenshot placeholder](zomb-survive-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/zrsavage/Zomb-survive](https://github.com/zrsavage/Zomb-survive)
- **Evidence:** [direct model evidence](https://github.com/zrsavage/Zomb-survive/commit/a03339e4361deae7bdba294cc9a2f80cb12973d8)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A top-down pixel-art survival / base-defence game that runs in the browser. Open index.html (no build step, no dependencies, all audio is synthesised). Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/zrsavage/Zomb-survive/blob/claude/inspiring-knuth-o9r7rt/js/sim.js](https://github.com/zrsavage/Zomb-survive/blob/claude/inspiring-knuth-o9r7rt/js/sim.js)
- [https://github.com/zrsavage/Zomb-survive/commit/a03339e4361deae7bdba294cc9a2f80cb12973d8](https://github.com/zrsavage/Zomb-survive/commit/a03339e4361deae7bdba294cc9a2f80cb12973d8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/zrsavage/Zomb-survive

[Back to the awesome list](../../README.md)
