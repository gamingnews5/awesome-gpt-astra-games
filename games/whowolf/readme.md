# Whowolf

> Verified game note.

![Whowolf screenshot](https://raw.githubusercontent.com/nurkert/whowolf/main/.github/assets/game-box.jpg)

## At a glance

- **Score:** 7.7/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/nurkert/whowolf/blob/main/.github/assets/game-box.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Flutter, Dart
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/nurkert/whowolf](https://github.com/nurkert/whowolf)
- **Evidence:** [direct model evidence](https://github.com/nurkert/whowolf/commit/81164f850fae24f8bdf68a35343a29f1002e054f)
- **Live demo:** [open demo](https://whowolf.de)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/nurkert/whowolf/blob/main/.github/assets/game-box.jpg) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Illustrated Whowolf landing with wolf and cards; polished cartoon art.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Werewolf at the table. Everyone on their own phone. The app is the narrator. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nurkert/whowolf/blob/main/app/lib/l10n/app_localizations.dart](https://github.com/nurkert/whowolf/blob/main/app/lib/l10n/app_localizations.dart)
- [https://github.com/nurkert/whowolf/commit/81164f850fae24f8bdf68a35343a29f1002e054f](https://github.com/nurkert/whowolf/commit/81164f850fae24f8bdf68a35343a29f1002e054f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/nurkert/whowolf

[Back to the awesome list](../../README.md)
