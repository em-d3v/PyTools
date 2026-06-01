"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller

"""
import tkinter as tk
from enum import Enum
from tkinter import ttk
from typing import List, Tuple

from lib.ui import ToolboxUI, ToolUI

from .enums import ToolType


class Tool:
    
    """A base class for tools in the application."""
    ui      : tk.Frame
    name    : str
    title   : str
    settings: dict
    data    : dict
    icon    : str | None
    enabled : bool
    def __init__(self, name:str="tool",title="Tool",type=ToolType.SINGLE,ui = None):
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
        
    def configure(self,**kwargs):
        pvalue = 0
        if len(kwargs) > 0:
            for key in kwargs:
                match key:
                    case "name":
                        self.name =kwargs[key]
                    case "title":
                        self.title =kwargs[key]
                    case "ui":
                        self.ui =kwargs[key]
                    case "settings":
                        pvalue = kwargs[key]
                        if isinstance(pvalue, "Tuple"):
                            self.settings[pvalue[0]] = pvalue[1]
                        else:
                            self.settings = pvalue
                    case "data":
                        #checkif instance is tupple
                        pvalue = kwargs[key]
                        if isinstance(pvalue, "Tuple"):
                            self.data[pvalue[0]] = pvalue[1]
                        else:
                            self.data = pvalue
                    case "enabled":
                        self.enabled = kwargs[key]
                    case _:
                        #do nothing
                        pvalue = 0
        #end
        pass

    def enable(self):
        self.enabled = True
    
    def disable(self):
        self.enabled = False
 
class Toolbox:
    """
    Class for a Collection of Tools
    """
    ui: "ToolboxUI"| tk.Frame
    tools: List[Tool]
    
    def __init__(self, ui=None,tools=[]):
        self.ui = ui
        self.tools = tools
        
    def add(self,tool:"Tool"|List[Tool],**kwargs):
        if self.ui is None:
            raise ValueError(f"missing ui")
        
        if isinstance(tool,List):
            for t in tool:
                inst = t(**kwargs)
                ui = inst.ui
                gui = None
                if ui is None:
                    gui = ui(master=self.ui.tools)
                else:
                    gui = ui
        pass
    