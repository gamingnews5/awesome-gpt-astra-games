# Ghostwolf

> Verified game note.

![Ghostwolf screenshot placeholder](ghostwolf-placeholder.svg)

## At a glance

- **Score:** 7.3/10
- **Model:** Claude Opus 5.5
- **Technology:** TypeScript, React, Browser
- **Estimated FP32 operations/s at 60 FPS:** 10,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-25
- **Repository:** [https://github.com/nvdekay/GhostWolf](https://github.com/nvdekay/GhostWolf)
- **Evidence:** [direct model evidence](https://github.com/nvdekay/GhostWolf/commit/c62ddf266b3bfe8df5850a19e41d92c746ea303f)

## Screenshots

No screenshot source is recorded yet. Keep the placeholder until a repository, awesome list, or creator source provides an image.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Web chơi Ma Sói trực tiếp: quản trò điều hành trên một máy, mỗi người chơi xem vai bí mật trên điện thoại của mình. React + TypeScript + Vite (static dist/), Supabase (Postgres + RLS, đăng nhập ẩn danh, Realtime, Edge Function). Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/nvdekay/GhostWolf/blob/main/supabase/functions/_shared/engine/engine.ts](https://github.com/nvdekay/GhostWolf/blob/main/supabase/functions/_shared/engine/engine.ts)
- [https://github.com/nvdekay/GhostWolf/commit/c62ddf266b3bfe8df5850a19e41d92c746ea303f](https://github.com/nvdekay/GhostWolf/commit/c62ddf266b3bfe8df5850a19e41d92c746ea303f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-24T01:00Z..2026-10-25T01:00Z (30-minute Opus 5.5 and wider other-model UTC partitions) joined to repositories created after 2026-10-23T01:00Z; https://github.com/nvdekay/GhostWolf

[Back to the awesome list](../../README.md)
