"""main.py
for creating the resources needed for the application
"""

import sys as sys
import tkinter as tk
from enum import Enum
from importlib import resources as res
from os import path
from pathlib import Path
from typing import Any, List, Literal

from lib.utilities import (FilePath, GetPath, Resource, ResourceDict,
                           ResourceLibDict, ResourceLibrary, ResourceManager)

DIRECTORY = GetPath(None, ["resources"])

directories = {
    "root": DIRECTORY,
    "image": {
        "root": "img",
        "icon": "icons",
    },
    "text": {"root": "txt"},
    "file": {"root": DIRECTORY},
}

Icons = ResourceLibrary(
    ResourceLibDict({
        "calculator": ResourceDict({"name": "calculator", "type": "image", "source": [DIRECTORY, directories["image"]["root"], "icons", "calculator.png"]}),
        "add": ResourceDict({"name": "add", "type": "image", "source": [DIRECTORY, directories["image"]["root"], "icons", "add.png"]}),
        "calendar": ResourceDict({"name": "calendar", "type": "image", "source": [DIRECTORY, directories["image"]["root"], "icons", "calendar.png"]}),
        "error": ResourceDict({"name": "error", "type": "image", "source": [DIRECTORY, directories["image"]["root"], "icons", "application_error.png"]}),
    })
)
Resources = ResourceManager(resources={}, libraries={"icons": Icons})
