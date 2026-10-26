# Neon Rush

> Verified game note.

![Neon Rush screenshot placeholder](neon-rush-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/vedshubham58-crypto/Chalk-Rush](https://github.com/vedshubham58-crypto/Chalk-Rush)
- **Evidence:** [direct model evidence](https://github.com/vedshubham58-crypto/Chalk-Rush/commit/9632125af5ad02a2d856b9d17e23f4b2d1f9d0eb)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An Android game: ride a glowing bike around a neon grid, loop back to your zone to claim land, and hit other riders' light trails to knock them out. (The repo is still called Chalk-Rush from the first version.). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/vedshubham58-crypto/Chalk-Rush/blob/main/godot/scripts/main.gd](https://github.com/vedshubham58-crypto/Chalk-Rush/blob/main/godot/scripts/main.gd)
- [https://github.com/vedshubham58-crypto/Chalk-Rush/commit/9632125af5ad02a2d856b9d17e23f4b2d1f9d0eb](https://github.com/vedshubham58-crypto/Chalk-Rush/commit/9632125af5ad02a2d856b9d17e23f4b2d1f9d0eb)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/vedshubham58-crypto/Chalk-Rush

[Back to the awesome list](../../README.md)
