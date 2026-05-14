#! /usr/bin/env python3
"""
menu_bar.py
Elena Miller
5/11/2026
Menu Bar
"""
import tkinter as tk
from tkinter import ttk
from typing import List
import gui.constants as gs

FILE_MENU = {"name":"File", "options":[("Exit", None)]}
        
    
class MainMenuBar(tk.Menu):
    """
    Menu Bar for MainGui
    """
    
    def __init__(self,parent, **kwargs):
        """
        Docstring for __init__
        
        Args:
            parent (tk.Tk): Parent of Gui Object
        """
        super().__init__(parent, **kwargs)
        self.main.add_cascade(label = 'Basic', menu = None, 
                font=gs.DEFAULT_MENU_FONT)
        self.main.add_cascade(label = 'Financial', menu = None, 
                font=gs.DEFAULT_MENU_FONT)
        
        
        # parent.config(menu = self.menu_bar)
        
    def build_menu(self,menu):
        """"""
        label = menu["name"]
        options = menu["options"]
        if options is None:
            self.add_cascade(label = label, menu = None, font=gs.DEFAULT_MENU_FONT)
        else:
            # Create a new menu for the options
            
        pass