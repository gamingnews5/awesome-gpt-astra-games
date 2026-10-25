# Quizzo

> Verified game note.

![Quizzo screenshot placeholder](quizzo-placeholder.svg)

## At a glance

- **Score:** 6.9/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/LupangSyS/Kahoot](https://github.com/LupangSyS/Kahoot)
- **Evidence:** [direct model evidence](https://github.com/LupangSyS/Kahoot/commit/80ef89c731e7aa475527c08eec7484996ffc939c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Live quiz game: guests scan a QR code, answer on their phones, the big screen shows questions, results and a leaderboard in real time. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/LupangSyS/Kahoot/blob/ccr-896a5c2b-g2qaap/server.js](https://github.com/LupangSyS/Kahoot/blob/ccr-896a5c2b-g2qaap/server.js)
- [https://github.com/LupangSyS/Kahoot/commit/80ef89c731e7aa475527c08eec7484996ffc939c](https://github.com/LupangSyS/Kahoot/commit/80ef89c731e7aa475527c08eec7484996ffc939c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/LupangSyS/Kahoot

[Back to the awesome list](../../README.md)
