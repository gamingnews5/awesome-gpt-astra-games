# Mind Arena 3D

> Verified game note.

![Mind Arena 3D screenshot placeholder](mind-arena-3d-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/jbtdc24/Minds3d](https://github.com/jbtdc24/Minds3d)
- **Evidence:** [direct model evidence](https://github.com/jbtdc24/Minds3d/commit/32afffcfff36d3ab9eb99e1c48a174c9113e0c72)
- **Live demo:** [open demo](https://minds3d.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 3v3 card-battle game (Axie-style) for the 3,333 MDG (minds.games) NFTs. Every fighter is built in 3D straight from its NFT layer art, so the front view matches the NFT 1:1, with toon shading and outlines. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jbtdc24/Minds3d/blob/main/web/src/main.js](https://github.com/jbtdc24/Minds3d/blob/main/web/src/main.js)
- [https://github.com/jbtdc24/Minds3d/commit/32afffcfff36d3ab9eb99e1c48a174c9113e0c72](https://github.com/jbtdc24/Minds3d/commit/32afffcfff36d3ab9eb99e1c48a174c9113e0c72)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/jbtdc24/Minds3d

[Back to the awesome list](../../README.md)
