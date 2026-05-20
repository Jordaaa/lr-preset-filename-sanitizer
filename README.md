# 🗂️ Lightroom Preset Filename Cleaner

A lightweight Python utility that recursively sanitizes Lightroom preset filenames by removing unwanted character artifacts (`~~`) introduced during preset import or export workflows.

---

## Problem

When exporting or syncing Lightroom develop presets across devices or preset packs, filenames can accumulate `~~` prefixes or infixes — for example:

```
~~Warm Matte.lrtemplate
Fade~~Soft.lrtemplate
```

These artifacts break Lightroom's ability to display preset names cleanly and can cause sorting issues in the preset panel.

---

## Solution

This script walks a target preset directory recursively and strips all `~~` occurrences from filenames in-place — no manual renaming required.

```
~~Warm Matte.lrtemplate  →  Warm Matte.lrtemplate
Fade~~Soft.lrtemplate    →  FadeSoft.lrtemplate
```

---

## Usage

### 1. Clone the repo

```bash
git clone https://github.com/Jordaaa/Rename-Lightroom-Files.git
cd Rename-Lightroom-Files
```

### 2. Set your preset folder path

Open `clean_preset_names.py` and update the path to your Lightroom presets folder:

```python
# macOS default
mother_folder_path = '/Users/<your-name>/Library/Application Support/Adobe/Lightroom/Develop Presets'

# Or point to any folder containing preset files
mother_folder_path = '/path/to/your/presets'
```

### 3. Run

```bash
python clean_preset_names.py
```

The script will print each rename operation as it goes:

```
Renamed: /Develop Presets/Pack A/~~Warm Matte.lrtemplate -> /Develop Presets/Pack A/Warm Matte.lrtemplate
Renamed: /Develop Presets/Pack B/Fade~~Soft.lrtemplate -> /Develop Presets/Pack B/FadeSoft.lrtemplate
```

---

## Requirements

- Python 3.x
- No external dependencies — uses only the standard library (`os`)

---

## Common Lightroom Preset Paths

| OS      | Path                                                                                     |
|---------|------------------------------------------------------------------------------------------|
| macOS   | `~/Library/Application Support/Adobe/Lightroom/Develop Presets`                         |
| Windows | `C:\Users\<name>\AppData\Roaming\Adobe\Lightroom\Develop Presets`                       |

> ⚠️ **Tip:** Close Lightroom before running the script to avoid file lock conflicts.

---

## Project Structure

```
lightroom-preset-cleaner/
├── clean_preset_names.py   # Main script
└── README.md
```

---

## License

MIT — free to use, modify, and distribute.
