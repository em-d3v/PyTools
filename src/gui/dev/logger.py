"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""
import tkinter as tk
from tkinter import ttk

from gui import AppUI


class LoggerUI(AppUI):
    """
    Logger UI class
    """
    
    
    def __init__(self, master, **kwargs):
        """
        create instance
        """
        super().__init__(master, **kwargs)
        body = tk.LabelFrame(self, text="Logs")
        body.pack(fill="both", expand=True)
        self.body = body
        
        self.pack(fill="both", expand=True)
        pass
    
    def __call__(self, *args, **kwds):
        """call desc"""
        pass