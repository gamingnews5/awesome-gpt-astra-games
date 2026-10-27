# Glimmerfall

> Verified game note.

![Glimmerfall screenshot](https://raw.githubusercontent.com/ArtemChikolaev/Glimmerfall/main/docs/spikes/img/g2-6-gray.png)

## At a glance

- **Score:** 7.5/10
- **Screenshot rating:** 4.0/10 ([manually reviewed image](https://github.com/ArtemChikolaev/Glimmerfall/blob/main/docs/spikes/img/g2-6-gray.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/ArtemChikolaev/Glimmerfall](https://github.com/ArtemChikolaev/Glimmerfall)
- **Evidence:** [direct model evidence](https://github.com/ArtemChikolaev/Glimmerfall/commit/2241ea456f06ac9dfae3370669f402404096bf28)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/ArtemChikolaev/Glimmerfall/blob/main/docs/spikes/img/g2-6-gray.png) — 📸 4.0/10 · manual visual review · Use this frame for the game-level score. Debug-like particle splatter panels; hard to read.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Изометрический пиксельный экшн-рогалик: отряд из трёх фонарщиков несёт свет через мир, который поглощает Тьма. Драфт героев с «сыгранностью», переключение посреди орды, огонь и молнии покровителей, дейлики с призраками друзей. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/ArtemChikolaev/Glimmerfall/blob/main/tools/sprites/blender/models.py](https://github.com/ArtemChikolaev/Glimmerfall/blob/main/tools/sprites/blender/models.py)
- [https://github.com/ArtemChikolaev/Glimmerfall/commit/2241ea456f06ac9dfae3370669f402404096bf28](https://github.com/ArtemChikolaev/Glimmerfall/commit/2241ea456f06ac9dfae3370669f402404096bf28)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/ArtemChikolaev/Glimmerfall

[Back to the awesome list](../../README.md)
