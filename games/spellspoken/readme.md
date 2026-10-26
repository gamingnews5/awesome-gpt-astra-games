# SpellSpoken

> Verified game note.

![SpellSpoken screenshot placeholder](spellspoken-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Fable 5.1
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/nottec/SpellSpoken](https://github.com/nottec/SpellSpoken)
- **Evidence:** [direct model evidence](https://github.com/nottec/SpellSpoken/commit/f0f89a2984d77cf9bbdd1acde556285b448bd06c)
- **Live demo:** [open demo](https://spellspoken.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A pronunciation roguelike for Spanish and Mandarin, built at HackTX 2026. Commit carries an exact Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nottec/SpellSpoken/blob/master/lib/engine.ts](https://github.com/nottec/SpellSpoken/blob/master/lib/engine.ts)
- [https://github.com/nottec/SpellSpoken/commit/f0f89a2984d77cf9bbdd1acde556285b448bd06c](https://github.com/nottec/SpellSpoken/commit/f0f89a2984d77cf9bbdd1acde556285b448bd06c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/nottec/SpellSpoken

[Back to the awesome list](../../README.md)
