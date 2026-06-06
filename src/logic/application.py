"""
File: application.py
Date: 05/13/2026
Author: Elena Miller
Application Class 
"""
import tkinter as tk
from collections import UserDict
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
    gui     : AppUI|AppLibraryUI|tk.Frame|tk.Tk
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

class AppLibrary:
    """
    Application Library Class
    Used to hold multiple small applications in a tabbed interface
    """
    apps: "AppLibDict"
    applications: "AppLibDict"
    gui: AppLibraryUI| tk.Frame
    resource = Resource()
    name: str
    title: str
    def __init__(self, name:str = "library", title:str = "Library", 
                 gui=None, apps = {}, parent=None):
        self.gui = gui
        self.name = name
        self.title = title
        self.apps = apps
        self.applications = {}
        if self.gui is None:
            if parent is not None:
                self.gui = AppLibraryUI(master=parent)
                pass
            
        if len(apps) > 0:
            self.add(apps)
        pass
      
    
    def build(self):
        if self.gui is not None:
            pass
        pass
    def add(self, data:Application|dict, icon:str=None)->None:
        """
        Adds an Application to the lib
        """
        if self.gui is not None:
            #add app
            if isinstance(data, Application):#if its 
                app = data(parent=self.gui)
                self.applications[app.name] = app
                gui = app.gui
                if icon is not None:
                    #get recource for icon
                    tab_icon = self.resource("image", name=icon)
                    self.gui.notebook.add(child=gui,text=app.title, image=tab_icon, compound="left")
                else:
                    self.gui.notebook.add(child=gui,text=app.title)
            else:
                #add multiple apps
                for name, cls in data.items():
                    app = cls(parent=self.gui.notebook)
                    img = app.icon
                    gui = app.gui
                    if icon is not None:
                        tab_icon = self.resource("image", name=img)
                        self.gui.notebook.add(child=gui,text=app.title, image=tab_icon, compound="left")
                    else:
                        self.gui.notebook.add(child=gui,text=app.title)
        pass

class AppLibDict(UserDict):
    """
    Class for App Libraries
    """
    __slots__ = ["name", "class", "apps"]
    def __init__(self,cls:"AppLibrary"):
        super().__init__()
        self["name"] = cls.name
        self["class"] = cls
        self["apps"] = {}
        if len(cls.applications) > 0:
            for name, app_cls in cls.applications.items():
                self["apps"][name] = app_cls
            
    def __getitem__(self, key:str):
        """get library data"""
        if key in self.__slots__:
            return super().__getitem__(key)
        else:
            # find app in apps
            for app in self["apps"]:
                if app.name == key:
                    return app
        return super().__getitem__(key)
    
    def __setitem__(self, key:str, value):
        super().__setitem__(key, value)
class ApplicationDict(UserDict):
    
    pass
class AppDict(UserDict):
    """
    Class to hold a list of applications
    format:
    
    
    """
    def __init__(self,list:List[Application|AppLibrary] = []):
        super().__init__()
        
        for app in list:
            if isinstance(app, Application) or isinstance(app, AppLibrary):
                self.data[app.name] = app
    def __getitem__(self, key:str):
        return self.data.get(key)
    def __setitem__(self, key:str, value:Application|AppLibrary):
        if isinstance(value, Application) or isinstance(value, AppLibrary):
            self.data[key] = value
                
            