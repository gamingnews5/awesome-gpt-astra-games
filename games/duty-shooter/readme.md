# Duty Shooter

> Verified game note.

![Duty Shooter screenshot placeholder](duty-shooter-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/aleixribera/duty-shooter](https://github.com/aleixribera/duty-shooter)
- **Evidence:** [direct model evidence](https://github.com/aleixribera/duty-shooter/commit/1ad2cef9d3ceb951b087a12a72241689760b4ed6)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser FPS test bed with MW2019-faithful gunplay and movement. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/aleixribera/duty-shooter/blob/main/packages/fps-client/src/viewmodel/m4a1.ts](https://github.com/aleixribera/duty-shooter/blob/main/packages/fps-client/src/viewmodel/m4a1.ts)
- [https://github.com/aleixribera/duty-shooter/commit/1ad2cef9d3ceb951b087a12a72241689760b4ed6](https://github.com/aleixribera/duty-shooter/commit/1ad2cef9d3ceb951b087a12a72241689760b4ed6)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/aleixribera/duty-shooter

[Back to the awesome list](../../README.md)
