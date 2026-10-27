# Pose Master

> Verified game note.

![Pose Master screenshot](https://raw.githubusercontent.com/HKSINGHTHAKUR/Pose-Master/main/src/main/resources/Background_Images/Background1.png)

## At a glance

- **Score:** 6.9/10
- **Screenshot rating:** 3.8/10 ([manually reviewed image](https://github.com/HKSINGHTHAKUR/Pose-Master/blob/main/src/main/resources/Background_Images/Background1.png)). Treat this as visual review only; do not infer a playtest.
- **Model:** Claude Opus 5.5, Claude Sonnet 5.5
- **Technology:** Java
- **Estimated FP32 operations/s at 60 FPS:** 1,000,000 (low confidence; static estimate, not measured).
- **Rating basis:** Heuristic from source size, README and commit history (5.8 + 0.6*log10(code KB+1), +0.3 with a reachable demo); no runtime playtest.
- **Verified:** 2026-10-27
- **Repository:** [https://github.com/HKSINGHTHAKUR/Pose-Master](https://github.com/HKSINGHTHAKUR/Pose-Master)
- **Evidence:** [direct model evidence](https://github.com/HKSINGHTHAKUR/Pose-Master/commit/45c5005146cef9be8f875c6e086fc7cf569d714f)

## Screenshots

Use the source screenshot links below. The list records these assets from the game repository or a related source.

- [screenshot 1](https://github.com/HKSINGHTHAKUR/Pose-Master/blob/main/src/main/resources/Background_Images/Background1.png) — 📸 3.8/10 · manual visual review · Use this frame for the game-level score. Empty sky and stone-block backdrop; no characters or action visible.

## Model attribution

Open the evidence link above. Evidence grade: **direct model evidence**.

## Source description

A real-time pose-matching game. The webcam watches you, a neural network recognises which of 16 poses you are holding, and you score points by matching the pose shown on screen before the timer runs out. Commit carries an exact Claude Opus 5.5 / Claude Sonnet 5.5 co-author trailer. Source inspected from README, file tree and commit history only; no playtest.

### Gameplay source

- [https://github.com/HKSINGHTHAKUR/Pose-Master/blob/main/src/main/java/com/posemaster/ui/GameFrame.java](https://github.com/HKSINGHTHAKUR/Pose-Master/blob/main/src/main/java/com/posemaster/ui/GameFrame.java)
- [https://github.com/HKSINGHTHAKUR/Pose-Master/commit/45c5005146cef9be8f875c6e086fc7cf569d714f](https://github.com/HKSINGHTHAKUR/Pose-Master/commit/45c5005146cef9be8f875c6e086fc7cf569d714f)

## Verification notes

- **Status:** verified_source
- **Counted units in repository:** 1
- **Units covered by this note:** 1
- **Discovery:** GitHub commit pool: model+game commits 2026-10-26T07:00Z..2026-10-27T01:00Z (30-minute Opus 5.5 and 2-6 hour other-model UTC partitions, via gh-read) joined to repositories created after 2026-10-25T01:00Z; https://github.com/HKSINGHTHAKUR/Pose-Master

[Back to the awesome list](../../README.md)
