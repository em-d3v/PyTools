"""
Filename: app.py
Date: 05/13/2026
Author: Elena Miller

"""
import tkinter as tk
from tkinter import ttk

class AppGui(tk.Frame):
    """
    Application Class for Creating Apps for tab frame
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