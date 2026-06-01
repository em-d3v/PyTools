"""
application.py

"""
import tkinter as tk
from tkinter import ttk
from typing import List, Optional, Tuple


class AppUI(tk.Frame):
    """
    Base Tool GUI Class
    """
    def __init__(self, master, **kwargs):
        """
        Initialize ToolUI
        """
        super().__init__(master, **kwargs)
        
        #end
    
    def build(self):
        """
        Method to build the Tool GUI
        """
        
        pass

"""

"""
TabParams = Tuple[AppUI, str, str]

class AppLibraryUI(tk.Frame):
    """
    Application Library GUI Class
    Used to hold multiple small applications in a tabbed interface
    """
    notebook: ttk.Notebook
    
    def __init__(self, master, **kwargs):
        """
        Initialize the Application Library GUI instance
        """
        super().__init__(master, **kwargs)
        self.notebook = ttk.Notebook(master=self)
        self.notebook.pack(fill="both", expand=True)
        
    def AddToTabs(self, a:List[TabParams]):
        """
        Add application gui to tabs
        Args:
            a (List[(AppUI, str, str)])
        """
        for app, icon, lbl in a:
            if icon is not None:
                self.notebook.add(child=app,state="normal",text=lbl, image=icon, compound="left")
            else:
                self.notebook.add(child=app,state="normal",text=lbl)
        pass
    
    