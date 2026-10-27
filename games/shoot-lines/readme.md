# Shoot Lines

> Verified game note.

![Shoot Lines screenshot placeholder](shoot-lines-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** JavaScript, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/matheuscrafiting-netizen/Shoot-lines](https://github.com/matheuscrafiting-netizen/Shoot-lines)
- **Evidence:** [direct model evidence](https://github.com/matheuscrafiting-netizen/Shoot-lines/commit/4ebf67e0a4e493188b2a0306b09427e0bab642a0)
- **Live demo:** [open demo](https://matheuscrafiting-netizen.github.io/Shoot-lines/)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Jogo de navegador no estilo dos "anúncios do YouTube": um esquadrão corre por 3 faixas, atira automaticamente nos bichos que vêm em sua direção e escolhe por quais portões passar. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/matheuscrafiting-netizen/Shoot-lines/blob/claude/three-lane-character-game-dexwg8/game.js](https://github.com/matheuscrafiting-netizen/Shoot-lines/blob/claude/three-lane-character-game-dexwg8/game.js)
- [https://github.com/matheuscrafiting-netizen/Shoot-lines/commit/4ebf67e0a4e493188b2a0306b09427e0bab642a0](https://github.com/matheuscrafiting-netizen/Shoot-lines/commit/4ebf67e0a4e493188b2a0306b09427e0bab642a0)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/matheuscrafiting-netizen/Shoot-lines

[Back to the awesome list](../../README.md)
