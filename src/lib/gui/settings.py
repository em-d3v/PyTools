"""
Filename: gui_settings.py
Date: 05/13/2026
Author: Elena Miller

"""

from csettings import Settings


class GuiSettings(Settings):
    """
    Class to hold GUI settings
    """
    def __init__(self):
        super().__init__()
        self.set("bg_color", "#f0f0f0")
        self.set("fg_color", "#000000")
        self.set("font", ("Arial", 12))
        self.set("entry_font", ("Arial", 14))