"""
Filename: test_app.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""

import tkinter as tk
from tkinter import ttk

from gui import AppUI


class TestApp(AppUI):
    """class description"""
    
    
    def __init__(self, master, **kwargs):
        """
        create instance
        """
        super().__init__(master=master, **kwargs)
        title_lbl = tk.Label(master=self,text="Test App")
        title_lbl.pack(fill="x")
        self.title_lbl = title_lbl
        lbl_frame = tk.LabelFrame(master=self, text="Label Frame")
        lbl_frame.pack(fill='both')
        self.lbl_frame = lbl_frame
        pass
    
    