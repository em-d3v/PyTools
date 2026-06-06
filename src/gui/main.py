"""
Filename: main.py
Date: 05/13/2026
Author: Elena Miller

"""

import sys
import tkinter as tk
from tkinter import ttk
from typing import List

import resources as res
from gui import MenuItem, MenuItemList
from gui.application import AppLibraryUI, AppUI
from gui.comp.menu_bar import MainMenuBar
from lib.gui import constants as gs
from logic.application import AppLibrary, Application


class MainGui(tk.Tk):
    """
    Root Gui
    """
    TITLE = "Tools"
    SIZE = "500x400"
    MENU_BAR_LABELS: List[str]  = [""]
    app_libs: List
    def __init__(self,on_exit:callable = None, **kwargs):
        """
        Docstring for __init__
        """
        self.res = res.Resource()
        # root
        super().__init__(**kwargs)
        self.geometry(self.SIZE)
        self.title(self.TITLE)
        #menu bar
        menu_bar = MainMenuBar(self)
        menu_bar.config(font=gs.DEFAULT_MENU_FONT)
        # main_menu = tk.Menu()
        self.menu_bar = menu_bar
        self._app = None
        self._body_panel = tk.Frame(master=self)
        self._tabs_frame = ttk.Notebook(master=self._body_panel)
        self._tabs_frame.pack(expand=True, fill="both")
        #add apps to tabs
    
        # self._build_apps()
        
        self._body_panel.pack(expand=True, fill="both")
        #Add menus
        self.menu_bar.add_menu(MenuItemList(name="File", 
                items=[ 
                        MenuItem(label="Log", cmd=None, menu=None),
                        MenuItem(label="Exit", cmd=on_exit, menu=None),
                        MenuItem(label="settings", cmd=None, menu=None),
                ]
        ))
        
        # file_menu:MenuItemList = MenuItemList(name="File", 
        #         items=[ 
        #                 MenuItem(label="Log", cmd=None, menu=None),
        #                 MenuItem(label="Exit", cmd=on_exit, menu=None),
        #                 MenuItem(label="settings", cmd=None, menu=None),
        #         ]
        # )
        # self.menu_bar.add_menu(file_menu)
        tool_menu:MenuItemList = MenuItemList(name="Tool", 
                items=[ 
                        MenuItem(label="Logger", cmd=None, menu=None),
                        # MenuItem(label="Exit", cmd=self.exit, menu=None),
                ]
        )
        self.protocol("WM_DELETE_WINDOW", on_exit)
        
    def _build(self):
        """
        Build Application
        """
        
        pass
    
    def add_app(self, app:AppUI|AppLibraryUI,title:str, icon:str= None)->None:
        """Add Application
        app: App to add         
        icon: icon to use for app tab
        """
        if icon is not None:
            self._tabs_frame.add(app, text=title,image=res.ResImg(icon), compound="left")
        else:
            self._tabs_frame.add(app, text=title)
        
        
            #end if
        #end def
    def add_to_menu(self,menu:MenuItemList)->None:
        """
        
        """
        lbl = menu["name"]
        options = menu["items"]
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
            self.menu_bar.add_cascade(label = lbl, menu = sub_menu)
        pass
    
    def exit(self)->None:
        """Exit Application"""
        self._root.destroy()
        


        
        

