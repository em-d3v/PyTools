"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller

"""
import tkinter as tk
from tkinter import ttk
from typing import List

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
class Tool:
    
    """A base class for tools in the application."""

    SINGLE = "single" # tool is a single function
    MULTI = "multi"   # tool is a collection of functions
    def __init__(self, name:str="tool",title="Tool",type=SINGLE,ui = None):
        """
        Create a Tool Instance
        Parameters:
            name (str): Name of the application (default: {"app"})
            title (str): Title of the application (default: {"App"})
            type (str): Type of the application (default: {"single"})
            gui (ttk.Frame): GUI for the application (default: None)
        """
        self._type      = type
        self.name       = name
        self.title      = title
        self.ui         = ui
        self.settings   = {}
        self.data       = {}
        
    
class ToolboxGui(ttk.Frame):
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
    def AddToolUI(self, tool_ui, icon):
        pass
    
class Toolbox:
    """
    Class for a Collection of Tools
    """
    def __init__(self, ui=None,tools=[]):
        self.ui = ui
        self.tools = tools
    