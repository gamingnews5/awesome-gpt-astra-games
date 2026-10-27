# Draft Duel

> Verified game note.

![Draft Duel screenshot](https://raw.githubusercontent.com/khalid413/Draft/main/docs/screenshots/card-library.jpg)

## At a glance

- **Score:** 7.3/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/khalid413/Draft/blob/main/docs/screenshots/card-library.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** PHP, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/khalid413/Draft](https://github.com/khalid413/Draft)
- **Evidence:** [direct model evidence](https://github.com/khalid413/Draft/commit/69bbd1357ff8d52b7c60434304c98af47b1e6569)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/khalid413/Draft/blob/main/docs/screenshots/card-library.jpg) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Dark card-builder form; plain app UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Private online rooms and the protected admin area are implemented. See ONLINE.md for admin account creation, Reverb startup, room behavior, and deployment requirements. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/khalid413/Draft/blob/main/resources/views/welcome.blade.php](https://github.com/khalid413/Draft/blob/main/resources/views/welcome.blade.php)
- [https://github.com/khalid413/Draft/commit/69bbd1357ff8d52b7c60434304c98af47b1e6569](https://github.com/khalid413/Draft/commit/69bbd1357ff8d52b7c60434304c98af47b1e6569)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/khalid413/Draft

[Back to the awesome list](../../README.md)
