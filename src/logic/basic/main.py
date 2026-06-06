"""
File: main.py
5/27/2026
Elena Miller
"""
from gui.basic import BasicCalculator
from logic.application import AppLibrary, AppLibraryUI
from resources import Resource

# from src.gui import 
from .calculator import BasicCalculator

applications = {
        "calculator": BasicCalculator
    }

class BasicApps(AppLibrary):
    """
    App library for basic applications
    """
    __name__ = "basic_library"
    
    name = "basic"
    # apps = 
    def __init__(self, gui=None, 
                 apps=None,
                 parent=None):
        
        super().__init__(name="basic", 
                        title="Basic",
                         gui=gui, 
                         apps={
                            "calculator": BasicCalculator
                            }, 
                         parent=parent
                         )
        
        pass
        
        
        