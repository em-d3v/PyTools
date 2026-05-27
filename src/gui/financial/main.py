"""
Filename: main.py
Date: 05/13/2026
Author: Elena Miller
main frame for financial tools
"""

import tkinter as tk
from tkinter import ttk
from typing import List
from lib.application import ApplicationGui

class FinancialTools(ApplicationGui):
    """Financial Tools Main Frame"""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title = "Financial Tools"
        #create notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)


