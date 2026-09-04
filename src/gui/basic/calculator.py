"""
basic.py
Elena Miller
Created: 5/11/2026

Calculator Gui

"""
import tkinter as tk
from typing import List

from lib.gui import constants as gs
from logic.application import AppUI

keypad_btn_w=5
keypad_btn_h=2

class BasicCalculator(AppUI):
    """	    
        Basic Calculator Gui		
    """
    NUM_KEYS: List[str] = [
        '7', '8', '9', 
        '4', '5', '6', 
        '1', '2', '3', 
        '+/-', '0', '=', 
    ]
    MAX_COLUMNS = 3
    def __init__(self, master, **kwargs):
        """
        Docstring for __init__
        """
        super().__init__(master, **kwargs)
        self.title = "Calculator"
        self.display = tk.Entry(self, width=18,font=gs.ENTRY_FONT,
                             borderwidth=2, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        #buttons
        self.keys: List[tk.Button] = []
        # self.buttons: List[str] = [
        #     '7', '8', '9', '/',
        #     '4', '5', '6', '*',
        #     '1', '2', '3', '-',
        #     'C', '0', '=', '+'      
        # ]
        self.keypad = {}
        
    
    def add_to_keypad(self,key:str,label:str,row,col, cmd):
        """
        add a key to keypad
        """
        if self.keypad[key] is None:
            btn = tk.Button(master=self,text=label, width=5, height=2, command=cmd)
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            self.keys.append(btn)
            self.keypad[key] = btn
        pass
    def button(self, id:str,**kwargs):
        """Add or configure calculator button
        Args:
            id (str): Button identifier
            **kwargs: Button configuration options (text, row, col, command)
        """
        if id not in self.keypad:
            # add button
            lbl = kwargs.get("text")
            row = kwargs.get("row")
            col = kwargs.get("col")
            cmd = kwargs.get("cmd")
            btn = None
            if cmd is None: #if no command, create a button without command
                btn = tk.Button(master=self,text=lbl,width=5, height=2)
            else:
                btn = tk.Button(master=self,text=lbl, width=5, height=2, command=cmd,)
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            # self.keys.append(btn) # add to keypad list
            self.keypad[id] = btn
            pass
        else:
            btn:tk.Button = self.keypad[id]
            btn.config(**kwargs)
        pass
    def build(self) -> None:
        """ Create Keypad """
        
        keys:List[tk.Button] = []
        row = 1
        col = 0
        for label in self.buttons:
            #command
            # create buttons
            btn = tk.Button(self, text=label, width=5, height=2)
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            keys.append(btn)
            col += 1
            if col > 3:
                col = 0
                row += 1
            #end if
        #end for
        self.keys = keys
        print(f"Total keys: {len(keys)}")
    #end def
    
    # def _on_press(self,char:str) ->None:
    #     """ logic for buttons """
        
    #     if (char =="="):
    #         try:
    #             result = eval(self.display.get())
    #             self.display.delete(0, tk.END)
    #             self.display.insert(tk.END, str(result))
    #         except Exception:
    #             self.display.delete(0, tk.END)
    #             self.display.insert(tk.END, "Error")
    #     elif char == "C":
    #         self.display.delete(0, tk.END)
    #     else:
    #         self.display.insert(tk.END, char)
            
    