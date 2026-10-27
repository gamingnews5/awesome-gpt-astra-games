# Lig 4 ao vivo

> Verified game note.

![Lig 4 ao vivo screenshot placeholder](lig-4-ao-vivo-placeholder.svg)

## At a glance

- **Score:** 7.2/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/lipefurlan/lige4](https://github.com/lipefurlan/lige4)
- **Evidence:** [direct model evidence](https://github.com/lipefurlan/lige4/commit/24b43f4781cb07874efa323f9e368daf3796ed8b)
- **Live demo:** [open demo](https://facamp-ia-demo-pi.vercel.app)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Lig 4 (Connect Four) multiplayer para jogar pelo celular durante uma palestra: a plateia entra por QR code, joga em duplas e o telão mostra as partidas e o placar em tempo real. Commit carries an exact Claude Opus 5.5 co-author trailer. Live demo returned HTTP 200 (availability only, not a playtest). Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/lipefurlan/lige4/blob/main/app/sala/[code]/RoomView.tsx](https://github.com/lipefurlan/lige4/blob/main/app/sala/[code]/RoomView.tsx)
- [https://github.com/lipefurlan/lige4/commit/24b43f4781cb07874efa323f9e368daf3796ed8b](https://github.com/lipefurlan/lige4/commit/24b43f4781cb07874efa323f9e368daf3796ed8b)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/lipefurlan/lige4

[Back to the awesome list](../../README.md)
