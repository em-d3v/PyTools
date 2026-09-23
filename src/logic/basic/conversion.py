"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""
import tkinter as tk
from tkinter import ttk

from gui.basic import BasicConversion as Gui
from logic import Application
from src.lib import conv

CONVERSIONS = ["Temperature", "Weight", "Volume", "Distance"]

class BasicConversion(Application):
    """class description"""
    settings = {}
    title = "Conversion"
    name = "conversion"
    
    #members
    gui: Gui
    conv_type: tk.StringVar
    conv_from: tk.Variable
    conv_to: tk.Variable
    _input: any
    _output: any
    
    def __init__(self,parent):
        
        """
        create instance
        """
        super().__init__(name="basic_conversion", title="Basic Conversion", gui=Gui(master=parent),enabled=True)
        
        
        gui = self.gui
        self.conv_type = tk.StringVar(value="")
        gui.conv_type_combo.configure(values=CONVERSIONS,textvariable=self.conv_type)
        gui.conv_type_combo.set("Select option")
        
        # gui.conv_type_combo.
        pass
    
    
    def _on_enter(self):
        pass
    
    def build(self):
        pass