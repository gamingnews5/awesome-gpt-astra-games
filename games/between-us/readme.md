# Between Us

> Verified game note.

![Between Us screenshot placeholder](between-us-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Pavan-PM-Portfolio/bobba_zone](https://github.com/Pavan-PM-Portfolio/bobba_zone)
- **Evidence:** [direct model evidence](https://github.com/Pavan-PM-Portfolio/bobba_zone/commit/8d603b94239ef1629caf0d2b2de6b4db0bbf8e4f)
- **Live demo:** [open demo](https://pavan-pm-portfolio.github.io/bobba_zone/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A private app of ten real-time games for two partners, each played on your own phone. Answers stay hidden until the game's reveal rule is met, and everything you finish is kept in a shared history with saved moments. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Pavan-PM-Portfolio/bobba_zone/blob/main/src/games/after-dark/modes/VelvetGame.tsx](https://github.com/Pavan-PM-Portfolio/bobba_zone/blob/main/src/games/after-dark/modes/VelvetGame.tsx)
- [https://github.com/Pavan-PM-Portfolio/bobba_zone/commit/8d603b94239ef1629caf0d2b2de6b4db0bbf8e4f](https://github.com/Pavan-PM-Portfolio/bobba_zone/commit/8d603b94239ef1629caf0d2b2de6b4db0bbf8e4f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Pavan-PM-Portfolio/bobba_zone

[Back to the awesome list](../../README.md)
