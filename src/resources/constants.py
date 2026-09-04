"""Constants.py
"""


from enum import Enum
from os import path
from typing import Literal

from lib.utils import GetPath

FileTypes = {
    "image": ["png", "jpg", "jpeg", "gif"],
    "text": ["txt", "md", "csv"],
    "database": ["db", "sqlite", "sqlite3"],

    "file": None,
    "unknown": None
}
Extensions = {
    "image": ["png", "jpg", "jpeg", "gif"],
    "text": ["txt", "csv"],
    "file": None,
    "unknown": None
}
