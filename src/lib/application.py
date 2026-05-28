"""
File: application.py
Date: 05/13/2026
Author: Elena Miller
Application Class 
"""
import tkinter as tk
from tkinter import ttk
from typing import List, Tuple
from resources import Resource
class ApplicationGui(tk.Frame):
    """
    Base Application GUI Class
    """
    
    def __init__(self, master, **kwargs):
        """
        Initialize the Application GUI instance
        """
        super().__init__(master, **kwargs)
        
        #end
    
    
    def _build(self):
        """
        Method to build the application GUI
        """
        
        pass
    


class Application:
    """
    Base Class for Applications
    """
    """Application Types"""
    APP_SINGLE = "single" # application is a single tool
    APP_MULTI = "multi"   # application is a library of tools
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

class ApplicationLibraryGui(ApplicationGui):
    """
    Application Library GUI Class
    Used to hold multiple small applications in a tabbed interface
    """
    
    def __init__(self, master, **kwargs):
        """
        Initialize the Application Library GUI instance
        """
        super().__init__(master, **kwargs)
        self.notebook = ttk.Notebook(master=self)
        self.notebook.pack(fill="both", expand=True)
        
    def AddToTabs(self, a:List[Tuple[Application, str]]):
        """
        Add application gui to tabs
        Args:
            a (List[(Application, str)])
        """
        for app, icon in a:
            gui = app.gui
            lbl = app.title
            self.notebook.add(child=gui,state="normal",)
        pass
    
        
class ApplicationLibrary:
    """
    Application Library Class
    Used to hold multiple small applications in a tabbed interface
    """
    resource = Resource()
    def __init__(self,gui=None,apps=[],parent=None):
        
        self.apps = apps
        self.gui = gui
        if self.gui is None:
            self.gui = ApplicationLibraryGui(master=parent)
        pass
    
    def Add(self, data:Application|List[Tuple[Application, str]], icon:str=None)->None:
        """
        Adds an Application to the 
        """
        if isinstance(data, Application):
            app = data()
            gui = app.gui
            if icon is not None:
                tab_icon = self.resource("image", name=icon)
                self.gui.notebook.add(child=gui,text=app.title, image=tab_icon, compound="left")
            else:
                self.gui.notebook.add(child=gui,text=app.title)
        else:
            for x, img in data:
                app = x()
                gui = app.gui
                if icon is not None:
                    tab_icon = self.resource("image", name=img)
                    self.gui.notebook.add(child=gui,text=app.title, image=tab_icon, compound="left")
                else:
                    self.gui.notebook.add(child=gui,text=app.title)
        pass

        