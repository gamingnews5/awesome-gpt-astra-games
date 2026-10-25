# Logic Lab

> Verified game note.

![Logic Lab screenshot placeholder](logic-lab-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/awaisathar/logiclab](https://github.com/awaisathar/logiclab)
- **Evidence:** [direct model evidence](https://github.com/awaisathar/logiclab/commit/5b186179e1a799e3114796f53cc40ec20bb99998)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A playful logic gates game for kids. It runs in the browser as one self-contained page (index.html), with no build step and no dependencies. Open the file and play. The only outside request is the Google Fonts stylesheet, and the page works without it using… Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/awaisathar/logiclab/blob/main/index.html](https://github.com/awaisathar/logiclab/blob/main/index.html)
- [https://github.com/awaisathar/logiclab/commit/5b186179e1a799e3114796f53cc40ec20bb99998](https://github.com/awaisathar/logiclab/commit/5b186179e1a799e3114796f53cc40ec20bb99998)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/awaisathar/logiclab

[Back to the awesome list](../../README.md)
