# MU Sky

> Verified game note.

![MU Sky screenshot placeholder](mu-sky-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Three.js, Browser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/u11028/mu_sky](https://github.com/u11028/mu_sky)
- **Evidence:** [direct model evidence](https://github.com/u11028/mu_sky/commit/1dc69e68efc3f7b26528aeec581ca59df6860557)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

เกม RPG ออนไลน์ 3 มิติ ตัวละครชิบิน่ารัก เล่นได้ทั้งบนเว็บและมือถือ ผจญภัยใน 6 ภาคของไทย ตีมอนสเตอร์ ล่าบอส สู้กับผู้เล่นอื่น สะสมฉายา และทำภารกิจประจำวัน. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/u11028/mu_sky/blob/master/server/src/WorldRoom.ts](https://github.com/u11028/mu_sky/blob/master/server/src/WorldRoom.ts)
- [https://github.com/u11028/mu_sky/commit/1dc69e68efc3f7b26528aeec581ca59df6860557](https://github.com/u11028/mu_sky/commit/1dc69e68efc3f7b26528aeec581ca59df6860557)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/u11028/mu_sky

[Back to the awesome list](../../README.md)
