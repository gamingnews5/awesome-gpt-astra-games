# Off the Map

> Verified game note.

![Off the Map screenshot placeholder](off-the-map-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/KingstonAD/Off-the-map](https://github.com/KingstonAD/Off-the-map)
- **Evidence:** [direct model evidence](https://github.com/KingstonAD/Off-the-map/commit/c1767d54df55a7d68c482910304460ad4fcee30a)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Daily geography trivia. 7 stops, 20 seconds each, and rare answers travel farther. See BUILDSPEC.md for the rules and design/ for the brand book. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/KingstonAD/Off-the-map/blob/main/lib/game.ts](https://github.com/KingstonAD/Off-the-map/blob/main/lib/game.ts)
- [https://github.com/KingstonAD/Off-the-map/commit/c1767d54df55a7d68c482910304460ad4fcee30a](https://github.com/KingstonAD/Off-the-map/commit/c1767d54df55a7d68c482910304460ad4fcee30a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/KingstonAD/Off-the-map

[Back to the awesome list](../../README.md)
