# Scope Creep

> Verified game note.

![Scope Creep screenshot placeholder](scope-creep-placeholder.svg)

## At a glance

- **Score:** 7.4/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, Phaser, Browser
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/inetslop/scope-creep](https://github.com/inetslop/scope-creep)
- **Evidence:** [direct model evidence](https://github.com/inetslop/scope-creep/commit/90b04a471d2527d95d3a1d83fd64309e2798a438)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

An abstract, Bauhaus-style twin-stick roguelite for desktop and mobile browsers, built continuously by a fleet of local LLM agents. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/inetslop/scope-creep/blob/main/site/build-log.ts](https://github.com/inetslop/scope-creep/blob/main/site/build-log.ts)
- [https://github.com/inetslop/scope-creep/commit/90b04a471d2527d95d3a1d83fd64309e2798a438](https://github.com/inetslop/scope-creep/commit/90b04a471d2527d95d3a1d83fd64309e2798a438)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/inetslop/scope-creep

[Back to the awesome list](../../README.md)
