"""
File: application.py
Date: 05/13/2026
Author: Elena Miller
Application Class 
"""
import tkinter as tk
from tkinter import ttk
from typing import List, Tuple

from gui import AppLibraryUI, AppUI
from resources import Resource


class Application:
    """
    Base Class for Applications
    """
    """Application Types"""
    APP_SINGLE = "single" # application is a single tool
    APP_MULTI = "multi"   # application is a library of tools
    gui     : AppUI
    name    : str
    title   : str
    settings: dict
    data    : dict
    icon    : str | None
    enabled : bool
    def __init__(self, name:str = "app", title:str = "App", type:str = APP_SINGLE, gui:ttk.Frame|tk.Tk = None, enabled=False):
        """
        Create an Application Instance
        Parameters:
            name (str): Name of the application (default: {"app"})
            title (str): Title of the application (default: {"App"})
            type (str): Type of the application (default: {"single"})
            gui (ttk.Frame): GUI for the application (default: None)
        """
        self._type = type
        self.name = name
        self.title = title
        self.gui = gui
        self.settings = {}
        self.data = {}
        self.enabled = False
    
    """private methods"""
    def _build(self):
        """
        Method to build the application
        """
        pass
    
    def _on_event(self, event:str, data:dict = {}):
        """
        Method to handle events
        """
        pass
    
    """public methods"""
    def get(self, key:str, default=None):
        """
        Method to get a value from the application data
        """
        return self.data.get(key, default)
    
        
    def trigger(self, event:str, data:dict = {}):
        """
        Method to trigger events
        """
        self._on_event(event, data)
    
    def save(self):
        """
        Method to save the application state
        """
        pass
    def load(self,data):
        """
        Method to load the application state
        """
        pass
    def reset(self):
        """
        Method to reset the application state
        """
        pass

class ApplicationLibrary:
    """
    Application Library Class
    Used to hold multiple small applications in a tabbed interface
    """
    _apps: List[Application]
    applications: List[Application]
    gui: AppLibraryUI| tk.Frame
    resource = Resource()
    def __init__(self,gui=None,apps:List[Tuple[Application, str]]=[],parent=None):
        self._apps
        self.applications = []
        self.gui = gui
        if self.gui is None:
            self.gui = AppLibraryUI(master=parent)
        
        
            
        pass
      
    def add_app(self,a:Application):
        pass 
    def add(self, data:Application|List[Tuple[Application, str]], icon:str=None)->None:
        """
        Adds an Application to the lib
        """
        if self.gui is not None:
            #add app
            if isinstance(data, Application):#if its 
                app = data()
                gui = app.gui
                if icon is not None:
                    tab_icon = self.resource("image", name=icon)
                    self.gui.notebook.add(child=gui,text=app.title, image=tab_icon, compound="left")
                else:
                    self.gui.notebook.add(child=gui,text=app.title)
            else:
                #add multiple apps
                for x, img in data:
                    app = x()
                    gui = app.gui
                    if icon is not None:
                        tab_icon = self.resource("image", name=img)
                        self.gui.notebook.add(child=gui,text=app.title, image=tab_icon, compound="left")
                    else:
                        self.gui.notebook.add(child=gui,text=app.title)
        pass

        