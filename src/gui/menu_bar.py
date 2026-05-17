#! /usr/bin/env python3
"""
menu_bar.py
Elena Miller
5/11/2026
Menu Bar
"""
import sys
import tkinter as tk
from tkinter import ttk
from typing import List
import lib.constants as gs

import gui.menus as menus

from lib.menu import CMenu, COption

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
        # self.add_cascade(label = 'Basic', menu = None, 
        #         font=gs.DEFAULT_MENU_FONT)
        # self.add_cascade(label = 'Financial', menu = None, 
        #         font=gs.DEFAULT_MENU_FONT)
        
        
        parent.config(menu = self)
        
    def add_menu(self,menu:CMenu)->None:
        """"""
        lbl = menu["name"]
        options = menu["options"]
        # self.add_cascade(label = lbl, menu = None)
        if options == None:
            return
        else:
            # Create a new menu for the options
            sub_menu = tk.Menu(self, tearoff=0)
            for option in options:
                opt_lbl = option.label
                command = option.command
                m = option.menu
            
                sub_menu.add_cascade(label = opt_lbl, command=command, menu=m)
                # Add the option to the menu
            self.add_cascade(label = lbl, menu = sub_menu)
        pass