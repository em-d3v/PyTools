"""
Filename: main.py
Date: 05/13/2026
Author: Elena Miller

"""
from typing import List
from gui.main import MainGui
from lib.app import App
from lib import Application, ApplicationGui
from .basic.calculator import BasicCalc
class MainApplication(Application):
    """Main Application Class"""
    #apps to be added to main app
    # _apps: List[(App, str)] = [
    #     (BasicCalc, "calculator16x16.png")
    # ]
    def __init__(self):
        super().__init__(name="main", title="Main App", type=Application.APP_MULTI)
        #create main gui
        self._gui=MainGui(on_exit=self.exit)
        self._build()
        
    def _build(self):
        """Build the application"""
        print("main: building (tbi)")
        # for app_cls, icon in self._apps:
        #     self.gui.add_app(app_cls, icon)
        # pass
    
    def run(self):
        """Run Main Loop"""
        if self._gui is not None:
            self._gui.mainloop()
            
    def exit(self):
        """Exit the application"""
        if self._gui is not None:
            self._gui.destroy()


class MainApp(App):
    """Main Application Class"""
    #apps to be added to main app
    # _apps: List[(App, str)] = [
    #     (BasicCalc, "calculator16x16.png")
    # ]
    def __init__(self):
        super().__init__(t="Main App")
        #create main gui
        self.gui = MainGui(on_exit=self.exit)
        self._build()
        
    def _build(self, apps):
        """Build the application"""
        for name, app_cls, icon in apps:
            self.gui.add_app(app_cls, icon)
        pass
    def run(self):
        """Run Main Loop"""
        if self.gui is not None:
            self.gui.mainloop()
    def exit(self):
        """Exit the application"""
        if self.gui is not None:
            self.gui.destroy()


