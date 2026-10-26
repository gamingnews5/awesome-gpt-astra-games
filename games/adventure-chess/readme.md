# Adventure Chess

> Verified game note.

![Adventure Chess screenshot placeholder](adventure-chess-placeholder.svg)

## At a glance

- **Score:** 7.0/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/hdunkel/adventure-chess](https://github.com/hdunkel/adventure-chess)
- **Evidence:** [direct model evidence](https://github.com/hdunkel/adventure-chess/commit/87af3388b305be62a5f6ecdc5c201b4be25e7c4c)
- **Live demo:** [open demo](https://hdunkel.github.io/adventure-chess/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Adventure Chess is a card add-on for chess. This repo contains the web app. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/hdunkel/adventure-chess/blob/main/src/App.tsx](https://github.com/hdunkel/adventure-chess/blob/main/src/App.tsx)
- [https://github.com/hdunkel/adventure-chess/commit/87af3388b305be62a5f6ecdc5c201b4be25e7c4c](https://github.com/hdunkel/adventure-chess/commit/87af3388b305be62a5f6ecdc5c201b4be25e7c4c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/hdunkel/adventure-chess

[Back to the awesome list](../../README.md)
