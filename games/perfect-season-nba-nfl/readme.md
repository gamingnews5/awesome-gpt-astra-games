# Perfect Season (NBA + NFL)

> Verified game note.

![Perfect Season (NBA + NFL) screenshot placeholder](perfect-season-nba-nfl-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/QemmHD/perfect-season](https://github.com/QemmHD/perfect-season)
- **Evidence:** [direct model evidence](https://github.com/QemmHD/perfect-season/commit/691daf8bd1c1ee6e09e9232fe5fc0f57d543ab80)
- **Live demo:** [open demo](https://qemmhd.github.io/perfect-season/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Spin a random NBA or NFL team and decade, draft players who played for them, and try for a perfect season: 82-0, then 16-0 in the playoffs, or 17-0 and four straight playoff wins through the Super Bowl. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/QemmHD/perfect-season/blob/main/src/ui/Draft.tsx](https://github.com/QemmHD/perfect-season/blob/main/src/ui/Draft.tsx)
- [https://github.com/QemmHD/perfect-season/commit/691daf8bd1c1ee6e09e9232fe5fc0f57d543ab80](https://github.com/QemmHD/perfect-season/commit/691daf8bd1c1ee6e09e9232fe5fc0f57d543ab80)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/QemmHD/perfect-season

[Back to the awesome list](../../README.md)
