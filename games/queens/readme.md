# Queens

> Verified game note.

![Queens screenshot placeholder](queens-placeholder.svg)

## At a glance

- **Score:** 7.1/10
- **Model:** Claude Opus 5.5
- **Technology:** Swift, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/berwickgeek/queens](https://github.com/berwickgeek/queens)
- **Evidence:** [direct model evidence](https://github.com/berwickgeek/queens/commit/fea004ebd44a9d564f226c9a923962779f581564)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Offline Queens puzzle game for iPhone, in SwiftUI, with hints that teach the deduction. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/berwickgeek/queens/blob/main/app/Queens/Board/BoardView.swift](https://github.com/berwickgeek/queens/blob/main/app/Queens/Board/BoardView.swift)
- [https://github.com/berwickgeek/queens/commit/fea004ebd44a9d564f226c9a923962779f581564](https://github.com/berwickgeek/queens/commit/fea004ebd44a9d564f226c9a923962779f581564)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/berwickgeek/queens

[Back to the awesome list](../../README.md)
