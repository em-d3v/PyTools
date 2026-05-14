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
from Tools.gui.calculator import BasicCalculator
class MainGui:
    """
    Root Gui
    """
    TITLE = "Tools"
    SIZE = "500x400"
    MENU_BAR_LABELS: List[str]  = [""]
    def __init__(self):
        """
        Docstring for __init__
        
        
        """
        # root
        root = tk.Tk()
        
        root.geometry(self.SIZE)
        root.title(self.TITLE)
        
        # root.config(menu=self.menu_bar.main)
        self._root = root
        # menu_bar = MainMenuBar(self.root)
        # menu_bar = tk.Menu(self._root)
        # menu_bar.main.config(font=gs.DEFAULT_MENU_FONT)
        
        # self.app_panel = tk.Frame(self.root)
        self._app = None
        self._apps: List[(str, tk.Frame)] = [
                ("Calculator", BasicCalculator)
        ]
        self._body_panel = tk.Frame(master=root)
        
        
        self._tabs_frame = ttk.Notebook(master=self._body_panel)
        self._tabs_frame.pack(expand=True, fill="both")
        self._tabs = ["Calculator", "Financial", ""]
        self._build_apps()
        self._body_panel.pack(expand=True, fill="both")
        #Add menus
        # self._file_menu = tk.Menu(self.menu_bar,tearoff=0)
        # self.menu_bar.add_cascade(label = 'File', menu = self.time_menu)
        
        # self.time_menu = tk.Menu(self.menu_bar)
        # self.menu_bar.add_cascade(label = 'Time', menu = self.time_menu)
        # self.time_menu.add_command(label = "Duration", command=None)
    def run(self):
        """Run Main Loop"""
        self._root.mainloop()
    
    def _build_menus(self):
        """Build Menus"""
        
    def _build(self):
        """Build Application"""
        
    def _build_apps(self)->None:
        """Build Application Frames"""
        
        self._basic_calc = BasicCalculator(self._tabs_frame)
        self._basic_calc.pack(expand=True, fill="both")
        
        self._tabs_frame.add(self._basic_calc, text="Calculator")
        

        
        

