"""
Filename: main.py
Date: 05/13/2026
Author: Elena Miller

"""
from typing import List
from gui.main import MainGui
from lib.app import App

from ...logic.basic.calculator import BasicCalculator

class MainApp(App):
    """Main Application Class"""
    def __init__(self):
        super().__init__(t="Main App")
        self._apps:List[(str, App)] = []
        self._build()
        
    def _build(self):
        """Build the application"""
        self.gui=MainGui(on_exit=self.exit)
        
        pass
    def run(self):
        """Run Main Loop"""
        if self.gui is not None:
            self.gui.mainloop()
    def exit(self):
        """Exit the application"""
        if self.gui is not None:
            self.gui.destroy()


