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
from resources import Resource

keypad_btn_w = 5
keypad_btn_h = 2


class BasicCalculator(Application):
    """Basic Calculator App"""
    name = "calculator"
    title = "calculator"
    icon = "calculator"
    __name__ = "basic_calculator"
    # __name__ = "calculator"

    def __init__(self, parent):
        super().__init__(name="calculator", title="Calculator",
                         gui=Gui(master=parent), enabled=True)
        # configure buttons
        self.keys = {
            "7": {"text": '7', "row": 1, "col": 0, "category": "number", 'value': 7},
            "8": {"text": '8', "row": 1, "col": 1, "category": "number", 'value': 8},
            "9": {"text": '9', "row": 1, "col": 2, "category": "number", 'value': 9},
            "4": {"text": '4', "row": 2, "col": 0, "category": "number", 'value': 4},
            "5": {"text": '5', "row": 2, "col": 1, "category": "number", 'value': 5},
            "6": {"text": '6', "row": 2, "col": 2, "category": "number", 'value': 6},
            "1": {"text": '1', "row": 3, "col": 0, "category": "number", 'value': 1},
            "2": {"text": '2', "row": 3, "col": 1, "category": "number", 'value': 2},
            "3": {"text": '3', "row": 3, "col": 2, "category": "number", 'value': 3},
            "0": {"text": '0', "row": 4, "col": 1, "category": "number", 'value': 0},
            "clear": {"text": 'C', "row": 4, "col": 0, "category": "function"},
            "add": {"text": '+', "row": 1, "col": 3, "category": "operator"},
            "subtract": {"text": '-', "row": 2, "col": 3, "category": "operator"},
            "multiply": {"text": '*', "row": 3, "col": 3, "category": "operator"},
            "divide": {"text": '/', "row": 4, "col": 3, "category": "operator"},
            "negate": {"text": '+/-', "row": 4, "col": 2, "category": "function"},
            "equals": {"text": '=', "row": 5, "col": 3, "category": "function"},
        }
        
        self.enabled = True
        keys = {
            "one": {"label": '1', "row": 3, "col": 0},
        }
        buttons: List[str] = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        # keys
        # buttons:List[tk.Button] = self.gui.keys
        self._build()
        # row = 1
        # col = 0
        # for btn in buttons:
        #     def cmd(b=btn): return self._on_press(btn)
        #     self.gui.button(id=btn, label=btn, row=row, col=col, command=cmd)
        #     col += 1
        #     if col > 3:
        #         col = 0
        #         row += 1
        # for btn in self.gui.keys:
        #     lbl = btn.cget("text")
        #     print(f"key: {lbl}")
        #     cmd = lambda b=btn: self._on_press(btn)
        #     btn.config(command=cmd)

    def _build(self):
        """_summary_
        Build the calculator GUI by adding buttons to the keypad.
        """
        #add keys
        keys = self.keys.items()
        for btn_id, btn_info in keys:
            label = btn_info["text"]
            row = btn_info["row"]
            col = btn_info["col"]
            cmd = lambda b=btn_id: self._on_press(b)
            self.gui.button(id=btn_id, text=label, row=row, col=col, cmd=cmd)
        pass

    def _on_press(self, input) -> None:
        """ logic for buttons """
        char = None
        # if isinstance(input, tk.Button):
        #     char = input.cget("text")
        # else:
        char = input
        print(f"calculator: button_pressed: {char}")
        
        if (char == "equals"):
            try:
                result = eval(self.gui.display.get())
                self.gui.display.delete(0, tk.END)
                self.gui.display.insert(tk.END, str(result))
            except Exception:
                self.gui.display.delete(0, tk.END)
                self.gui.display.insert(tk.END, "Error")

        elif char == "clear" or char == "C":
            self.gui.display.delete(0, tk.END)
        else:
            self.gui.display.insert(tk.END, char)
            self._text = self.gui.display.get()
