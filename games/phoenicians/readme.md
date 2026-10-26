# Phoenicians

> Verified game note.

![Phoenicians screenshot placeholder](phoenicians-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/BoardAtHome/phoenicians](https://github.com/BoardAtHome/phoenicians)
- **Evidence:** [direct model evidence](https://github.com/BoardAtHome/phoenicians/commit/7c6ca6061c0b619fe72e67ed96dda7a9fa699551)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Online prototype of the board game Phoenicians, built for remote playtesting with family and friends. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/BoardAtHome/phoenicians/blob/main/packages/client/src/table/Curses.tsx](https://github.com/BoardAtHome/phoenicians/blob/main/packages/client/src/table/Curses.tsx)
- [https://github.com/BoardAtHome/phoenicians/commit/7c6ca6061c0b619fe72e67ed96dda7a9fa699551](https://github.com/BoardAtHome/phoenicians/commit/7c6ca6061c0b619fe72e67ed96dda7a9fa699551)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/BoardAtHome/phoenicians

[Back to the awesome list](../../README.md)
