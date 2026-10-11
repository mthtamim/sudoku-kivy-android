# Sudoku Pro — Kivy Android App

Full-featured Sudoku game & solver converted from a Tkinter desktop app to **Kivy** for Android (and desktop).

## Features

- **Grid sizes**: 4×4, 9×9, 16×16
- **Difficulties**: Easy / Medium / Hard
- Pencil marks (notes)
- Timer + best time records
- Undo
- Smart hints (naked/hidden singles)
- Auto-fill singles
- Solve / Check
- Save / Load game
- Stats tracking
- Dark theme (Catppuccin-inspired)
- Touch-friendly number pad for mobile

## Run on Desktop

```bash
pip install kivy pillow
python main.py
```

## Build Android APK (with Buildozer)

### Requirements (on Linux / WSL / macOS recommended)

```bash
# Install system deps (Ubuntu/Debian example)
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Install Buildozer
pip install --user buildozer
```

### Build

```bash
# Inside this folder
buildozer -v android debug
```

The APK will appear in the `bin/` folder:

```
bin/sudokupro-1.0.0-arm64-v8a-debug.apk
```

Install on phone:

```bash
adb install -r bin/*.apk
```

### Notes

- First build downloads NDK/SDK and takes a long time (30–60+ min).
- `pillow` is optional (used only for PNG export). On pure Android it may be skipped if issues arise.
- Storage uses Android’s app-private directory via `android.storage.app_storage_path`.

## Project Structure

```
.
├── main.py          # Complete app (engine + UI)
├── buildozer.spec   # Buildozer configuration
└── README.md
```

## License

MIT — feel free to use, modify and distribute.
