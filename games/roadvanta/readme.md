# ROADVANTA

> Verified game note.

![ROADVANTA screenshot placeholder](roadvanta-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/osigwechibuike43-ux/ROADVANTA](https://github.com/osigwechibuike43-ux/ROADVANTA)
- **Evidence:** [direct model evidence](https://github.com/osigwechibuike43-ux/ROADVANTA/commit/879e9c649645438a3ec509c9d14bfd136d1f7554)
- **Live demo:** [open demo](https://roadvanta.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3D open-world driving game that runs entirely in the browser. React + TypeScript + Three.js (React Three Fiber) + Vite. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/osigwechibuike43-ux/ROADVANTA/blob/main/src/world/city.ts](https://github.com/osigwechibuike43-ux/ROADVANTA/blob/main/src/world/city.ts)
- [https://github.com/osigwechibuike43-ux/ROADVANTA/commit/879e9c649645438a3ec509c9d14bfd136d1f7554](https://github.com/osigwechibuike43-ux/ROADVANTA/commit/879e9c649645438a3ec509c9d14bfd136d1f7554)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/osigwechibuike43-ux/ROADVANTA

[Back to the awesome list](../../README.md)
