# Inkling

> Verified game note.

![Inkling screenshot placeholder](inkling-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/sakshammalge/MyScribbleClone](https://github.com/sakshammalge/MyScribbleClone)
- **Evidence:** [direct model evidence](https://github.com/sakshammalge/MyScribbleClone/commit/5e75cbe6265a6d6938e5fb16fc4cae2a35dbe050)
- **Live demo:** [open demo](https://inkling-5wrz.onrender.com)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A multiplayer draw-and-guess game for private rooms. Same classic game idea, its own look and feel. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/sakshammalge/MyScribbleClone/blob/main/server/src/wordlist.ts](https://github.com/sakshammalge/MyScribbleClone/blob/main/server/src/wordlist.ts)
- [https://github.com/sakshammalge/MyScribbleClone/commit/5e75cbe6265a6d6938e5fb16fc4cae2a35dbe050](https://github.com/sakshammalge/MyScribbleClone/commit/5e75cbe6265a6d6938e5fb16fc4cae2a35dbe050)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/sakshammalge/MyScribbleClone

[Back to the awesome list](../../README.md)
