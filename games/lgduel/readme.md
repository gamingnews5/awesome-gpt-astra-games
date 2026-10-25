# LGDuel

> Verified game note.

![LGDuel screenshot placeholder](lgduel-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Rust, React
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/s0pk/lgduel](https://github.com/s0pk/lgduel)
- **Evidence:** [direct model evidence](https://github.com/s0pk/lgduel/commit/eda58594763480475f4349d93bd6c9793a567196)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Standalone Lightning-Gun duel trainer: vamp duels, arena-shooter movement, anti-lag / no-anti-lag netcode, practice bots. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/s0pk/lgduel/blob/main/crates/client/src/main.rs](https://github.com/s0pk/lgduel/blob/main/crates/client/src/main.rs)
- [https://github.com/s0pk/lgduel/commit/eda58594763480475f4349d93bd6c9793a567196](https://github.com/s0pk/lgduel/commit/eda58594763480475f4349d93bd6c9793a567196)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/s0pk/lgduel

[Back to the awesome list](../../README.md)
