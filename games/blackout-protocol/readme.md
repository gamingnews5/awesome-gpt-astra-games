# Blackout Protocol

> Verified game note.

![Blackout Protocol screenshot placeholder](blackout-protocol-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Sonnet 5.5
- **Technology:** Roblox, Luau
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/cckhaw/gridlock](https://github.com/cckhaw/gridlock)
- **Evidence:** [direct model evidence](https://github.com/cckhaw/gridlock/commit/4e22ba959a656593d741c5afffabfe3c6d12d347)
- **Live demo:** [open demo](https://gridlock-ecru-pi.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

SCADA-style power grid crisis game — mobile-first, zero-install, installable and playable offline. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/cckhaw/gridlock/blob/claude/youthful-newton-dgl82c/src/city/CityScene.tsx](https://github.com/cckhaw/gridlock/blob/claude/youthful-newton-dgl82c/src/city/CityScene.tsx)
- [https://github.com/cckhaw/gridlock/commit/4e22ba959a656593d741c5afffabfe3c6d12d347](https://github.com/cckhaw/gridlock/commit/4e22ba959a656593d741c5afffabfe3c6d12d347)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/cckhaw/gridlock

[Back to the awesome list](../../README.md)
