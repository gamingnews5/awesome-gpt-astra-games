# 1930s Racing Manager

> Verified game note.

![1930s Racing Manager screenshot](https://raw.githubusercontent.com/comeonfloyd/1930s-racing/main/docs/screenshots/calendar.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 4.4/10 ([manually reviewed image](https://github.com/comeonfloyd/1930s-racing/blob/main/docs/screenshots/calendar.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/comeonfloyd/1930s-racing](https://github.com/comeonfloyd/1930s-racing)
- **Evidence:** [direct model evidence](https://github.com/comeonfloyd/1930s-racing/commit/48d56cf228e3219aaf165bde4b2cf870f486a501)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/comeonfloyd/1930s-racing/blob/main/docs/screenshots/calendar.png) — 📸 4.4/10 · manual visual review · Use this frame for the game-level score. Dense racing-manager calendar table; readable but text-only UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A desktop management game set in 1930s Grand Prix and Indianapolis racing. You take over a real team (with lightly renamed brands, such as Alfa Rossa and Bugetti), develop its cars and drivers, and choose which races on a map of Europe and the USA are worth… Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/comeonfloyd/1930s-racing/blob/main/game/scripts/CalendarScreen.cs](https://github.com/comeonfloyd/1930s-racing/blob/main/game/scripts/CalendarScreen.cs)
- [https://github.com/comeonfloyd/1930s-racing/commit/48d56cf228e3219aaf165bde4b2cf870f486a501](https://github.com/comeonfloyd/1930s-racing/commit/48d56cf228e3219aaf165bde4b2cf870f486a501)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/comeonfloyd/1930s-racing

[Back to the awesome list](../../README.md)
