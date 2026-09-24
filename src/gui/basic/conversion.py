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
    
    converter_input: ttk.Combobox
    unit_input_combobox: ttk.Combobox
    unit_output_combobox: ttk.Combobox
    conv_btn: tk.Button
    input_value_box: tk.Entry
    output_value_box: tk.Entry
    
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

        self.converter_input = ttk.Combobox(master=body, width=50,state="readonly")
        self.converter_input.grid(row=0, column=0, columnspan=2, padx=PADDING, pady=PADDING, sticky="w")
        # self.lbl_selected = tk.Label(master=body, text="None")
        # self.lbl_selected.grid(row=0, column=2, padx=PADDING, pady=PADDING, sticky="w")
        
        self.converter = ttk.Labelframe(master=body,text="Converter")
        self.converter.grid(row=1, column=0, columnspan=4,rowspan=4, padx=PADDING,
                            pady=PADDING, sticky="w")
        
        lbl_unit_input = tk.Label(master=self.converter, text="From:")
        lbl_unit_input.grid(row=0, column=0, padx=PADDING, pady=PADDING, sticky="w")
        lbl_unit_output = tk.Label(master=self.converter, text="To:")
        lbl_unit_output.grid(row=0, column=1, padx=PADDING, pady=PADDING, sticky="w")
    
        self.unit_input_combobox = ttk.Combobox(master=self.converter, state="readonly")
        self.unit_input_combobox.grid(row=1, column=0, padx=PADDING, pady=PADDING, sticky="w")
        self.unit_output_combobox = ttk.Combobox(
            master=self.converter, state="readonly")
        self.unit_output_combobox.grid(row=1, column=1, padx=PADDING, pady=PADDING, sticky="w")
        
        lbl_input = tk.Label(master=self.converter,
                             text="Input:", justify="left")
        lbl_input.grid(row=2,column=0, sticky="w")
        self.input_value_box = tk.Entry(master=self.converter, width=40)
        self.input_value_box.grid(row=3, column=0, columnspan=2,  padx=2,pady=2, sticky="w")
        
        self.conv_btn = tk.Button(master=self.converter, text="Convert")
        self.conv_btn.grid(row=3, column=2, padx=PADDING, pady=PADDING)
        lbl_output = tk.Label(master=body,text="Output")
        lbl_output.grid(row=5,column=0)
        # self.output_value_box = tk.Text(master=body, height=5, width=30,state="disabled")
        self.output_value_box = tk.Entry(master=body, width=30, state="disabled")
        self.output_value_box.grid(row=6, column=0, columnspan=2, padx=PADDING, pady=PADDING)
        self.pack(expand=True, fill="both")
    pass

    