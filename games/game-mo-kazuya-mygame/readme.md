# レトロゲーム集

> Verified game note.

![レトロゲーム集 screenshot placeholder](game-mo-kazuya-mygame-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/mo-kazuya/MyGame](https://github.com/mo-kazuya/MyGame)
- **Evidence:** [direct model evidence](https://github.com/mo-kazuya/MyGame/commit/7e101254bd5f36e8f6fd93c21781d14c8cae05f7)
- **Live demo:** [open demo](https://mo-kazuya.github.io/MyGame/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

ブラウザですぐ遊べる、レトロゲーム風の小さなゲームを集めたリポジトリです。どのゲームも HTML5 Canvas と素の JavaScript だけで動きます（ビルド不要）。パソコンでもスマホでも遊べます。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/mo-kazuya/MyGame/blob/master/underground-dragon/js/game.js](https://github.com/mo-kazuya/MyGame/blob/master/underground-dragon/js/game.js)
- [https://github.com/mo-kazuya/MyGame/commit/7e101254bd5f36e8f6fd93c21781d14c8cae05f7](https://github.com/mo-kazuya/MyGame/commit/7e101254bd5f36e8f6fd93c21781d14c8cae05f7)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/mo-kazuya/MyGame

[Back to the awesome list](../../README.md)
