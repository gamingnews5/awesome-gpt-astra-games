# Dolmuş

> Verified game note.

![Dolmuş screenshot](https://raw.githubusercontent.com/Furkiozknn/dolmus/main/docs/gameplay.gif)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/Furkiozknn/dolmus/blob/main/docs/gameplay.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Furkiozknn/dolmus](https://github.com/Furkiozknn/dolmus)
- **Evidence:** [direct model evidence](https://github.com/Furkiozknn/dolmus/commit/a0c2e454c42b65f2f7d4bd6cefbb6853f1229d59)
- **Live demo:** [open demo](https://furkiozknn.github.io/dolmus/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Furkiozknn/dolmus/blob/main/docs/gameplay.gif) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Yellow minibus in a 3D city street with minimap and HUD; clear driving scene.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

3D minibus driving game in an Istanbul-style city: pick up passengers, obey lights, earn fares. Browser game built by Claude Sonnet 5.5 · İstanbul'da dolmuş şoförlüğü: yolcu al, ışıklara uy, kazan. Claude Sonnet 5.5 yaptı. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Furkiozknn/dolmus/blob/main/index.html](https://github.com/Furkiozknn/dolmus/blob/main/index.html)
- [https://github.com/Furkiozknn/dolmus/commit/a0c2e454c42b65f2f7d4bd6cefbb6853f1229d59](https://github.com/Furkiozknn/dolmus/commit/a0c2e454c42b65f2f7d4bd6cefbb6853f1229d59)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Furkiozknn/dolmus

[Back to the awesome list](../../README.md)
