"""
Functs.py
7/9/2026
utility functions
"""

import sys as sys
import tkinter as tk
from os import path
from tkinter import ttk
from typing import List


def FilePath(src: str, *args):
    """
    Get path to file
    Args:
        src (str): Source path of the resource
        *args: Additional path components
    Returns:
        str: Path to the resource
    """
    if src is not None:
        return path.join(src, *args)
    else:
        return path.join(sys.path[0], *args)


def GetPath(root: str | None, filepath: str | List[str]) -> str:
  """
    Get path to file
    Args:
        root (str): Root path of the resource
        filepath (List[str]): List of path components
    Returns:
        str: Path to the resource
  """
  if root is not None:
      if isinstance(filepath, List):
          return path.join(root, *filepath)
      else:
          return path.join(root, filepath)
  else:
      if isinstance(filepath, List):
          return path.join(sys.path[0], *filepath)
      else:
        return path.join(sys.path[0], filepath)
