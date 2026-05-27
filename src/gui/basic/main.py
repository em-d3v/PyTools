"""
File: main.py  
Date: 05/17/2026
Author: Elena Miller
main gui module for basic tools
"""
import tkinter as tk
from tkinter import ttk
from lib.application import ApplicationGui
from .calculator import BasicCalculator as CalculatorGui
class BasicAppLib(ApplicationGui):
    """
    Application Library Gui
    """
    def __init__(self, master,**kwargs ):
        super().__init__(master, **kwargs)
        self._build()
        self.visible = True
        
    def _build(self):
        """Build the application"""
        self._tabs = ttk.Notebook(self)
        self._tabs.pack(fill="both", expand=True)
        pass
    def run(self):
        """Run Main Loop"""
        if self.gui is not None:
            self.gui.mainloop()
    def exit(self):
        """Exit the application"""
        if self.gui is not None:
            self.gui.destroy()


