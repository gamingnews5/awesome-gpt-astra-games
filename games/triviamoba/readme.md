# TriviaMoba

> Verified game note.

![TriviaMoba screenshot placeholder](triviamoba-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/okayline/triviamoba](https://github.com/okayline/triviamoba)
- **Evidence:** [direct model evidence](https://github.com/okayline/triviamoba/commit/cecdfe9475600c365c7e68327a55b6707658c329)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Trivia in three MOBA lanes. Draft 3 of 6 creatures into the lanes, answer each question, and push your marker in from the edge toward the common goal: a right answer pushes 2 (INT heals 1 in a lane you pick), a wrong one lets the map's wave push you back 1.… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/okayline/triviamoba/blob/main/public/index.html](https://github.com/okayline/triviamoba/blob/main/public/index.html)
- [https://github.com/okayline/triviamoba/commit/cecdfe9475600c365c7e68327a55b6707658c329](https://github.com/okayline/triviamoba/commit/cecdfe9475600c365c7e68327a55b6707658c329)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/okayline/triviamoba

[Back to the awesome list](../../README.md)
