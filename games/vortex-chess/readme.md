# Vortex Chess

> Verified game note.

![Vortex Chess screenshot placeholder](vortex-chess-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/unse1234/vortex-chess](https://github.com/unse1234/vortex-chess)
- **Evidence:** [direct model evidence](https://github.com/unse1234/vortex-chess/commit/dd075a174e5fb9f78ee248b8ec7a22d0da18c00d)
- **Live demo:** [open demo](https://vortex-chess-phi.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

One repository for the Vortex Chess frontend, backend, and project documentation. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/unse1234/vortex-chess/blob/main/frontend/src/components/ui/icons.tsx](https://github.com/unse1234/vortex-chess/blob/main/frontend/src/components/ui/icons.tsx)
- [https://github.com/unse1234/vortex-chess/commit/dd075a174e5fb9f78ee248b8ec7a22d0da18c00d](https://github.com/unse1234/vortex-chess/commit/dd075a174e5fb9f78ee248b8ec7a22d0da18c00d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/unse1234/vortex-chess

[Back to the awesome list](../../README.md)
