"""
Filename: main.py
Date: 05/13/2026
Author: Elena Miller

"""
from typing import List, Tuple

from gui.main import MainGui
from lib import Application, ApplicationGui

from .basic.calculator import BasicCalculator


class MainApplication(Application):
    """Main Application Class"""
    #apps to be added to main app
    _apps = [
        (BasicCalculator, "calculator16x16.png")
    ]
    def __init__(self, name:str = "main", title:str = "PyTools", type:str = Application.APP_MULTI):
        super().__init__(name=name, title=title, type=type)
        #create main gui
        self.gui=MainGui(on_exit=self.exit)
        # self.
        self.applications = []
        self.tools = []
        self._build()
        
    def _build(self):
        """Build the application"""
        print("main: building (tbi)")
        for app_cls, icon in self._apps:
            app = app_cls(parent=self.gui._tabs_frame)
            self.gui.addApp(app, icon)
            self.applications.append(app)
        pass
    
    def run(self):
        """Run Main Loop"""
        if self.gui is not None:
            self.gui.mainloop()
            
    def exit(self):
        """Exit the application"""
        if self.gui is not None:
            self.gui.destroy()





