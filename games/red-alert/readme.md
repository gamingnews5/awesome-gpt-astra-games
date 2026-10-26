# Red Alert

> Verified game note.

![Red Alert screenshot placeholder](red-alert-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/CrawfishChowder/GDSCHackathon](https://github.com/CrawfishChowder/GDSCHackathon)
- **Evidence:** [direct model evidence](https://github.com/CrawfishChowder/GDSCHackathon/commit/54af4946ac68c012479abad19d7b575cf655d90b)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A first-person survival game in a habitat module. Over one five-minute shift, life-critical systems fail and you fix them by hand. One mistake kills you instantly, and the mission log tells you which real spaceflight disaster your mistake mirrors. Players… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/CrawfishChowder/GDSCHackathon/blob/main/red-alert/scripts/stage1/industrial_room_shell.gd](https://github.com/CrawfishChowder/GDSCHackathon/blob/main/red-alert/scripts/stage1/industrial_room_shell.gd)
- [https://github.com/CrawfishChowder/GDSCHackathon/commit/54af4946ac68c012479abad19d7b575cf655d90b](https://github.com/CrawfishChowder/GDSCHackathon/commit/54af4946ac68c012479abad19d7b575cf655d90b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/CrawfishChowder/GDSCHackathon

[Back to the awesome list](../../README.md)
