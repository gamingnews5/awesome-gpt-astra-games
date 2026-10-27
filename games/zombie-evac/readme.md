# Zombie Evac

> Verified game note.

![Zombie Evac screenshot placeholder](zombie-evac-placeholder.svg)

## At a glance

- **Score:** 7.7/10
- **Model:** Claude Opus 5.5
- **Technology:** Python, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/SimpleCleanSpleen/Zombie-Evac](https://github.com/SimpleCleanSpleen/Zombie-Evac)
- **Evidence:** [direct model evidence](https://github.com/SimpleCleanSpleen/Zombie-Evac/commit/6b79cd988daa92ba7180933eee3440568154a4b2)
- **Live demo:** [open demo](https://simplecleanspleen.github.io/Zombie-Evac/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Zombie outbreak evacuation RTS on real-world city maps - play in the browser. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/SimpleCleanSpleen/Zombie-Evac/blob/main/zombie_evac.py](https://github.com/SimpleCleanSpleen/Zombie-Evac/blob/main/zombie_evac.py)
- [https://github.com/SimpleCleanSpleen/Zombie-Evac/commit/6b79cd988daa92ba7180933eee3440568154a4b2](https://github.com/SimpleCleanSpleen/Zombie-Evac/commit/6b79cd988daa92ba7180933eee3440568154a4b2)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/SimpleCleanSpleen/Zombie-Evac

[Back to the awesome list](../../README.md)
