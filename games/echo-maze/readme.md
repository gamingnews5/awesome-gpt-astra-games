# Echo Maze

> Verified game note.

![Echo Maze screenshot](https://raw.githubusercontent.com/ThanhBC1234/echo-maze/main/docs/screenshots/memorize.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.2/10 ([manually reviewed image](https://github.com/ThanhBC1234/echo-maze/blob/main/docs/screenshots/memorize.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Fable 5.1
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/ThanhBC1234/echo-maze](https://github.com/ThanhBC1234/echo-maze)
- **Evidence:** [direct model evidence](https://github.com/ThanhBC1234/echo-maze/commit/2652b647a61bc16521e33bdacac34d7a1809429e)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ThanhBC1234/echo-maze/blob/main/docs/screenshots/memorize.png) — 📸 5.2/10 · manual visual review · Use this frame for the game-level score. Dark maze grid with colored memory dots and control panel; clear but utilitarian.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Game mê cung chơi mù bằng tai nghe: nhìn bản đồ vài giây, tắt đèn, rồi tìm đường bằng trí nhớ và âm thanh 3D (trái/phải, trước/sau). Chạy thẳng trên trình duyệt, không cần cài đặt, không cần build. Commit carries an exact Claude Fable 5.1 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ThanhBC1234/echo-maze/blob/main/js/main.js](https://github.com/ThanhBC1234/echo-maze/blob/main/js/main.js)
- [https://github.com/ThanhBC1234/echo-maze/commit/2652b647a61bc16521e33bdacac34d7a1809429e](https://github.com/ThanhBC1234/echo-maze/commit/2652b647a61bc16521e33bdacac34d7a1809429e)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/ThanhBC1234/echo-maze

[Back to the awesome list](../../README.md)
