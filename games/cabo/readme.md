# Cabo

> Verified game note.

![Cabo screenshot placeholder](cabo-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Python, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/kizmiz/cabo-rl](https://github.com/kizmiz/cabo-rl)
- **Evidence:** [direct model evidence](https://github.com/kizmiz/cabo-rl/commit/45be6323fa4190fc22f6c5c36ef1af2ee28958c3)
- **Live demo:** [open demo](https://pypi.org/project/cabo-rl/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Play Cabo with friends and a self-play RL agent in the browser; benchmark LLMs against it. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kizmiz/cabo-rl/blob/main/cabo/web/static/app.js](https://github.com/kizmiz/cabo-rl/blob/main/cabo/web/static/app.js)
- [https://github.com/kizmiz/cabo-rl/commit/45be6323fa4190fc22f6c5c36ef1af2ee28958c3](https://github.com/kizmiz/cabo-rl/commit/45be6323fa4190fc22f6c5c36ef1af2ee28958c3)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/kizmiz/cabo-rl

[Back to the awesome list](../../README.md)
