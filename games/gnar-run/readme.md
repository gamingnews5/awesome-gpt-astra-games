# Gnar Run

> Verified game note.

![Gnar Run screenshot placeholder](gnar-run-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/webgnar/skate-rogue](https://github.com/webgnar/skate-rogue)
- **Evidence:** [direct model evidence](https://github.com/webgnar/skate-rogue/commit/46e562765ae5bec829efc40d5218c0682508582a)
- **Live demo:** [open demo](https://skate-rogue.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A mobile-first 3D roguelike skate game in JavaScript: the Lou Gnar runner remade with Quest For Stoken's skate. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/webgnar/skate-rogue/blob/main/src/game/game.ts](https://github.com/webgnar/skate-rogue/blob/main/src/game/game.ts)
- [https://github.com/webgnar/skate-rogue/commit/46e562765ae5bec829efc40d5218c0682508582a](https://github.com/webgnar/skate-rogue/commit/46e562765ae5bec829efc40d5218c0682508582a)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/webgnar/skate-rogue

[Back to the awesome list](../../README.md)
