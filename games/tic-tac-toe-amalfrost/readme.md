# Tic Tac Toe (amalfrost)

> Verified game note.

![Tic Tac Toe (amalfrost) screenshot](https://github.com/user-attachments/assets/db966b88-cd13-42bc-a95e-878971917dcd)

## At a glance

- **Score:** 6.8/10
- **Screenshot rating:** 5.6/10 ([manually reviewed image](https://github.com/user-attachments/assets/db966b88-cd13-42bc-a95e-878971917dcd)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/amalfrost/Abb-Assesment](https://github.com/amalfrost/Abb-Assesment)
- **Evidence:** [direct model evidence](https://github.com/amalfrost/Abb-Assesment/commit/d0ad881eb86f7491e9da10d55868dd3dd118b237)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot source 1](https://github.com/user-attachments/assets/db966b88-cd13-42bc-a95e-878971917dcd) — 📸 5.6/10 · manual visual review · Use this frame for the game-level score. Bright tic-tac-toe landing page with a winning board illustration; clean and friendly.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A browser-based Tic Tac Toe game with a React + TypeScript frontend and a Node.js REST API. The backend owns all game state: board, turns, move history, undo, game status, scoreboard and the computer opponent. The frontend renders whatever the API returns. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/amalfrost/Abb-Assesment/blob/main/frontend/src/components/Landing.tsx](https://github.com/amalfrost/Abb-Assesment/blob/main/frontend/src/components/Landing.tsx)
- [https://github.com/amalfrost/Abb-Assesment/commit/d0ad881eb86f7491e9da10d55868dd3dd118b237](https://github.com/amalfrost/Abb-Assesment/commit/d0ad881eb86f7491e9da10d55868dd3dd118b237)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-23T01:00Z..2026-10-24T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-22T01:00Z; carried over from the 2026-10-24 pending list; https://github.com/amalfrost/Abb-Assesment

[Back to the awesome list](../../README.md)
