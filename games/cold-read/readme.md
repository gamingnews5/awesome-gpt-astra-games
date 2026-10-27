# Cold Read

> Verified game note.

![Cold Read screenshot placeholder](cold-read-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/2Steazy/cold-read](https://github.com/2Steazy/cold-read)
- **Evidence:** [direct model evidence](https://github.com/2Steazy/cold-read/commit/c745fdcbcc6fafec060009462bb31435478f6c93)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A daily true-crime investigation in the browser. Each day opens a real, solved case. You read the files police gathered, choose which leads to follow, and make one arrest when you're sure. The arrest plays out all the way to sentencing. Only then do you find… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/2Steazy/cold-read/blob/main/game.js](https://github.com/2Steazy/cold-read/blob/main/game.js)
- [https://github.com/2Steazy/cold-read/commit/c745fdcbcc6fafec060009462bb31435478f6c93](https://github.com/2Steazy/cold-read/commit/c745fdcbcc6fafec060009462bb31435478f6c93)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/2Steazy/cold-read

[Back to the awesome list](../../README.md)
