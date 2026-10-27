# Nosum

> Top-list entry: **today** (#5).

![Nosum screenshot](https://raw.githubusercontent.com/ppn-systems/nosum/master/docs/qa/art-upgrade-ingame-coop-exterior-1280x720.png)

## At a glance

- **Score:** 8.3/10
- **Screenshot rating:** 6.6/10 ([manually reviewed image](https://github.com/ppn-systems/nosum/blob/master/docs/qa/art-upgrade-ingame-coop-exterior-1280x720.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/ppn-systems/nosum](https://github.com/ppn-systems/nosum)
- **Evidence:** [direct model evidence](https://github.com/ppn-systems/nosum/commit/091148c4e83146485c72e0492e1c40115deb81f9)
- **Live demo:** [open demo](https://farm.ppnsys.com)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ppn-systems/nosum/blob/master/docs/qa/art-upgrade-ingame-coop-exterior-1280x720.png) — 📸 6.6/10 · manual visual review · Use this frame for the game-level score. Top-down pixel village with houses, path and inventory bar; detailed and cohesive.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser-based multiplayer farming game in 3/4 top-down pixel art. The client is Blazor WebAssembly with its own. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ppn-systems/nosum/blob/master/server/Nosum.Infrastructure/Persistence/Migrations/20261025200256_CoopUpgrades.Designer.cs](https://github.com/ppn-systems/nosum/blob/master/server/Nosum.Infrastructure/Persistence/Migrations/20261025200256_CoopUpgrades.Designer.cs)
- [https://github.com/ppn-systems/nosum/commit/091148c4e83146485c72e0492e1c40115deb81f9](https://github.com/ppn-systems/nosum/commit/091148c4e83146485c72e0492e1c40115deb81f9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/ppn-systems/nosum

[Back to the awesome list](../../README.md)
