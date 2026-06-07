"""
Filename: example.py
Date: 05/13/2026
Author: Elena Miller
Desc:
for app development purposes only
"""

from gui.dev import DevLib as Gui
from gui.dev import LoggerUI
from logic import AppLibrary, Application

from .logger import LoggerTool
from .test_app import TestApp

applications = {
    "logger": LoggerTool,
    "test_app":TestApp
}
class DevLib(AppLibrary):
    """development library"""
    name = "dev"
    title = "DEV"
    
    
    def __init__(self,gui=None, apps=applications, parent=None):
        """
        create instance
        """
        super().__init__(name="dev",title="Development",
                        gui=gui, 
                        apps={
                            # "logger": LoggerTool,
                            "test_app":TestApp
                        }, 
                        parent=parent
                        )
        
        pass
    
    def __call__(self, *args, **kwds):
        """call desc"""
        pass