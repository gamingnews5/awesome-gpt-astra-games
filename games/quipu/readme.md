# Quipu

> Verified game note.

![Quipu screenshot placeholder](quipu-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/marinajimnz/quipugame](https://github.com/marinajimnz/quipugame)
- **Evidence:** [direct model evidence](https://github.com/marinajimnz/quipugame/commit/5f7bd4ccce279841349fb9cc4b50b8fe1213d7c5)
- **Live demo:** [open demo](https://quiputhegame.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Juego de deducción por turnos para 2–4 jugadores (PWA). Next.js + Supabase + Vercel. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/marinajimnz/quipugame/blob/main/src/types/database.ts](https://github.com/marinajimnz/quipugame/blob/main/src/types/database.ts)
- [https://github.com/marinajimnz/quipugame/commit/5f7bd4ccce279841349fb9cc4b50b8fe1213d7c5](https://github.com/marinajimnz/quipugame/commit/5f7bd4ccce279841349fb9cc4b50b8fe1213d7c5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/marinajimnz/quipugame

[Back to the awesome list](../../README.md)
