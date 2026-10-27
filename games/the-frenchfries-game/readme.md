# The Frenchfries Game

> Verified game note.

![The Frenchfries Game screenshot placeholder](the-frenchfries-game-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/t00bstAr/frenchfries](https://github.com/t00bstAr/frenchfries)
- **Evidence:** [direct model evidence](https://github.com/t00bstAr/frenchfries/commit/76703b7fff27296d18ac8e5569fa85be06ced7d8)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

The whole game is one file, index.html. Vs computer and pass-the-phone work straight away. Online play ("Own phones") uses Supabase Realtime, so it needs a free Supabase project. You don't need a database, tables or a server of your own. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/t00bstAr/frenchfries/blob/main/index.html](https://github.com/t00bstAr/frenchfries/blob/main/index.html)
- [https://github.com/t00bstAr/frenchfries/commit/76703b7fff27296d18ac8e5569fa85be06ced7d8](https://github.com/t00bstAr/frenchfries/commit/76703b7fff27296d18ac8e5569fa85be06ced7d8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/t00bstAr/frenchfries

[Back to the awesome list](../../README.md)
