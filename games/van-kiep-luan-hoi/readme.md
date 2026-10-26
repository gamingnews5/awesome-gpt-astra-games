# Vạn Kiếp Luân Hồi

> Verified game note.

![Vạn Kiếp Luân Hồi screenshot placeholder](van-kiep-luan-hoi-placeholder.svg)

## At a glance

- **Score:** 8.0/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/katshuhama-jpg/van-kiep-luan-hoi](https://github.com/katshuhama-jpg/van-kiep-luan-hoi)
- **Evidence:** [direct model evidence](https://github.com/katshuhama-jpg/van-kiep-luan-hoi/commit/06a73e11f4baa4abe0149bc85f7a275cac49c34d)
- **Live demo:** [open demo](https://van-kiep-luan-hoi.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Game pixel trùng sinh tu tiên, chơi trên trình duyệt điện thoại. Lấy cảm hứng từ 1in8b.life: đầu thai ngẫu nhiên, thời gian tự trôi, mỗi năm chọn một trọng tâm, gặp kỳ ngộ thì chọn 1 trong 4 hướng, sống đến hết thọ nguyên rồi luân hồi. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/katshuhama-jpg/van-kiep-luan-hoi/blob/main/lib/game/events.ts](https://github.com/katshuhama-jpg/van-kiep-luan-hoi/blob/main/lib/game/events.ts)
- [https://github.com/katshuhama-jpg/van-kiep-luan-hoi/commit/06a73e11f4baa4abe0149bc85f7a275cac49c34d](https://github.com/katshuhama-jpg/van-kiep-luan-hoi/commit/06a73e11f4baa4abe0149bc85f7a275cac49c34d)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/katshuhama-jpg/van-kiep-luan-hoi

[Back to the awesome list](../../README.md)
