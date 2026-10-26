# Blindspot (HackPSU Fall 2026)

> Verified game note.

![Blindspot (HackPSU Fall 2026) screenshot placeholder](blindspot-hackpsu-fall-2026-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Swift
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Orimaster354/hackpsu-fall-2026](https://github.com/Orimaster354/hackpsu-fall-2026)
- **Evidence:** [direct model evidence](https://github.com/Orimaster354/hackpsu-fall-2026/commit/d768fe26d864a4fd8001b4208272024def388995)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Blindspot is a social-deduction game, inspired by Among Us, played in a real room on four iPhones. Players walk to real task stations, do motion-based tasks, and try to find the impostor. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Orimaster354/hackpsu-fall-2026/blob/main/Tests/ARScanChecks/main.swift](https://github.com/Orimaster354/hackpsu-fall-2026/blob/main/Tests/ARScanChecks/main.swift)
- [https://github.com/Orimaster354/hackpsu-fall-2026/commit/d768fe26d864a4fd8001b4208272024def388995](https://github.com/Orimaster354/hackpsu-fall-2026/commit/d768fe26d864a4fd8001b4208272024def388995)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Orimaster354/hackpsu-fall-2026

[Back to the awesome list](../../README.md)
