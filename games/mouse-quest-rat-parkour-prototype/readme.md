# Mouse Quest: rat parkour prototype

> Verified game note.

![Mouse Quest: rat parkour prototype screenshot](https://raw.githubusercontent.com/mykkro/mouse-quest/main/docs/images/game.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 4.6/10 ([manually reviewed image](https://github.com/mykkro/mouse-quest/blob/main/docs/images/game.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/mykkro/mouse-quest](https://github.com/mykkro/mouse-quest)
- **Evidence:** [direct model evidence](https://github.com/mykkro/mouse-quest/commit/b1d61de242d15d9c29a0f64e5344430e62b79450)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/mykkro/mouse-quest/blob/main/docs/images/game.png) — 📸 4.6/10 · manual visual review · Use this frame for the game-level score. Dark 3D beams with a small rat and debug text; prototype look.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Guide a rigged, animated rat along narrow beams, across gaps and up stairs to the. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mykkro/mouse-quest/blob/main/models/rat/pipeline/clips.py](https://github.com/mykkro/mouse-quest/blob/main/models/rat/pipeline/clips.py)
- [https://github.com/mykkro/mouse-quest/commit/b1d61de242d15d9c29a0f64e5344430e62b79450](https://github.com/mykkro/mouse-quest/commit/b1d61de242d15d9c29a0f64e5344430e62b79450)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/mykkro/mouse-quest

[Back to the awesome list](../../README.md)
