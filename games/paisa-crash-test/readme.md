# Paisa Crash Test

> Verified game note.

![Paisa Crash Test screenshot placeholder](paisa-crash-test-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/WinningCloud/PaisaCrash](https://github.com/WinningCloud/PaisaCrash)
- **Evidence:** [direct model evidence](https://github.com/WinningCloud/PaisaCrash/commit/804ccbc1192fad91f255069d3ce67f747fc4773c)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A retro pixel-art game where you live five years of an Indian adult's financial life, from age 22 to 27. Every year random events hit (layoffs, hospital bills, UPI scams, weddings, bonuses), your choices cause later events, and a voice mascot called Paisa Pal… Commit carries an exact Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/WinningCloud/PaisaCrash/blob/main/client/src/game/deck/life.js](https://github.com/WinningCloud/PaisaCrash/blob/main/client/src/game/deck/life.js)
- [https://github.com/WinningCloud/PaisaCrash/commit/804ccbc1192fad91f255069d3ce67f747fc4773c](https://github.com/WinningCloud/PaisaCrash/commit/804ccbc1192fad91f255069d3ce67f747fc4773c)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/WinningCloud/PaisaCrash

[Back to the awesome list](../../README.md)
