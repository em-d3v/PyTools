"""
Filename: test_app.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""

import tkinter as tk
from tkinter import ttk

from gui import AppUI
from gui.comp import ScrollFrame
from src.resources import Resources


class TestApp(AppUI):
    """class description"""
    PADDING = 5
    
    body: ScrollFrame
    def __init__(self, master, **kwargs):
        """
        create instance
        """
        super().__init__(master=master, **kwargs)
        # other variables
        self._row = 0
        self._column = 0
        self._test_options = ["Option 1", "Option 2", "Option 3"]
        
        
        # GUI
    
        title_lbl = tk.Label(master=self,text="Test App")
        title_lbl.pack(fill="x")
        self.title_lbl = title_lbl
        # body
        
        self.body = ScrollFrame(master=self,scroll="vertical", scrollregion=(0, 0, 500, 500))
        #scroll bar        
        
        input_frame = tk.LabelFrame(master=self.body.inner_frame, text="Inputs")
        
        # entry
        self._entry_var = tk.StringVar(value="")
        lbl_entry = tk.Label(master=input_frame, text="Entry:")
        lbl_entry.grid(row=0, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")
        
        entry_box = tk.Entry(master=input_frame, textvariable=self._entry_var)
        entry_box.grid(row=0, column=1, padx=self.PADDING, pady=self.PADDING, columnspan=1, sticky="w")
        clear_entry_btn = tk.Button(master=input_frame, text="Clear", command=lambda: self._entry_var.set(""))
        clear_entry_btn.grid(row=0, column=2, padx=self.PADDING, sticky="w")
        #text box
        self._text_var = tk.StringVar(value="")
        lbl_text = tk.Label(master=input_frame, text="Text Box:")
        lbl_text.grid(row=1, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")
       
        text_box = tk.Text(master=input_frame, height=5, width=15, wrap="word")
        text_box.grid(row=1, column=1, padx=self.PADDING, pady=self.PADDING, sticky="w")
        # combo box
        self._combo_var = tk.StringVar(value="")
        
        lbl_combo = tk.Label(master=input_frame, text="Combo Box:")
        lbl_combo.grid(row=2, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")
        combo_box = ttk.Combobox(master=input_frame, values=self._test_options)
        combo_box.set("Select option")
        combo_box.grid(row=2, column=1, padx=self.PADDING, pady=self.PADDING, sticky="w")
        
        # check box
        self._checkbox_vars = [tk.BooleanVar() for _ in self._test_options]
        
        lbl_check = tk.Label(master=input_frame, text="Check Box:")
        lbl_check.grid(row=3, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")
        self._row = 3
        self._column = 1
        self._checkboxes = []
    
        for option in self._test_options:
            check_box = tk.Checkbutton(master=input_frame, variable=self._checkbox_vars[self._test_options.index(option)], text=option)
            check_box.grid(row=self._row, column=self._column,sticky="w")
            self._checkboxes.append(check_box)
            self._row += 1
            pass
        # radio buttons
        self._radio_var = tk.StringVar(value="")
        
        lbl_radio = tk.Label(master=input_frame, text="Radio Buttons:")
        lbl_radio.grid(row=6, column=0, padx=self.PADDING, pady=self.PADDING, sticky="w")
        
        self._radio_group = []
        
        # create radio buttons
        self._row = 6
        self._column = 1
        for option in self._test_options:
            radio_btn = tk.Radiobutton(master=input_frame, variable=self._radio_var, value=option, text=option)
            radio_btn.grid(row=self._row, column=self._column, sticky="w")
            self._radio_group.append(radio_btn)
            self._row += 1
        # button for clearing radio selection
        clear_rad = tk.Button(master=input_frame, text="Clear Radio Buttons", 
                              command=lambda: self._radio_var.set(""))
        clear_rad.grid(row=10, column=1, padx=self.PADDING, pady=self.PADDING, sticky="w")
        
        # list box
        listbox_lbl = tk.Label(master=input_frame, text="List Box:")
        listbox_lbl.grid(row=11, column=0, padx=self.PADDING, pady=self.PADDING, sticky="nw")
    
        self._listbox = tk.Listbox(master=input_frame, selectmode="multiple")
        self._listbox.grid(row=11, column=1, padx=self.PADDING, pady=self.PADDING, sticky="w") 
        for option in self._test_options:
            self._listbox.insert(tk.END, option)
            
        # tree view
        lbl_tree = tk.Label(master=input_frame, text="Tree View:")
        lbl_tree.grid(row=12, column=0, padx=self.PADDING, pady=self.PADDING, sticky="nw")
        self._tree = ttk.Treeview(master=input_frame, columns=("Value"), show="headings")
        self._tree.heading("Value", text="Value")   
        self._tree.grid(row=12, column=1, padx=self.PADDING, pady=self.PADDING, sticky="w")
        input_frame.pack(fill='both',expand=True)
        
        self.lbl_frame = input_frame
        self.pack(expand=True, fill="both")
        
        self.body.pack(expand=True,fill="both")
        
        pass
    
    # def _build_tree(self):
    #     """
    #     Build the tree view with test data
    #     """
    #     for option in self._test_options:
    #         self._tree.insert("", tk.END, values=(option,))
    #     self._tree.pack(fill="both", expand=True)
    #     pass
    def label_text(self, label:tk.Label, text:str)->None:
        """Set label text"""
        label.config(text=text)
        pass
    