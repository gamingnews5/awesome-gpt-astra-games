# Meld

> Verified game note.

![Meld screenshot](https://raw.githubusercontent.com/andreasmwenzel/meld-with-friends/main/docs/screens/trick-1280.png)

## At a glance

- **Score:** 7.8/10
- **Screenshot rating:** 4.8/10 ([manually reviewed image](https://github.com/andreasmwenzel/meld-with-friends/blob/main/docs/screens/trick-1280.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Fable 5.1, GPT-6.1 Sol
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/andreasmwenzel/meld-with-friends](https://github.com/andreasmwenzel/meld-with-friends)
- **Evidence:** [direct model evidence](https://github.com/andreasmwenzel/meld-with-friends/commit/5531f3177209857346a2d21e5b0b5e08fd1fd3d8)
- **Live demo:** [open demo](https://meld.insulatorgap.com)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/andreasmwenzel/meld-with-friends/blob/main/docs/screens/trick-1280.png) — 📸 4.8/10 · manual visual review · Use this frame for the game-level score. Pinochle table on maroon felt with cards; clean but plain.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Pinochle with your friends, live or a trick a day. Next.js + Supabase. Commit carries an exact Claude Opus 5.5 / Claude Fable 5.1 / GPT-6.1 Sol co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/andreasmwenzel/meld-with-friends/blob/main/src/components/table/Game.tsx](https://github.com/andreasmwenzel/meld-with-friends/blob/main/src/components/table/Game.tsx)
- [https://github.com/andreasmwenzel/meld-with-friends/commit/5531f3177209857346a2d21e5b0b5e08fd1fd3d8](https://github.com/andreasmwenzel/meld-with-friends/commit/5531f3177209857346a2d21e5b0b5e08fd1fd3d8)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/andreasmwenzel/meld-with-friends

[Back to the awesome list](../../README.md)
