# Slime Push

> Verified game note.

![Slime Push screenshot placeholder](slime-push-placeholder.svg)

## At a glance

- **Score:** 7.9/10
- **Model:** Claude Opus 5.5
- **Technology:** C++
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/shrieeiee/Slime-push](https://github.com/shrieeiee/Slime-push)
- **Evidence:** [direct model evidence](https://github.com/shrieeiee/Slime-push/commit/467edd41f6b5d38e83a6a1cb5a57bb8d27b9f6ee)
- **Live demo:** [open demo](https://not-jam.itch.io/not-jam-music-pack-2)
- **Additional live link:** [open demo](https://dylanntaylor.itch.io/buzzy-bits)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A slime-themed take on the two-player Push mode from the DS block game, made for Steam Deck,. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/shrieeiee/Slime-push/blob/main/third_party/dr_wav.h](https://github.com/shrieeiee/Slime-push/blob/main/third_party/dr_wav.h)
- [https://github.com/shrieeiee/Slime-push/commit/467edd41f6b5d38e83a6a1cb5a57bb8d27b9f6ee](https://github.com/shrieeiee/Slime-push/commit/467edd41f6b5d38e83a6a1cb5a57bb8d27b9f6ee)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/shrieeiee/Slime-push

[Back to the awesome list](../../README.md)
