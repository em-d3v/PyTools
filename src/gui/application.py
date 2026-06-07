"""
application.py

"""
import tkinter as tk
from tkinter import ttk
from typing import List, Optional, Tuple

from resources import Resource


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
        self.resource = Resource()
        
    def AddToTabs(self, params:List[TabParams]|TabParams):
        """
        Add application gui to tabs
        Args:
            a (List[(AppUI, str, str)])
        """
        if isinstance(params ,List):
            for a in params:
                for app,  lbl,icon in a:
                    if icon is not None:
                        self.notebook.add(child=app,state="normal",text=lbl, image=icon, compound="left")
                    else:
                        self.notebook.add(child=app,state="normal",text=lbl)
        elif isinstance(params,Tuple):
            print(f"Adding to Tabs: {params[1]}")
            app = params[0]
            lbl = params[1]
            icon = params[2]
            if icon is not None:
                image:tk.PhotoImage = self.resource(type="image",src=f"icons/{icon}",gui=True)
                self.notebook.add(child=app,state="normal",text=lbl, image=image, compound="left")
            else:
                self.notebook.add(child=app,state="normal",text=lbl)
            
        pass
    
    