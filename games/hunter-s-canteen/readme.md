# Hunter's Canteen

> Verified game note.

![Hunter's Canteen screenshot placeholder](hunter-s-canteen-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/vibecoding3/mh-restaurant](https://github.com/vibecoding3/mh-restaurant)
- **Evidence:** [direct model evidence](https://github.com/vibecoding3/mh-restaurant/commit/c1aeb4e99d173bd213a04fd8c41b92ae6ae6d7c0)
- **Live demo:** [open demo](https://vibecoding3.github.io/mh-restaurant/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

You play a Palico chef who has just taken over a run-down canteen in a hunting village. Hunters come in before their quests and order hearty meals. Cook them well and the hunters set out with better buffs, come back alive, and bring you rare monster… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/vibecoding3/mh-restaurant/blob/main/src/scenes/ServiceScene.ts](https://github.com/vibecoding3/mh-restaurant/blob/main/src/scenes/ServiceScene.ts)
- [https://github.com/vibecoding3/mh-restaurant/commit/c1aeb4e99d173bd213a04fd8c41b92ae6ae6d7c0](https://github.com/vibecoding3/mh-restaurant/commit/c1aeb4e99d173bd213a04fd8c41b92ae6ae6d7c0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/vibecoding3/mh-restaurant

[Back to the awesome list](../../README.md)
