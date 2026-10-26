# Lines

> Verified game note.

![Lines screenshot placeholder](lines-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/timbortnik/lines](https://github.com/timbortnik/lines)
- **Evidence:** [direct model evidence](https://github.com/timbortnik/lines/commit/1a550df831fea5a91e0a42d403f918f566bfad7c)
- **Live demo:** [open demo](https://timbortnik.github.io/lines/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An open-source browser version of Color Lines, also known as Lines98: move balls on a 9×9 board to line up five or more of the same color. It is an installable web app that works offline and keeps your game on your device, with no backend. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/timbortnik/lines/blob/main/src/game/game.ts](https://github.com/timbortnik/lines/blob/main/src/game/game.ts)
- [https://github.com/timbortnik/lines/commit/1a550df831fea5a91e0a42d403f918f566bfad7c](https://github.com/timbortnik/lines/commit/1a550df831fea5a91e0a42d403f918f566bfad7c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/timbortnik/lines

[Back to the awesome list](../../README.md)
