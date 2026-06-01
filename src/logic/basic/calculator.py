"""
basic.py
Elena Miller
Created: 5/11/2026

Main Module for Gui

"""
import tkinter as tk
from typing import List

from gui.basic.calculator import BasicCalculator as Gui
from logic.application import Application

keypad_btn_w=5
keypad_btn_h=2
class BasicCalculator(Application):
    """Basic Calculator App"""
    _text: str
    def __init__(self,parent):
        super().__init__(name="calculator",title="Calculator", gui=None)
        #configure buttons
        self.icon = "calcu"
        self.gui = Gui(master=parent)
        buttons = self.gui.keys
        for btn in buttons:
            lbl = btn.cget("text")
            cmd = lambda b=btn: self._on_press(lbl)
            btn.config(command=cmd)
            
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
            self._text = self.gui.display.get()
            