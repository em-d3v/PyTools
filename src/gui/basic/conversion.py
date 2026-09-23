"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""
import tkinter as tk
from tkinter import ttk
from typing import List

from gui import AppUI
from gui.comp import ScrollFrame

PADDING = 5

class BasicConversion(AppUI):
    """
    GUI Class Name
    """
    conversion_types: list
    
    conv_type_combo: ttk.Combobox
    conv_from_combo: ttk.Combobox
    conv_to_combo: ttk.Combobox
    conv_btn: tk.Button
    input_text: tk.Text
    output_text: tk.Text
    
    def __init__(self, master,**kwds):
        """
        create instance
        """
        super().__init__(master, **kwds)
        self.scroll_frame = ScrollFrame(master=self)
        body = tk.LabelFrame(master=self.scroll_frame.inner_frame,text="Conversion")
        self.scroll_frame.pack(expand=True,fill="both")
        body.pack(expand=True,fill="both")
        
        # gui elements
        # lbl_conv_type_combo = tk.Label(master=body, text="Conversion Type:")
        # lbl_conv_type_combo.grid(row=0, column=0, padx=PADDING, pady=PADDING, sticky="w")

        self.conv_type_combo = ttk.Combobox(master=body, width=50)
        self.conv_type_combo.grid(row=0, column=0, columnspan=3, padx=PADDING, pady=PADDING, sticky="w")
        self.conv_type_combo.set("Conversion")
        # lbl_conv_from_combo = tk.Label(master=body, text="From:")
        # lbl_conv_from_combo.grid(row=1, column=0, padx=PADDING, pady=PADDING, sticky="w")
    
        self.conv_from_combo = ttk.Combobox(master=body)
        self.conv_from_combo.grid(row=1, column=0, padx=PADDING, pady=PADDING, sticky="w")
        
        lbl_conv_to_combo = tk.Label(master=body, text=" to ")
        lbl_conv_to_combo.grid(row=1, column=1, padx=PADDING, pady=PADDING, sticky="w")
        self.conv_to_combo = ttk.Combobox(master=body)
        self.conv_to_combo.grid(row=1, column=2, padx=PADDING, pady=PADDING, sticky="w")
        
        lbl_input = tk.Label(master=body,text="input:")
        lbl_input.grid(row=2,column=0, sticky="w")
        self.input_text = tk.Text(master=body, height=5, width=30)
        self.input_text.grid(row=3, column=0, columnspan=2)
        

        self.conv_btn = tk.Button(master=body, text="Convert")
        self.conv_btn.grid(row=4, column=0, columnspan=2, padx=PADDING, pady=PADDING)
        lbl_output = tk.Label(master=body,text="Output")
        lbl_output.grid(row=5,column=0)
        self.output_text = tk.Text(master=body, height=5, width=30)
        self.output_text.grid(row=6, column=0, columnspan=2, padx=PADDING, pady=PADDING)
        self.pack(expand=True, fill="both")
    pass

    