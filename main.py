#!/usr/bin/env python3
"""
Sudoku Pro — Kivy version for Android (Buildozer ready)
Converted from Tkinter. Core engine kept intact.
"""
import random
import time
import copy
import json
import os
from functools import partial

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty, BooleanProperty, StringProperty
from kivy.utils import platform

# Try PIL for export (optional on Android)
try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# ---------------- Config ----------------

if platform == "android":
    from android.storage import app_storage_path
    CONFIG_DIR = os.path.join(app_storage_path(), "sudoku_gui")
else:
    CONFIG_DIR = os.path.expanduser("~/.sudoku_gui")

STATS_FILE = os.path.join(CONFIG_DIR, "stats.json")
SAVE_FILE = os.path.join(CONFIG_DIR, "save.json")
os.makedirs(CONFIG_DIR, exist_ok=True)

SIZES = {4: 2, 9: 3, 16: 4}
DIFF_RATIOS = {"easy": 0.40, "medium": 0.55, "hard": 0.68}

# Colors (Catppuccin-ish dark theme)
BG = (0.12, 0.12, 0.18, 1)
CELL_BG = (0.15, 0.15, 0.22, 1)
CELL_FIXED = (0.19, 0.20, 0.27, 1)
CELL_SELECT = (0.29, 0.30, 0.41, 1)
CELL_PEER = (0.16, 0.17, 0.25, 1)
CELL_SAME = (0.23, 0.24, 0.33, 1)
CELL_ERROR = (0.29, 0.16, 0.16, 1)
BORDER_THIN = (0.27, 0.28, 0.35, 1)
BORDER_THICK = (0.54, 0.71, 0.98, 1)
TEXT_MAIN = (0.80, 0.84, 0.96, 1)
TEXT_FIXED = (0.54, 0.71, 0.98, 1)
TEXT_USER = (0.65, 0.89, 0.63, 1)
TEXT_ERROR = (0.95, 0.55, 0.66, 1)
TEXT_HINT = (0.98, 0.89, 0.69, 1)
TEXT_PENCIL = (0.50, 0.52, 0.61, 1)
BTN_BG = (0.19, 0.20, 0.27, 1)
BTN_FG = (0.80, 0.84, 0.96, 1)
BTN_ACCENT = (0.65, 0.89, 0.63, 1)
BTN_WARN = (0.98, 0.89, 0.69, 1)
BTN_DANGER = (0.95, 0.55, 0.66, 1)

# ---------------- Engine (unchanged) ----------------

def is_valid(board, r, c, n, size, box):
    if n == 0:
        return True
    for i in range(size):
        if i != c and board[r][i] == n:
            return False
        if i != r and board[i][c] == n:
            return False
    br, bc = box * (r // box), box * (c // box)
    for i in range(br, br + box):
        for j in range(bc, bc + box):
            if (i, j) != (r, c) and board[i][j] == n:
                return False
    return True


def solve(board, size, box):
    for r in range(size):
        for c in range(size):
            if board[r][c] == 0:
                for n in range(1, size + 1):
                    if is_valid(board, r, c, n, size, box):
                        board[r][c] = n
                        if solve(board, size, box):
                            return True
                        board[r][c] = 0
                return False
    return True
