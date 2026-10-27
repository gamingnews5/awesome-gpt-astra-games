# Overclocked

> Verified game note.

![Overclocked screenshot placeholder](overclocked-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/danjaekim/overclocked](https://github.com/danjaekim/overclocked)
- **Evidence:** [direct model evidence](https://github.com/danjaekim/overclocked/commit/ae04410575fe9097f5b7c8e7c2dff27bbef9a329)
- **Live demo:** [open demo](https://danjaekim.github.io/overclocked/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A mobile-first survivors-style roguelike where you program your power. Your character fires on its own, and what it fires comes from a rig: short chains that start with a rule card (when it runs) and continue with weapons, modifiers and triggers read left to… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/danjaekim/overclocked/blob/main/tools/bench.mjs](https://github.com/danjaekim/overclocked/blob/main/tools/bench.mjs)
- [https://github.com/danjaekim/overclocked/commit/ae04410575fe9097f5b7c8e7c2dff27bbef9a329](https://github.com/danjaekim/overclocked/commit/ae04410575fe9097f5b7c8e7c2dff27bbef9a329)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/danjaekim/overclocked

[Back to the awesome list](../../README.md)
