# PokéChill

> Verified game note.

![PokéChill screenshot](https://raw.githubusercontent.com/BradSavary/pokechill/main/docs/images/pokedex.png)

## At a glance

- **Score:** 7.4/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/BradSavary/pokechill/blob/main/docs/images/pokedex.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python, Three.js, Phaser
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/BradSavary/pokechill](https://github.com/BradSavary/pokechill)
- **Evidence:** [direct model evidence](https://github.com/BradSavary/pokechill/commit/816c5d39f41f5cafe94870074fee32a7d626f987)
- **Live demo:** [open demo](https://pokechill-three.vercel.app)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/BradSavary/pokechill/blob/main/docs/images/pokedex.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Pokedex-style creature panel with list; tidy but menu-heavy.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Un jeu web idle + roguelike dans la région de Kanto. Vous reprenez une pension Pokémon abandonnée : chaque heure, un Pokémon sauvage s'y présente, attiré par ce que vous avez construit, ce que vous avez mis dans la mangeoire, l'heure qu'il est et les Pokémon… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/BradSavary/pokechill/blob/main/scripts/build_ranch_map.py](https://github.com/BradSavary/pokechill/blob/main/scripts/build_ranch_map.py)
- [https://github.com/BradSavary/pokechill/commit/816c5d39f41f5cafe94870074fee32a7d626f987](https://github.com/BradSavary/pokechill/commit/816c5d39f41f5cafe94870074fee32a7d626f987)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/BradSavary/pokechill

[Back to the awesome list](../../README.md)
