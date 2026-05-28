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
FOLDER = Path(__file__).parent
PROJECT = FOLDER.parent
# project directories
DIRECTORY = {
    "config":   FOLDER,
    "project":  PROJECT,
    "source":   "src",
    "log":      "log",
    "bin":      "bin",
    "data":     "data",
    "build":    "build",
    "res":      "rsrc",
    "cache":    "__pycache__"
}

SOURCE_FILE =  os.path.join(PROJECT, DIRECTORY["source"],"main.py")
EXTENSIONS = {
    "win": ".exe",
    "linux": "",
    "mac": ".app"
}

TARGET = {
    "name": "PyTools",
    "dir": os.path.join(PROJECT, DIRECTORY["build"]),
    "source": os.path.join(PROJECT, DIRECTORY["source"],"main.py")
}

