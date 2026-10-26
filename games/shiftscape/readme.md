# Shiftscape

> Verified game note.

![Shiftscape screenshot](https://raw.githubusercontent.com/jaking-studios/shiftscape/main/docs/media/shiftscape-preview.gif)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/jaking-studios/shiftscape/blob/main/docs/media/shiftscape-preview.gif)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Sonnet 5.5, Claude Fable 5.1
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/jaking-studios/shiftscape](https://github.com/jaking-studios/shiftscape)
- **Evidence:** [direct model evidence](https://github.com/jaking-studios/shiftscape/commit/271a9bbf596af2fa68435417d7b5f68c1128b1b0)
- **Live demo:** [open demo](https://jaking-studios.github.io/shiftscape/play/)
- **Additional live link:** [open demo](https://jaking-studios.github.io/shiftscape/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/jaking-studios/shiftscape/blob/main/docs/media/shiftscape-preview.gif) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Low-poly checkpoint platform with hero and HUD; simple 3D.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Shiftscape is an original 3D escape game built in Unity 6 (6000.3) for browser (WebGL), Android and PC (iOS exports too). Every run is a procedurally generated chain of rooms you have to get through before the Void — a creeping wall of nothing — catches you. Commit carries an exact Claude Sonnet 5.5 / Claude Fable 5.1 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jaking-studios/shiftscape/blob/main/Assets/Shiftscape/Scripts/World/LevelBuilder.cs](https://github.com/jaking-studios/shiftscape/blob/main/Assets/Shiftscape/Scripts/World/LevelBuilder.cs)
- [https://github.com/jaking-studios/shiftscape/commit/271a9bbf596af2fa68435417d7b5f68c1128b1b0](https://github.com/jaking-studios/shiftscape/commit/271a9bbf596af2fa68435417d7b5f68c1128b1b0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/jaking-studios/shiftscape

[Back to the awesome list](../../README.md)
