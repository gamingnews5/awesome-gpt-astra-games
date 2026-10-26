# Avalanche Run

> Verified game note.

![Avalanche Run screenshot placeholder](avalanche-run-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Sonnet 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/jkempy2009-lang/skigameclaude](https://github.com/jkempy2009-lang/skigameclaude)
- **Evidence:** [direct model evidence](https://github.com/jkempy2009-lang/skigameclaude/commit/2d02abb381ac60120a313f1bae471c1e522cf495)
- **Live demo:** [open demo](https://skigameclaude.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A third-person ski game (camera behind the skier, looking down the slope) in a single HTML file — no build step, no dependencies. Open index.html in a browser. Commit carries an exact Claude Sonnet 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jkempy2009-lang/skigameclaude/blob/claude/zealous-lovelace-ninb62/index.html](https://github.com/jkempy2009-lang/skigameclaude/blob/claude/zealous-lovelace-ninb62/index.html)
- [https://github.com/jkempy2009-lang/skigameclaude/commit/2d02abb381ac60120a313f1bae471c1e522cf495](https://github.com/jkempy2009-lang/skigameclaude/commit/2d02abb381ac60120a313f1bae471c1e522cf495)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T01:00Z..07:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-24T01:00Z; https://github.com/jkempy2009-lang/skigameclaude

[Back to the awesome list](../../README.md)
