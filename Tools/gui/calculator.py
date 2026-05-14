"""
basic.py
Elena Miller
Created: 5/11/2026

Main Module for Gui

"""
import tkinter as tk
from typing import List

import gui.constants as gs
from ..libs.app import Application

keypad_btn_w=5
keypad_btn_h=2

class BasicCalculator(Application):
    """	    
        Basic Calculator Gui		
    """
    
    def __init__(self, master, **kwargs):
        """
        Docstring for __init__
                
        """
        super().__init__(master, **kwargs)
        self.title = "Calculator"
        self.display = tk.Entry(self, width=18,font=gs.ENTRY_FONT,
                             borderwidth=2, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self._build_keypad()
        #configure display
        
    
    
    def _build_keypad(self) -> None:
        """ Create Keypad """
        buttons: List[str] = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'        
        ]
        row = 1
        col = 0
        for label in buttons:
            #command
            cmd = lambda l=label: self._on_press(l)
            # create buttons
            btn = tk.Button(self, text=label, width=5, height=2, command=cmd)
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2
            )
            col += 1
            if col > 3:
                col = 0
                row += 1
            #end if
        #end for
    #end def
    
    def _on_press(self,char:str) ->None:
        """ logic for buttons """
        
        if (char =="="):
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif char == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, char)
            
    