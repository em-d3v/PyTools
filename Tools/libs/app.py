"""
Filename: app.py
Date: 05/13/2026
Author: Elena Miller

"""
import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
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