# GBFR Autofarm Script

A quick script for **Granblue Fantasy: Relink** auto farming for personal use

> This is a scuffed early implementation. Expect bugs and manual setup.

## Requirements

### Software

- Python **3.11.x**
- Windows
- Granblue Fantasy: Relink

### Required Driver

This script uses a virtual Xbox controller through ViGEmBus.

Install:

https://github.com/nefarius/ViGEmBus/releases

## Setup

1. Install Python 3.11.x

2. Clone/download this repository.

3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the virtual environment:

```bash
source env/Scripts/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Create a new folder containing:
   - The script (`.py` or `.exe`)
   - The correct resolution images used for image detection
   
   **NOTE:** The folder should contain the script (`.py` or `.exe`) and 5 .png images

2. Launch the game.

3. Ensure the game window is focused so the inputs will work.

4. Start the script.

**NOTE:** The game window must remain focused while the script is running.

## Helpful Info

### Image Detection

The script uses image recognition. If image searching is not working:

- Take screenshots from your own game window.
- Replace the provided images with your own screenshots.
- Make sure the game resolution and UI settings match.

Recommended settings:
- 1280x720 resolution
- Windowed mode
- 30 FPS

## Known issues

- The image detection may break after updates
- Changing the resolution will require new screenshots