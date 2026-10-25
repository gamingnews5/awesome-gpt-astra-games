# NEON RECKONING

> Verified game note.

![NEON RECKONING screenshot placeholder](neon-reckoning-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/threepoint7516/neon-reckoning](https://github.com/threepoint7516/neon-reckoning)
- **Evidence:** [direct model evidence](https://github.com/threepoint7516/neon-reckoning/commit/074f2dacde1f453ccccfc6cd898bdbf147b75ca0)
- **Live demo:** [open demo](https://neon-reckoning.netlify.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A free-to-play, browser-based arena shooter set in a bright, toy-like city at night, with real authoritative multiplayer. No accounts, no trackers, no paid advantages. Everything you see and hear (map, textures, models, sound, music) is generated procedurally… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/threepoint7516/neon-reckoning/blob/master/shared/src/sim/match.ts](https://github.com/threepoint7516/neon-reckoning/blob/master/shared/src/sim/match.ts)
- [https://github.com/threepoint7516/neon-reckoning/commit/074f2dacde1f453ccccfc6cd898bdbf147b75ca0](https://github.com/threepoint7516/neon-reckoning/commit/074f2dacde1f453ccccfc6cd898bdbf147b75ca0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/threepoint7516/neon-reckoning

[Back to the awesome list](../../README.md)
