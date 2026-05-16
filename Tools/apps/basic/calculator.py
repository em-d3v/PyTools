"""
basic.py
Elena Miller
Created: 5/11/2026

Main Module for Gui

"""
import tkinter as tk
from typing import List

import gui.constants as gs
from lib.app import AppGui, App
from gui.calc import BasicCalculator as BasicCalculatorGui

keypad_btn_w=5
keypad_btn_h=2
class Calculator(App):
    """Basic Calculator App"""
    def __init__(self,parent):
        super().__init__(t="Calculator")
        self._build(parent)
        
    def _build(self, parent):
        """Build the application"""
        self.gui=BasicCalculatorGui(master=parent)
        buttons = self.gui.keys
        for btn in buttons:
            pass
    
    def _on_press(self,char:str) ->None:
        """ logic for buttons """
        
        if (char =="="):
            try:
                result = eval(self.gui.display.get())
                self.gui.display.delete(0, tk.END)
                self.gui.display.insert(tk.END, str(result))
            except Exception:
                self.gui.display.delete(0, tk.END)
                self.gui.display.insert(tk.END, "Error")
        elif char == "C":
            self.gui.display.delete(0, tk.END)
        else:
            self.gui.display.insert(tk.END, char)
            