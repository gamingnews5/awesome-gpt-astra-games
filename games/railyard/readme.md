# Railyard

> Verified game note.

![Railyard screenshot placeholder](railyard-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Fable 5.1
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/dettonijr/ticket-to-ride](https://github.com/dettonijr/ticket-to-ride)
- **Evidence:** [direct model evidence](https://github.com/dettonijr/ticket-to-ride/commit/3ed128bb49032eba4659bdcc37fa1b1a7cd7db8b)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Online Ticket to Ride for two to five friends. One person creates a game and shares a code; everyone else joins from a browser. The official 2015 USA rules run on the server. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/dettonijr/ticket-to-ride/blob/main/packages/engine/src/data/usa.ts](https://github.com/dettonijr/ticket-to-ride/blob/main/packages/engine/src/data/usa.ts)
- [https://github.com/dettonijr/ticket-to-ride/commit/3ed128bb49032eba4659bdcc37fa1b1a7cd7db8b](https://github.com/dettonijr/ticket-to-ride/commit/3ed128bb49032eba4659bdcc37fa1b1a7cd7db8b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/dettonijr/ticket-to-ride

[Back to the awesome list](../../README.md)
