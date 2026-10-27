# Shout

> Verified game note.

![Shout screenshot placeholder](shout-placeholder.svg)

## At a glance

- **Score:** 7.5/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/jonahallibone/clue-ladder](https://github.com/jonahallibone/clue-ladder)
- **Evidence:** [direct model evidence](https://github.com/jonahallibone/clue-ladder/commit/742bf390d18a6b4c7b92fce7b3ac7a2d8a532376)
- **Live demo:** [open demo](https://clue-ladder-nine.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A daily pub-trivia deduction game. Each answer comes with six clues that go from vague to obvious. Your pint starts full, every clue is a sip, and every wrong guess is your shout (a big gulp). Whatever's left in the pint when you name the answer is your score. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/jonahallibone/clue-ladder/blob/main/legacy/index.html](https://github.com/jonahallibone/clue-ladder/blob/main/legacy/index.html)
- [https://github.com/jonahallibone/clue-ladder/commit/742bf390d18a6b4c7b92fce7b3ac7a2d8a532376](https://github.com/jonahallibone/clue-ladder/commit/742bf390d18a6b4c7b92fce7b3ac7a2d8a532376)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/jonahallibone/clue-ladder

[Back to the awesome list](../../README.md)
