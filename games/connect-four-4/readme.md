# Connect Four (4 в ряд)

> Verified game note.

![Connect Four (4 в ряд) screenshot](https://raw.githubusercontent.com/olshanskiyad/telegram-connect-four/main/screenshots/room.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 5.4/10 ([manually reviewed image](https://github.com/olshanskiyad/telegram-connect-four/blob/main/screenshots/room.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/olshanskiyad/telegram-connect-four](https://github.com/olshanskiyad/telegram-connect-four)
- **Evidence:** [direct model evidence](https://github.com/olshanskiyad/telegram-connect-four/commit/19353c7e63071b1237bb0b0b866bfd7fb061a6d0)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/olshanskiyad/telegram-connect-four/blob/main/screenshots/room.png) — 📸 5.4/10 · manual visual review · Use this frame for the game-level score. Connect-four board mid-game with coloured discs; clear but plain dark UI.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Connect Four as a Telegram Mini App and web game: play a friend by link, a random opponent or a bot; guest mode works without Telegram. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/olshanskiyad/telegram-connect-four/blob/main/src/components/room-client.tsx](https://github.com/olshanskiyad/telegram-connect-four/blob/main/src/components/room-client.tsx)
- [https://github.com/olshanskiyad/telegram-connect-four/commit/19353c7e63071b1237bb0b0b866bfd7fb061a6d0](https://github.com/olshanskiyad/telegram-connect-four/commit/19353c7e63071b1237bb0b0b866bfd7fb061a6d0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/olshanskiyad/telegram-connect-four

[Back to the awesome list](../../README.md)
