"""
Filename: app.py
Date: 05/13/2026
Author: Elena Miller

"""
import tkinter as tk
from tkinter import ttk
class Application:
    """
    Base Application Class
    """
    
    def __init__(self, name:str = "app", title:str = "App", settings:dict = {}, data:dict = {}, gui:ttk.Frame = None):
        """
        Create an Application Instance
        Parameters:
            name (str): Name of the application (default: {"app"})
            title (str): Title of the application (default: {"App"})
            settings (dict): Settings for the application (default: {{}})
            data (dict): Data for the application (default: {{}})
            gui (ttk.Frame): GUI for the application (default: None)
        """
        
        self._type = "App"
        self.name = name
        self.title = title
        self.settings = settings
        self.data = data
        self.gui = gui
    
    def _build(self, gui:tk.Frame):
        """
        Method to build the application
        """
        pass
    
    def _on_event(self, event:str, data:dict = {}):
        """
        Method to handle events
        """
        pass
    
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
        
class AppGui(tk.Frame):
    """
    Application Gui Class for
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title = "App"
        pass
    
    def save_data(self):
        """
        Method to save data
        """
        pass
    def reset(self):
        """
        Method to reset data
        """
        pass
    def load_data(self):
        """Method to load data
        """        
        pass



class App:
    """
    Application Class 
    """
    def __init__(self, t:str = "App",gui:AppGui = None, settings:dict = {}, data:dict = {}):
        """
        Constructor for App class
        Args:
            t (str, optional): Title of the app. Defaults to "App".
            gui (AppGui, optional): GUI for the app. Defaults to None.
            settings (dict, optional): Settings for the app. Defaults to None.
            data (dict, optional): Data for the app. Defaults to None.
        """
        self.title = "App"
        self.gui = gui
        self.settings = settings
        self.data = data
        
        pass
    def save_data(self):
        """
        Method to save data
        """
        pass
    def reset(self):
        """
        Method to reset data
        """
        pass
    def load_data(self):
        """Method to load data
        """        
        pass