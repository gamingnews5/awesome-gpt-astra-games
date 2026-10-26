# Storybound

> Verified game note.

![Storybound screenshot](https://raw.githubusercontent.com/trungle42/Storybound/main/docs/images/avatars-before-after.jpg)

## At a glance

- **Score:** 7.6/10
- **Screenshot rating:** 6.2/10 ([manually reviewed image](https://github.com/trungle42/Storybound/blob/main/docs/images/avatars-before-after.jpg)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/trungle42/Storybound](https://github.com/trungle42/Storybound)
- **Evidence:** [direct model evidence](https://github.com/trungle42/Storybound/commit/0965884192a521fa10d5e2668b9896c07a6299dc)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/trungle42/Storybound/blob/main/docs/images/avatars-before-after.jpg) — 📸 6.2/10 · manual visual review · Use this frame for the game-level score. Third-person forest scene with characters and three dialogue portraits; decent 3D, cluttered layout.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Storybound is a third-person 3D fairy-tale adventure in the browser, built for HackTX 2026 (theme: Fairy Tale). A Gemini-powered storyteller writes the tale from what you do, and your real world plays along: your phone is the controller, a stick with a… Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/trungle42/Storybound/blob/main/frontend/src/adventure/Adventure.ts](https://github.com/trungle42/Storybound/blob/main/frontend/src/adventure/Adventure.ts)
- [https://github.com/trungle42/Storybound/commit/0965884192a521fa10d5e2668b9896c07a6299dc](https://github.com/trungle42/Storybound/commit/0965884192a521fa10d5e2668b9896c07a6299dc)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/trungle42/Storybound

[Back to the awesome list](../../README.md)
