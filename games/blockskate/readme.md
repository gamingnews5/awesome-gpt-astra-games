# Blockskate

> Verified game note.

![Blockskate screenshot placeholder](blockskate-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** Rust
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Bookersy/mashup-MC-skate](https://github.com/Bookersy/mashup-MC-skate)
- **Evidence:** [direct model evidence](https://github.com/Bookersy/mashup-MC-skate/commit/950d20c76ecee3b82393f098570e61dd4bd2ca8b)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Skateboard through your own Minecraft worlds. Blockskate is a standalone Rust game: it reads your Minecraft Java saves and draws them with your game's own textures, including your resource packs and your mods' blocks. You skate them with skate.-style controls. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Bookersy/mashup-MC-skate/blob/claude/rea-agent-setup-6i928y/src/skate/physics.rs](https://github.com/Bookersy/mashup-MC-skate/blob/claude/rea-agent-setup-6i928y/src/skate/physics.rs)
- [https://github.com/Bookersy/mashup-MC-skate/commit/950d20c76ecee3b82393f098570e61dd4bd2ca8b](https://github.com/Bookersy/mashup-MC-skate/commit/950d20c76ecee3b82393f098570e61dd4bd2ca8b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Bookersy/mashup-MC-skate

[Back to the awesome list](../../README.md)
