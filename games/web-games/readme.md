# Web Games

> Verified game note.

![Web Games screenshot placeholder](web-games-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Ridoy-MAX/web-games](https://github.com/Ridoy-MAX/web-games)
- **Evidence:** [direct model evidence](https://github.com/Ridoy-MAX/web-games/commit/d74ad029187978570e3feb64f41a53a59585f22f)
- **Live demo:** [open demo](https://web-games-lime.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Ridiculous browser games with serious leaderboards. Cow vs UFO (Three.js) + SQLite player profiles. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Ridoy-MAX/web-games/blob/main/games/office-brawl/src/fighters/Body.js](https://github.com/Ridoy-MAX/web-games/blob/main/games/office-brawl/src/fighters/Body.js)
- [https://github.com/Ridoy-MAX/web-games/commit/d74ad029187978570e3feb64f41a53a59585f22f](https://github.com/Ridoy-MAX/web-games/commit/d74ad029187978570e3feb64f41a53a59585f22f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Ridoy-MAX/web-games

[Back to the awesome list](../../README.md)
