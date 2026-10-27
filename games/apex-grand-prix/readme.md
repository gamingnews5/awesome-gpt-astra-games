# Apex Grand Prix

> Verified game note.

![Apex Grand Prix screenshot placeholder](apex-grand-prix-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/jkempy2009-lang/claudeF1game](https://github.com/jkempy2009-lang/claudeF1game)
- **Evidence:** [direct model evidence](https://github.com/jkempy2009-lang/claudeF1game/commit/95dfc203975a1cbce9bae75910ebd2858169fb6e)
- **Live demo:** [open demo](https://claudef1game.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D Formula-style racing game that runs in the browser. Twenty cars, twelve original circuits, a physics model built from first principles (not a canned arcade handling model), and an AI field with adjustable difficulty. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jkempy2009-lang/claudeF1game/blob/claude/epic-keller-w3tz4v/docs/game.js](https://github.com/jkempy2009-lang/claudeF1game/blob/claude/epic-keller-w3tz4v/docs/game.js)
- [https://github.com/jkempy2009-lang/claudeF1game/commit/95dfc203975a1cbce9bae75910ebd2858169fb6e](https://github.com/jkempy2009-lang/claudeF1game/commit/95dfc203975a1cbce9bae75910ebd2858169fb6e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/jkempy2009-lang/claudeF1game

[Back to the awesome list](../../README.md)
