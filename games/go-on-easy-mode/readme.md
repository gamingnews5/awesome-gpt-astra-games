# Go on Easy Mode

> Verified game note.

![Go on Easy Mode screenshot placeholder](go-on-easy-mode-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Go, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/cbelsole/easygo](https://github.com/cbelsole/easygo)
- **Evidence:** [direct model evidence](https://github.com/cbelsole/easygo/commit/c475ae3169df4a3ad57cccc7d23cc0696f6d2bbb)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Go (baduk) client with a KataGo opponent you can set to a rank (20k-9d), live joseki recognition, tactical shape sensing, and OGS-style clocks. Go backend, React + Vite+ frontend. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cbelsole/easygo/blob/main/web/src/components/GameScreen.tsx](https://github.com/cbelsole/easygo/blob/main/web/src/components/GameScreen.tsx)
- [https://github.com/cbelsole/easygo/commit/c475ae3169df4a3ad57cccc7d23cc0696f6d2bbb](https://github.com/cbelsole/easygo/commit/c475ae3169df4a3ad57cccc7d23cc0696f6d2bbb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/cbelsole/easygo

[Back to the awesome list](../../README.md)
