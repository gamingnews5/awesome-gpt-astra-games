# 虛擬跑跑樂 Virtual Runners

> Verified game note.

![虛擬跑跑樂 Virtual Runners screenshot placeholder](virtual-runners-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/YuutaTsubasa/VirtualRunners](https://github.com/YuutaTsubasa/VirtualRunners)
- **Evidence:** [direct model evidence](https://github.com/YuutaTsubasa/VirtualRunners/commit/7f30b144115bdbac7bb8b4648b157eec71a5ccce)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

虛擬跑跑樂 Virtual Runners — Sonic Runners／跑跑薑餅人風格的跑酷遊戲：六大關 48 小關（含魔王關）、越跑越快的無盡模式、最多 8 人連線競速（別人在遠景裡跑），角色是虛擬台麻館的大家，各有小能力。Tauri v2 + Svelte 5 + Rust/WebAssembly. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/YuutaTsubasa/VirtualRunners/blob/main/src/lib/game/render.js](https://github.com/YuutaTsubasa/VirtualRunners/blob/main/src/lib/game/render.js)
- [https://github.com/YuutaTsubasa/VirtualRunners/commit/7f30b144115bdbac7bb8b4648b157eec71a5ccce](https://github.com/YuutaTsubasa/VirtualRunners/commit/7f30b144115bdbac7bb8b4648b157eec71a5ccce)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/YuutaTsubasa/VirtualRunners

[Back to the awesome list](../../README.md)
