"""
Filename: example.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""

import tkinter as tk
from tkinter import ttk

from gui.dev import LoggerUI
from logic import Application


class LoggerTool(Application):
    """Used for Displaying application log files"""
    name = "logger"
    title = "Logger"
    
    def __init__(self):
        """
        create instance
        """
        
        pass
    
    def __call__(self, *args, **kwds):
        """call desc"""
        pass