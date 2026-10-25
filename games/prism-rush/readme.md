# Prism Rush

> Verified game note.

![Prism Rush screenshot placeholder](prism-rush-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/Moha-df/prism-rush](https://github.com/Moha-df/prism-rush)
- **Evidence:** [direct model evidence](https://github.com/Moha-df/prism-rush/commit/5d3e1a24b4c024c95b35fabfe08b40b800b46478)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

FPS roguelike coopératif 1-4 joueurs en Rust + Bevy 0.20 — modèles procéduraux, jeu en ligne P2P (iroh) sans ouverture de port. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Moha-df/prism-rush/blob/master/src/render/icons.rs](https://github.com/Moha-df/prism-rush/blob/master/src/render/icons.rs)
- [https://github.com/Moha-df/prism-rush/commit/5d3e1a24b4c024c95b35fabfe08b40b800b46478](https://github.com/Moha-df/prism-rush/commit/5d3e1a24b4c024c95b35fabfe08b40b800b46478)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/Moha-df/prism-rush

[Back to the awesome list](../../README.md)
