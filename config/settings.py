"""
File: settings.py
Date: 05/17/2026
Author: Elena Miller
Settings for the Python Tools project.
"""

# 
from typing import Dict
from pathlib import Path
import os

PROJECT_DIR = Path(__file__).parent.parent
CONFIG_DIR = Path(__file__).parent

# LOG_DIR = f"{PROJECT_DIR}/log"
# BIN_DIR = f"{PROJECT_DIR}/bin"
# SRC_DIR = f"{PROJECT_DIR}/src"
# DATA_DIR = f"{PROJECT_DIR}/data"
DIRS = {
    "log": f"{PROJECT_DIR}/log",
    "bin": f"{PROJECT_DIR}/bin",
    "src": f"{PROJECT_DIR}/src",
    "data": f"{PROJECT_DIR}/data"
}
extensions = {
    "win": ".exe",
    "linux": "",
    "mac": ".app"
}
target = {
    "name": "PyTools",
    "dir": "./build/",
    
}

SOURCE_FILE = f"{DIRS['src']}/main.py"
target_name = "PyTools"

MAIN_FILE = f"{DIRS['src']}/main.py"
