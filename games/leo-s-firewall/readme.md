# Leo's Firewall

> Verified game note.

![Leo's Firewall screenshot](https://raw.githubusercontent.com/Mhielikiks/leos-firewall/main/docs/screenshots/solo.png)

## At a glance

- **Score:** 7.2/10
- **Screenshot rating:** 5.0/10 ([manually reviewed image](https://github.com/Mhielikiks/leos-firewall/blob/main/docs/screenshots/solo.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5
- **Technology:** Python
- **Estimated FP32 operations/s at 60 FPS:** 100,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/Mhielikiks/leos-firewall](https://github.com/Mhielikiks/leos-firewall)
- **Evidence:** [direct model evidence](https://github.com/Mhielikiks/leos-firewall/commit/0a8199923735deb984f1db73c4799122e9f21552)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/Mhielikiks/leos-firewall/blob/main/docs/screenshots/solo.png) — 📸 5.0/10 · manual visual review · Use this frame for the game-level score. Pixel character on a red checkered floor with HUD; simple but clear.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

Retro 8-bit reflex game in Python/Tkinter: block orbs with Leo's Firewall. Solo leaderboard (PostgreSQL) and local split-screen PvP. Commit carries an exact Claude Opus 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/Mhielikiks/leos-firewall/blob/main/database/services.py](https://github.com/Mhielikiks/leos-firewall/blob/main/database/services.py)
- [https://github.com/Mhielikiks/leos-firewall/commit/0a8199923735deb984f1db73c4799122e9f21552](https://github.com/Mhielikiks/leos-firewall/commit/0a8199923735deb984f1db73c4799122e9f21552)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/Mhielikiks/leos-firewall

[Back to the awesome list](../../README.md)
