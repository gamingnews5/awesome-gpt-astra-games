# wizaaahhh!

> Verified game note.

![wizaaahhh! screenshot placeholder](wizaaahhh-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/tarpat/hacktx-2026](https://github.com/tarpat/hacktx-2026)
- **Evidence:** [direct model evidence](https://github.com/tarpat/hacktx-2026/commit/e7f5ac6b3306484b5a8864b63a956cbbdd343f3b)
- **Live demo:** [open demo](https://v-ktor.itch.io/spell-animations)
- **Additional live link:** [open demo](https://tornadogames.itch.io/magic-sparksattacks-for-the-devs)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A real-time 1v1 browser game where two wizards cast spells with hand gestures, block attacks, and compete in camera-based collision challenges. Built for HackTX 2026 with React, Phaser, MediaPipe, and an authoritative Socket.IO server. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/tarpat/hacktx-2026/blob/main/client/src/arena/ArenaScene.ts](https://github.com/tarpat/hacktx-2026/blob/main/client/src/arena/ArenaScene.ts)
- [https://github.com/tarpat/hacktx-2026/commit/e7f5ac6b3306484b5a8864b63a956cbbdd343f3b](https://github.com/tarpat/hacktx-2026/commit/e7f5ac6b3306484b5a8864b63a956cbbdd343f3b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/tarpat/hacktx-2026

[Back to the awesome list](../../README.md)
