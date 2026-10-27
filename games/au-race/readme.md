# AU Race

> Verified game note.

![AU Race screenshot placeholder](au-race-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/AU-PSK/AU_RACE](https://github.com/AU-PSK/AU_RACE)
- **Evidence:** [direct model evidence](https://github.com/AU-PSK/AU_RACE/commit/6c7512f0f54c6074aea2c0febc8afa506b7159ab)
- **Live demo:** [open demo](https://au-psk.github.io/AU_RACE/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Uofficielt browserbaseret 3D-gokartspil inspireret af Universitetsparken. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/AU-PSK/AU_RACE/blob/main/client/src/campus-data.ts](https://github.com/AU-PSK/AU_RACE/blob/main/client/src/campus-data.ts)
- [https://github.com/AU-PSK/AU_RACE/commit/6c7512f0f54c6074aea2c0febc8afa506b7159ab](https://github.com/AU-PSK/AU_RACE/commit/6c7512f0f54c6074aea2c0febc8afa506b7159ab)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/AU-PSK/AU_RACE

[Back to the awesome list](../../README.md)
