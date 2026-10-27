# Poke Brawl

> Verified game note.

![Poke Brawl screenshot placeholder](poke-brawl-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/preston93lane/Poke-brawl-](https://github.com/preston93lane/Poke-brawl-)
- **Evidence:** [direct model evidence](https://github.com/preston93lane/Poke-brawl-/commit/686f26559fc2ed61114573567af5629a5d9c88e1)
- **Live demo:** [open demo](https://preston93lane.github.io/Poke-brawl-/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A game that runs like brawl stars but with Pokémon as the brawlers. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/preston93lane/Poke-brawl-/blob/claude/pokemon-brawl-stars-godot-88r0k1/scripts/brawler.gd](https://github.com/preston93lane/Poke-brawl-/blob/claude/pokemon-brawl-stars-godot-88r0k1/scripts/brawler.gd)
- [https://github.com/preston93lane/Poke-brawl-/commit/686f26559fc2ed61114573567af5629a5d9c88e1](https://github.com/preston93lane/Poke-brawl-/commit/686f26559fc2ed61114573567af5629a5d9c88e1)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/preston93lane/Poke-brawl-

[Back to the awesome list](../../README.md)
