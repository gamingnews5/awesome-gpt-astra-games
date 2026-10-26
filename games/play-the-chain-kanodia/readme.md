# Play the Chain (kanodia)

> Verified game note.

![Play the Chain (kanodia) screenshot placeholder](play-the-chain-kanodia-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-26
- **Repository:** [https://github.com/kanodia/play-the-chain](https://github.com/kanodia/play-the-chain)
- **Evidence:** [direct model evidence](https://github.com/kanodia/play-the-chain/commit/4caf2c3f254af4ae7a2511236502e1a4894122f5)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Play chess against Stockfish running inside an Internet Computer canister (C++ via icpp-pro). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/kanodia/play-the-chain/blob/main/src/sf/search.cpp](https://github.com/kanodia/play-the-chain/blob/main/src/sf/search.cpp)
- [https://github.com/kanodia/play-the-chain/commit/4caf2c3f254af4ae7a2511236502e1a4894122f5](https://github.com/kanodia/play-the-chain/commit/4caf2c3f254af4ae7a2511236502e1a4894122f5)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-26T01:00Z (30-minute Opus 5.5 partitions from 2026-10-24T20:00Z and wider other-model UTC partitions; covers windows left unsearched on 2026-10-25) joined to repositories created after 2026-10-23T01:00Z; https://github.com/kanodia/play-the-chain

[Back to the awesome list](../../README.md)
