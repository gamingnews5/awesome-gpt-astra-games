# Who's Lying?

> Verified game note.

![Who's Lying? screenshot placeholder](who-s-lying-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** Flutter, Dart
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/R4Flutter/WhoLies](https://github.com/R4Flutter/WhoLies)
- **Evidence:** [direct model evidence](https://github.com/R4Flutter/WhoLies/commit/4c0bff15ae01fc20087f1a9686d7e865a68bbc1e)
- **Live demo:** [open demo](https://r4flutter.github.io/WhoLies/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A daily detective game for the browser. Every day there are 5 short cases. In each one, the police checked some facts and 3 suspects tell their story. One story can't be true. Players tap the liar, then share a spoiler-free result like this. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/R4Flutter/WhoLies/blob/main/js/cases.js](https://github.com/R4Flutter/WhoLies/blob/main/js/cases.js)
- [https://github.com/R4Flutter/WhoLies/commit/4c0bff15ae01fc20087f1a9686d7e865a68bbc1e](https://github.com/R4Flutter/WhoLies/commit/4c0bff15ae01fc20087f1a9686d7e865a68bbc1e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/R4Flutter/WhoLies

[Back to the awesome list](../../README.md)
