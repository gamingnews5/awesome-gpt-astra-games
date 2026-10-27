# Afterburner

> Verified game note.

![Afterburner screenshot placeholder](afterburner-placeholder.svg)

## At a glance

- **Score:** 7.8/10
- **Model:** Claude Opus 5.5
- **Technology:** Roblox, Luau
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/wgw0/afterburner](https://github.com/wgw0/afterburner)
- **Evidence:** [direct model evidence](https://github.com/wgw0/afterburner/commit/c31426e1dd645cb0fe3358170d7c92b6f6617bd3)
- **Live demo:** [open demo](https://www.roblox.com/users/35203031/profile)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Afterburner is a Roblox dogfighting game inspired by DCS World. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/wgw0/afterburner/blob/master/tools/blender/f5e_generate.py](https://github.com/wgw0/afterburner/blob/master/tools/blender/f5e_generate.py)
- [https://github.com/wgw0/afterburner/commit/c31426e1dd645cb0fe3358170d7c92b6f6617bd3](https://github.com/wgw0/afterburner/commit/c31426e1dd645cb0fe3358170d7c92b6f6617bd3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/wgw0/afterburner

[Back to the awesome list](../../README.md)
