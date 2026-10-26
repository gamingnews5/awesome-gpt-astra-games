# RSDP Poker Live!

> Verified game note.

![RSDP Poker Live! screenshot placeholder](rsdp-poker-live-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/jcolter11374/rsdp-poker-live](https://github.com/jcolter11374/rsdp-poker-live)
- **Evidence:** [direct model evidence](https://github.com/jcolter11374/rsdp-poker-live/commit/b810e2435d37e7188107900b7713458db69e6a7f)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Browser poker for friends, no sign-up. A host creates a cash table or a tournament, shares the link, and everyone plays in real time. Every game and option is free for everyone. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jcolter11374/rsdp-poker-live/blob/main/apps/server/src/runtime/table.ts](https://github.com/jcolter11374/rsdp-poker-live/blob/main/apps/server/src/runtime/table.ts)
- [https://github.com/jcolter11374/rsdp-poker-live/commit/b810e2435d37e7188107900b7713458db69e6a7f](https://github.com/jcolter11374/rsdp-poker-live/commit/b810e2435d37e7188107900b7713458db69e6a7f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/jcolter11374/rsdp-poker-live

[Back to the awesome list](../../README.md)
