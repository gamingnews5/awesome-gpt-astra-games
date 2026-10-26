# Shardbreaker (roguelike)

> Verified game note.

![Shardbreaker (roguelike) screenshot placeholder](shardbreaker-roguelike-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/JakeA-UKSBS/Shardbreaker](https://github.com/JakeA-UKSBS/Shardbreaker)
- **Evidence:** [direct model evidence](https://github.com/JakeA-UKSBS/Shardbreaker/commit/9424cfe395a04ea75fea8522a361130376c90fb1)
- **Live demo:** [open demo](https://jakea-uksbs.github.io/Shardbreaker/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A run-based tactics roguelike in the style of GBA Fire Emblem. Built for PC first (map left, command panel right), and still playable on phones. Forked from Nightbound's engine. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/JakeA-UKSBS/Shardbreaker/blob/main/js/03-pixel-art.js](https://github.com/JakeA-UKSBS/Shardbreaker/blob/main/js/03-pixel-art.js)
- [https://github.com/JakeA-UKSBS/Shardbreaker/commit/9424cfe395a04ea75fea8522a361130376c90fb1](https://github.com/JakeA-UKSBS/Shardbreaker/commit/9424cfe395a04ea75fea8522a361130376c90fb1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/JakeA-UKSBS/Shardbreaker

[Back to the awesome list](../../README.md)
