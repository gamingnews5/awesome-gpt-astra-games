# Dig Up

> Verified game note.

![Dig Up screenshot](https://raw.githubusercontent.com/woydarko/digup-hemi/main/docs/screenshots/gameplay.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.0/10 ([manually reviewed image](https://github.com/woydarko/digup-hemi/blob/main/docs/screenshots/gameplay.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/woydarko/digup-hemi](https://github.com/woydarko/digup-hemi)
- **Evidence:** [direct model evidence](https://github.com/woydarko/digup-hemi/commit/6d2e73ff1c2932b443e61bf0253c4400171d7a8b)
- **Live demo:** [open demo](https://digup-hemi.digup-worker.workers.dev)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/woydarko/digup-hemi/blob/main/docs/screenshots/gameplay.png) — 📸 6.0/10 · manual visual review · Use this frame for the game-level score. Pixel cave platformer with coins, lava and enemy; readable and lively.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A 2D platformer where you dig your way up through a cave while lava rises beneath you. Break blocks, stomp. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/woydarko/digup-hemi/blob/main/Assets/TextMesh Pro/Examples & Extras/Scripts/TMP_TextInfoDebugTool.cs](https://github.com/woydarko/digup-hemi/blob/main/Assets/TextMesh Pro/Examples & Extras/Scripts/TMP_TextInfoDebugTool.cs)
- [https://github.com/woydarko/digup-hemi/commit/6d2e73ff1c2932b443e61bf0253c4400171d7a8b](https://github.com/woydarko/digup-hemi/commit/6d2e73ff1c2932b443e61bf0253c4400171d7a8b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/woydarko/digup-hemi

[Back to the awesome list](../../README.md)
