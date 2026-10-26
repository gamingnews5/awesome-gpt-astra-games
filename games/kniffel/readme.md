# Kniffel

> Verified game note.

![Kniffel screenshot placeholder](kniffel-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Ranger-Jones/kniffel](https://github.com/Ranger-Jones/kniffel)
- **Evidence:** [direct model evidence](https://github.com/Ranger-Jones/kniffel/commit/8f39923463c40f5da7107bbdc948183d4b4572fa)
- **Live demo:** [open demo](https://kniffel-sigma.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Online-Kniffel für Freunde: Accounts, Live-Räume für 1–6 Spieler, Freundesliste mit Online-Status, Einladungen, Emoji-Reaktionen, Revanche, Statistiken, Spielverlauf und Bestenliste. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Ranger-Jones/kniffel/blob/main/src/lib/supabase/database.types.ts](https://github.com/Ranger-Jones/kniffel/blob/main/src/lib/supabase/database.types.ts)
- [https://github.com/Ranger-Jones/kniffel/commit/8f39923463c40f5da7107bbdc948183d4b4572fa](https://github.com/Ranger-Jones/kniffel/commit/8f39923463c40f5da7107bbdc948183d4b4572fa)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Ranger-Jones/kniffel

[Back to the awesome list](../../README.md)
