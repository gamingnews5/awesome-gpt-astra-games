# PM Brawler

> Verified game note.

![PM Brawler screenshot placeholder](pm-brawler-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Unity, C#
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/miroslavkrupa/pm-brawler](https://github.com/miroslavkrupa/pm-brawler)
- **Evidence:** [direct model evidence](https://github.com/miroslavkrupa/pm-brawler/commit/d992545d71274d56cbdd2d583a628988f3374d58)
- **Live demo:** [open demo](https://miroslavkrupa.github.io/pm-brawler/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Funny 2D beat 'em up platformer in Unity: a project manager vs. developers, testers, stakeholders, the steering committee and the C-suite. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/miroslavkrupa/pm-brawler/blob/main/Tools/ArtGenHD/environment_hd.py](https://github.com/miroslavkrupa/pm-brawler/blob/main/Tools/ArtGenHD/environment_hd.py)
- [https://github.com/miroslavkrupa/pm-brawler/commit/d992545d71274d56cbdd2d583a628988f3374d58](https://github.com/miroslavkrupa/pm-brawler/commit/d992545d71274d56cbdd2d583a628988f3374d58)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/miroslavkrupa/pm-brawler

[Back to the awesome list](../../README.md)
