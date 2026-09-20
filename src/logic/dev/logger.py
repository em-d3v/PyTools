"""
Filename: example.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""

import tkinter as tk
from tkinter import ttk

from gui.dev import LoggerUI as Gui
from logic import Application


class LoggerTool(Application):
    """Used for Displaying application log files"""
    name = "logger"
    title = "Logger"
    
    def __init__(self, name="logger", title="Logger", gui=Gui, parent=None, icon=None):
        """
        create instance
        """
        super().__init__(name=name, title=title, gui=gui, enabled=True)
        pass
    