# Family Quiz

> Verified game note.

![Family Quiz screenshot placeholder](family-quiz-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** Python, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/KenDarcy01/Quiz](https://github.com/KenDarcy01/Quiz)
- **Evidence:** [direct model evidence](https://github.com/KenDarcy01/Quiz/commit/60626eb24b56689e1a114dc3b99e7a1966e0aff9)
- **Live demo:** [open demo](https://kendarcy01.github.io/Quiz/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A pass-the-phone family quiz, built as a Progressive Web App (PWA). Each player gets questions graded for their own age (6 to adult), everyone answers question 1, then question 2, and so on, and a leaderboard closes each round. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/KenDarcy01/Quiz/blob/main/js/multiplayer.js](https://github.com/KenDarcy01/Quiz/blob/main/js/multiplayer.js)
- [https://github.com/KenDarcy01/Quiz/commit/60626eb24b56689e1a114dc3b99e7a1966e0aff9](https://github.com/KenDarcy01/Quiz/commit/60626eb24b56689e1a114dc3b99e7a1966e0aff9)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/KenDarcy01/Quiz

[Back to the awesome list](../../README.md)
