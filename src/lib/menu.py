"""
File: menu.py
Date: 05/14/2026
Author: Elena Miller
cusotm menu class
"""
import tkinter as tk
from collections import UserDict
from typing import List, Dict, Any

class COption:
    """menu option
    keys:
        label:str
        command:callable or None
        menu: tk.Menu or None
    """
    def __init__(self, label:str, cmd:callable = None, menu:tk.Menu=None):
        self.label = label
        self.command = cmd
        self.menu = menu
        self.options = None


class CMenu(UserDict):
    """
    custom menu dictionary
    keys: 
    label:str
    name:str   
    cmd:callable or None 
    options:List[COption] or None
    
    """
    def __init__(self, name:str = "", options:List[COption] = None):
        super().__init__()
        self["name"] = name
        self["options"] = options
        #end
    def __setitem__(self, key, value:COption):
        if key == "name":
            if not isinstance(value, str):
                raise ValueError("name must be a string")
            super().__setitem__(key, value)
        elif key == "options":
            super().__setitem__(key, value)
        pass
    def __getitem__(self, key):
        return super().__getitem__(key)