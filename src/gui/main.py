"""
Filename: main.py
Date: 05/13/2026
Author: Elena Miller

"""

import sys
from typing import List
import tkinter as tk
from tkinter import ttk
import gui.constants as gs
from Tools.gui.basic.calculator import BasicCalculator
from gui.menu_bar import MainMenuBar
from lib.menu import CMenu, COption, CustMenu

class MainGui(tk.Tk):
    """
    Root Gui
    """
    TITLE = "Tools"
    SIZE = "500x400"
    MENU_BAR_LABELS: List[str]  = [""]
    def __init__(self,on_exit:callable = None, **kwargs):
        """
        Docstring for __init__
        
        
        """
        # root
        super().__init__(**kwargs)
        self.geometry(self.SIZE)
        self.title(self.TITLE)
        #menu bar
        menu_bar = MainMenuBar(self)
        menu_bar.config(font=gs.DEFAULT_MENU_FONT)
        self.menu_bar = menu_bar
        self._app = None
        self._apps: List[(str, tk.Frame)] = [
                ("Calculator", BasicCalculator)
        ]
        self._body_panel = tk.Frame(master=self)
        
        
        self._tabs_frame = ttk.Notebook(master=self._body_panel)
        self._tabs_frame.pack(expand=True, fill="both")
        #add apps to tabs
    
        self._build_apps()
        
        self._body_panel.pack(expand=True, fill="both")
        #Add menus
        file_menu:CMenu = CMenu(name="File", 
                options=[ 
                        COption(label="Log", cmd=None, menu=None),
                        COption(label="Exit", cmd=on_exit, menu=None),
                        COption(label="settings", cmd=None, menu=None),
                ]
        )
        self.menu_bar.add_menu(file_menu)
        tool_menu:CMenu = CMenu(name="Tool", 
                options=[ 
                        COption(label="Logger", cmd=None, menu=None),
                        # COption(label="Exit", cmd=self.exit, menu=None),
                ]
        )
        self.protocol("WM_DELETE_WINDOW", on_exit)
        
    def _build(self):
        """Build Application"""
        
    def _build_apps(self)->None:
        """Build Application Frames"""
        
        self._basic_calc = BasicCalculator(self._tabs_frame)
        self._basic_calc.pack(expand=True, fill="both")
        
        self._tabs_frame.add(self._basic_calc, text="Calculator")
        
    def exit(self)->None:
        """Exit Application"""
        self._root.destroy()
        

        
        

