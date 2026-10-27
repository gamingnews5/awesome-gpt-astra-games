# Игры для Telegram

> Verified game note.

![Игры для Telegram screenshot placeholder](telegram-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/abaykopenov/tower-defense](https://github.com/abaykopenov/tower-defense)
- **Evidence:** [direct model evidence](https://github.com/abaykopenov/tower-defense/commit/4abedc0188ea464fe3e27d0da063b6c34efb5e04)
- **Live demo:** [open demo](https://abaykopenov.github.io/tower-defense/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Tower defense for phones — works as a website and as a Telegram Mini App. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/abaykopenov/tower-defense/blob/main/games/tower-defense/src/game.js](https://github.com/abaykopenov/tower-defense/blob/main/games/tower-defense/src/game.js)
- [https://github.com/abaykopenov/tower-defense/commit/4abedc0188ea464fe3e27d0da063b6c34efb5e04](https://github.com/abaykopenov/tower-defense/commit/4abedc0188ea464fe3e27d0da063b6c34efb5e04)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/abaykopenov/tower-defense

[Back to the awesome list](../../README.md)
