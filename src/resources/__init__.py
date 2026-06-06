"""
Filename: __init__.py
Date: 05/13/2026
Author: Elena Miller

"""
import sys
import tkinter as tk
from typing import List, Literal, Tuple

from .rsrc import Resource

DIRECTORY = sys.path[0] + "/resources/"
IMG_DIR = DIRECTORY + "img/"

def ResImg(path:str):
    """
    Get an image from the resources directory.
    """
    p = IMG_DIR + path
    image = tk.PhotoImage(file=p)
    return image


__all__ = [
    "Resource"
]