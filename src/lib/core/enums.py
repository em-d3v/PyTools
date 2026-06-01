"""
enums.py
5/30/26
Elena Miller
Contains Enum classes
"""
from enum import Enum


class ToolType(Enum):
    SINGLE = "single" # tool is a single function
    MULTI = "multi"   # tool is a collection of functions
    TOOLBOX = "toolbox"
