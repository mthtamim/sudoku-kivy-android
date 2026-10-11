# Sudoku Pro — Kivy Android App

Full-featured Sudoku game & solver converted from a Tkinter desktop app to **Kivy** for Android (and desktop).

## 🚀 Build APK with GitHub Actions

A workflow is already set up: **`.github/workflows/build-apk.yml`**

- Triggers on every push / PR to `main`
- Also supports **manual run** from the Actions tab (`workflow_dispatch`)
- Uses the official recommended `ArtemSBulgakov/buildozer-action`
- Uploads the resulting APK as a downloadable artifact named `sudoku-pro-apk`

### How to get the APK

1. Go to the **Actions** tab of this repository
2. Select the latest **Build Android APK** run
3. Download the artifact **sudoku-pro-apk**

First run can take 40–90 minutes (downloads NDK/SDK + compiles everything).

## ⚠️ Important: Full `main.py`

The current `main.py` in the repository is a short placeholder because of size limits during automated upload.

**You must replace it with the complete source** (the full ~33 KB Kivy version that contains the complete engine + UI).

The complete file is available in the original session artifacts. After replacing `main.py`, push again — the workflow will rebuild the APK with the real game.

## Features

- Grid sizes: 4×4, 9×9, 16×16
- Difficulties: Easy / Medium / Hard
- Pencil marks, timer, undo, smart hints, auto-fill, solve/check
- Save / Load, stats, dark theme
- Touch-friendly number pad

## Local Desktop Run

```bash
pip install kivy
python main.py
```

## Local Build (optional)

```bash
pip install --user buildozer cython
buildozer -v android debug
```

## Project Structure

```
.
├── main.py                      # ← replace with the full version
├── buildozer.spec
├── .github/workflows/build-apk.yml
└── README.md
```

## License

MIT
