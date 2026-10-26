# Witch Way?

> Verified game note.

![Witch Way? screenshot placeholder](witch-way-placeholder.svg)

## At a glance

- **Score:** 7.6/10
- **Model:** Claude Opus 5.5
- **Technology:** Godot, GDScript
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/Anchevskiii/GameJam2026-WitchWay-](https://github.com/Anchevskiii/GameJam2026-WitchWay-)
- **Evidence:** [direct model evidence](https://github.com/Anchevskiii/GameJam2026-WitchWay-/commit/44ff1e1e40b4435e2529cb52383ba9b9858766ae)
- **Live demo:** [open demo](https://limezu.itch.io/moderninteriors)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Neskončen (endless replayability) proceduralno generiran "dungeon crawler". Igralec prevzame vlogo protagonista, ki obišče hišo strahov in ugotovi, da iz nje ni izhoda. Prostori (sobe, nadstropja, kleti, podstrešja) se generirajo sproti. Namesto klasičnega… Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Anchevskiii/GameJam2026-WitchWay-/blob/main/scripts/generators/house_generator.gd](https://github.com/Anchevskiii/GameJam2026-WitchWay-/blob/main/scripts/generators/house_generator.gd)
- [https://github.com/Anchevskiii/GameJam2026-WitchWay-/commit/44ff1e1e40b4435e2529cb52383ba9b9858766ae](https://github.com/Anchevskiii/GameJam2026-WitchWay-/commit/44ff1e1e40b4435e2529cb52383ba9b9858766ae)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/Anchevskiii/GameJam2026-WitchWay-

[Back to the awesome list](../../README.md)
