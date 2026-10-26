# BLIND//FIRE

> Verified game note.

![BLIND//FIRE screenshot placeholder](blind-fire-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/kaankoch/BlindFire](https://github.com/kaankoch/BlindFire)
- **Evidence:** [direct model evidence](https://github.com/kaankoch/BlindFire/commit/4244d42ed9b0996438f378a57c8d5dfa74c06e4c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Pitch-black team deathmatch built with Next.js 16 + React 19 + Three.js. Everything is invisible. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kaankoch/BlindFire/blob/main/src/game/engine.ts](https://github.com/kaankoch/BlindFire/blob/main/src/game/engine.ts)
- [https://github.com/kaankoch/BlindFire/commit/4244d42ed9b0996438f378a57c8d5dfa74c06e4c](https://github.com/kaankoch/BlindFire/commit/4244d42ed9b0996438f378a57c8d5dfa74c06e4c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/kaankoch/BlindFire

[Back to the awesome list](../../README.md)
