# Bouncy Buddies（バウンシー・バディーズ）

> Verified game note.

![Bouncy Buddies（バウンシー・バディーズ） screenshot placeholder](bouncy-buddies-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/kdt26aie40002-ops/my-game](https://github.com/kdt26aie40002-ops/my-game)
- **Evidence:** [direct model evidence](https://github.com/kdt26aie40002-ops/my-game/commit/ccea6a0a7424b3ff9bab59c8952dc0d717ad244b)
- **Live demo:** [open demo](https://kdt26aie40002-ops.github.io/my-game/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

ブラウザで遊べる3D物理アクションゲームです。ころころしたキャラクターを操作して、空に浮かぶアスレチックコースのゴールを目指します。1人プレイと、同じキーボードでの2人協力プレイに対応しています。. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kdt26aie40002-ops/my-game/blob/main/src/level.js](https://github.com/kdt26aie40002-ops/my-game/blob/main/src/level.js)
- [https://github.com/kdt26aie40002-ops/my-game/commit/ccea6a0a7424b3ff9bab59c8952dc0d717ad244b](https://github.com/kdt26aie40002-ops/my-game/commit/ccea6a0a7424b3ff9bab59c8952dc0d717ad244b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/kdt26aie40002-ops/my-game

[Back to the awesome list](../../README.md)
