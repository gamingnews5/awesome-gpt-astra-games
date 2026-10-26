# Loop Rebirth

> Verified game note.

![Loop Rebirth screenshot](https://raw.githubusercontent.com/johnnysins24/looprebirth/main/docs/art/mockup_grass.png)

## At a glance

- **Score:** 7.1/10
- **Screenshot rating:** 5.8/10 ([manually reviewed image](https://github.com/johnnysins24/looprebirth/blob/main/docs/art/mockup_grass.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/johnnysins24/looprebirth](https://github.com/johnnysins24/looprebirth)
- **Evidence:** [direct model evidence](https://github.com/johnnysins24/looprebirth/commit/4ccbfac083dda102e18448e393e6bb08b5d1b072)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/johnnysins24/looprebirth/blob/main/docs/art/mockup_grass.png) — 📸 5.8/10 · manual visual review · Use this frame for the game-level score. Pixel loop path on green island with cards and stats; dense but coherent.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

roguelite แนว Loop Hero ที่ขยาย gameplay: loop เปลี่ยนทุก run, การ์ด tile และ skill card ที่ merge ได้,. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/johnnysins24/looprebirth/blob/main/tools/art/mockup.py](https://github.com/johnnysins24/looprebirth/blob/main/tools/art/mockup.py)
- [https://github.com/johnnysins24/looprebirth/commit/4ccbfac083dda102e18448e393e6bb08b5d1b072](https://github.com/johnnysins24/looprebirth/commit/4ccbfac083dda102e18448e393e6bb08b5d1b072)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/johnnysins24/looprebirth

[Back to the awesome list](../../README.md)
