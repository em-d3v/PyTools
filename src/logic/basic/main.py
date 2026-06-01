"""
File: main.py
5/27/2026
Elena Miller
"""
from logic.application import AppLibraryUI, ApplicationLibrary
from resources import Resource

# from src.gui import 
from .calculator import BasicCalculator


class BasicApps(ApplicationLibrary):
    """App library from basic applications"""
    _apps = [
        (BasicCalculator, "calculator16x16.png")
    ]

    def __init__(self, gui=None, apps=[], parent=None):
        
        super().__init__(gui, apps, parent)
        
        for app, icon in apps:
            pass
        
        
        