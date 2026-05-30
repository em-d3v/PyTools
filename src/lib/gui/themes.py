"""

"""

import tkinter as tk
from collections import UserDict
from tkinter import ttk
from typing import Any, Dict, List, Tuple


class CustomStyle:
    target  :str
    data    :dict
    
    def __init__(self):
        pass
    
    
    
class UIStyle(UserDict):
    """
    Style
    """
    
    def __init__(self, name:str, styles:List[CustomStyle]):
        super().__init__()
        self["name"] = name
        self["styles"] = styles
        
    def __setitem__(self, key, value:ttk.Style):
        if key == "name":
            if not isinstance(value, str):
                raise ValueError("name must be a string")
            super().__setitem__(key, value)
        elif key == "style":
            super().__setitem__(key, value)
        pass
    
    def __getitem__(self, key):
        
        return super().__getitem__(key)
    
class Theme:
    """Gui theme"""
    name: str
    _settings:list
    _styles  :List[UIStyle]
    def __init__(self):
        
        pass
    
    def apply(self, gui):
        pass