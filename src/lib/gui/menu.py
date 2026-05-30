"""
File: menu.py
Date: 05/14/2026
Author: Elena Miller
cusotm menu class
"""
import tkinter as tk
from collections import UserDict
from typing import Any, Dict, List


class MenuItem:
    """
    menu item
    keys:
        label:str
        command:callable or None
        menu: tk.Menu or None
        items: 
    """
    def __init__(self, label:str, cmd:callable = None, menu:tk.Menu=None, items=None):
        self.label = label
        self.command = cmd
        self.menu = menu
        self.items = None

class MenuItemList(UserDict):
    def __init__(self, name:str, items:List[MenuItem]= []):
        super().__init__()
        self["name"] = name
        self["items"] = items
        
    def __setitem__(self, key, value:MenuItem):
        if key == "name":
            if not isinstance(value, str):
                raise ValueError("name must be a string")
            super().__setitem__(key, value)
        elif key == "items":
            super().__setitem__(key, value)
        pass
    def __getitem__(self, key):
        
        return super().__getitem__(key)