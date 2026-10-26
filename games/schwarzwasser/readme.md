# Schwarzwasser

> Verified game note.

![Schwarzwasser screenshot placeholder](schwarzwasser-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/eXtro181/PirateGame](https://github.com/eXtro181/PirateGame)
- **Evidence:** [direct model evidence](https://github.com/eXtro181/PirateGame/commit/b19b9f39082ecd53cb9426f3bfa5745571dca009)
- **Live demo:** [open demo](https://extro181.github.io/PirateGame/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Ein düsteres Soulslike-Piratenspiel im Browser in HD-Pixelart (Top-Down-3/4-Sicht), Kampf wie Dark Souls, gebaut mit einem eigenen kleinen WebGL2-Renderer. Alle Grafiken, Shantys und Klänge entstehen beim Start aus Code – es gibt keine Bild- oder Audiodateien. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/eXtro181/PirateGame/blob/main/src/world/mod.rs](https://github.com/eXtro181/PirateGame/blob/main/src/world/mod.rs)
- [https://github.com/eXtro181/PirateGame/commit/b19b9f39082ecd53cb9426f3bfa5745571dca009](https://github.com/eXtro181/PirateGame/commit/b19b9f39082ecd53cb9426f3bfa5745571dca009)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/eXtro181/PirateGame

[Back to the awesome list](../../README.md)
