# Midnight Paws

> Verified game note.

![Midnight Paws screenshot](https://raw.githubusercontent.com/vmttri-glitch/midnightpaws/main/docs/intro-cutscene/references/boss_athlete_cat.png)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/vmttri-glitch/midnightpaws/blob/main/docs/intro-cutscene/references/boss_athlete_cat.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/vmttri-glitch/midnightpaws](https://github.com/vmttri-glitch/midnightpaws)
- **Evidence:** [direct model evidence](https://github.com/vmttri-glitch/midnightpaws/commit/af50264e9a3e9306bd5d09fcaa08f391a4f1df55)
- **Live demo:** [open demo](https://vmttri-glitch.github.io/midnightpaws/)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/vmttri-glitch/midnightpaws/blob/main/docs/intro-cutscene/references/boss_athlete_cat.png) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. Cute yellow cat with headband 3D render on grey; charming character.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An endless runner about a stray cat sprinting through the city at midnight. Dodge traffic, leap between rooftops and outrun three bosses, then spend the fish you collect on new cats, rooms and gear. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/vmttri-glitch/midnightpaws/blob/main/src/components/GameCanvas.tsx](https://github.com/vmttri-glitch/midnightpaws/blob/main/src/components/GameCanvas.tsx)
- [https://github.com/vmttri-glitch/midnightpaws/commit/af50264e9a3e9306bd5d09fcaa08f391a4f1df55](https://github.com/vmttri-glitch/midnightpaws/commit/af50264e9a3e9306bd5d09fcaa08f391a4f1df55)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/vmttri-glitch/midnightpaws

[Back to the awesome list](../../README.md)
