# Riftward

> Verified game note.

![Riftward screenshot placeholder](riftward-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Foxworks-Studios/riftward](https://github.com/Foxworks-Studios/riftward)
- **Evidence:** [direct model evidence](https://github.com/Foxworks-Studios/riftward/commit/deafb8907aec60000b4b35c717652c8e5b19ef21)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A classless telnet MUD on a headless Bevy server, in Rust: characters are defined by the skills they learn and use. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Foxworks-Studios/riftward/blob/master/src/items.rs](https://github.com/Foxworks-Studios/riftward/blob/master/src/items.rs)
- [https://github.com/Foxworks-Studios/riftward/commit/deafb8907aec60000b4b35c717652c8e5b19ef21](https://github.com/Foxworks-Studios/riftward/commit/deafb8907aec60000b4b35c717652c8e5b19ef21)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Foxworks-Studios/riftward

[Back to the awesome list](../../README.md)
