# GSB World

> Verified game note.

![GSB World screenshot placeholder](gsb-world-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** Python, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/jamescstapleton/gsbworld](https://github.com/jamescstapleton/gsbworld)
- **Evidence:** [direct model evidence](https://github.com/jamescstapleton/gsbworld/commit/aa1b6fd9602ceaaa309acc3fd573847b41cd5475)
- **Live demo:** [open demo](https://jamescstapleton.github.io/gsbworld/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Stanford Business School simulator. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jamescstapleton/gsbworld/blob/main/gsb_campus.py](https://github.com/jamescstapleton/gsbworld/blob/main/gsb_campus.py)
- [https://github.com/jamescstapleton/gsbworld/commit/aa1b6fd9602ceaaa309acc3fd573847b41cd5475](https://github.com/jamescstapleton/gsbworld/commit/aa1b6fd9602ceaaa309acc3fd573847b41cd5475)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/jamescstapleton/gsbworld

[Back to the awesome list](../../README.md)
