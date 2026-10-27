# Jackaroo

> Verified game note.

![Jackaroo screenshot placeholder](jackaroo-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** Java
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/12tifa12/Jackaroo](https://github.com/12tifa12/Jackaroo)
- **Evidence:** [direct model evidence](https://github.com/12tifa12/Jackaroo/commit/42e78bf1ec17246fd5eea66844a35419a3bce89d)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A JavaFX version of Jackaroo, the marbles-and-cards board game, with a Balatro-inspired pixel UI. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/12tifa12/Jackaroo/blob/main/src/application/GameScreen.java](https://github.com/12tifa12/Jackaroo/blob/main/src/application/GameScreen.java)
- [https://github.com/12tifa12/Jackaroo/commit/42e78bf1ec17246fd5eea66844a35419a3bce89d](https://github.com/12tifa12/Jackaroo/commit/42e78bf1ec17246fd5eea66844a35419a3bce89d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/12tifa12/Jackaroo

[Back to the awesome list](../../README.md)
