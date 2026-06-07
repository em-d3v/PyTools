"""
File: menu.py
Date: 05/14/2026
Author: Elena Miller
custom menu module
"""
import tkinter as tk
from collections import UserDict
from enum import Enum
from tkinter import ttk
from typing import Any, Dict, List, Literal

MenuType = Literal["item","button", "submenu"]
class MenuItem:
    """
    Custom Menu Item \n
    Attributes
    ------------
    label : str
    type : MenuType
    command : callable or None
    menu : tk.Menu or None
    items : List["MenuItem"] 
    """
    label   : str
    type    : MenuType
    command : callable
    items   : List["MenuItem"]
    menu    : tk.Menu
    def __init__(self, label:str,type:MenuType="item", cmd:callable = None, menu:tk.Menu=None, items=None):
        self.label = label
        self.type = type
        self.command = cmd
        self.menu = menu
        self.items = items

class MenuItemList(UserDict):
    """
    Menu Item List User Defined Dictionary
    
    """
    
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