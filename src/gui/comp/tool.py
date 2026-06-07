"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""
import tkinter as tk
from tkinter import ttk


class ToolUI(tk.Frame):
    """
    Base Tool GUI Class
    """
    def __init__(self, master, **kwargs):
        """
        Initialize ToolUI
        """
        super().__init__(master, **kwargs)
        
        #end
    
    def _build(self):
        """
        Method to build the Tool GUI
        """
        
        pass   


class ToolboxUI(ttk.Frame):

    def __init__(self, master, **kwargs):
        """
        Initialize ToolUI
        """
        super().__init__(master, **kwargs)
        self.tools = ttk.Notebook(master=self)
        #end
    
    def _build(self):
        """
        Method to build the Tool GUI
        """
        
        pass
    def add_ui(self, tool_ui, icon):
        pass
   
    """class description"""
    member:str
    
    