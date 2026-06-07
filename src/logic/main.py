"""
Filename: main.py
Date: 05/13/2026
Author: Elena Miller
MAIN GUI
"""
from typing import List, Tuple

from gui import AppUI
from gui.main import MainGui
from logic import AppLibDict, AppLibrary, Application
from resources import Resource

# from .apps import applications
from .basic import BasicApps, BasicCalculator
from .dev import DevLib


class MainApplication(Application):
    """Main Application Class"""
    #apps to be added to main app
    
    applications: AppLibDict 
    libraries: AppLibDict
    def __init__(self, name:str = "main", title:str = "PyTools", type:str = Application.APP_MULTI):
        super().__init__(name=name, title=title, type=type)
        #create main gui
        self.resource = Resource()
        self.applications = {}
        self.libraries = {
            "basic": BasicApps,
            "dev": DevLib
        }
        
        self.tools = []
        self._build()
    
    def add_apps(self, apps:dict, ui):
        """Add apps to the main application"""
        for app_name, app_cls in apps.items():
            if isinstance(app_cls, Application):
                app = app_cls(parent=ui._tabs_frame)
                ui.add_app(app=app.gui, title=app.title)
                self.applications.append(app)
        pass
    def add_app(self, app_cls:Application, ui):
        """Add a single app to the main application"""
        if isinstance(app_cls, Application) :
            app = app_cls(parent=ui._tabs_frame)
            ui.add_app(app=app.gui, title=app.title)
            self.applications.append(app)
            pass
        pass
    def _build(self):
        """Build the application"""
        self.gui = MainGui(on_exit = self.exit)
        # print("main: building ")
        
        ##build libraries first
        for name, cls in self.libraries.items():
            if issubclass(cls, AppLibrary):
                lib = cls(parent=self.gui._tabs_frame)
                print(f"Building {name} applications\n")
                
                print(f"Library: {lib.apps.keys()}")
                for app_name, app_cls in lib.apps.items():
                    
                    print(f"App:{app_name}\n")
                    if issubclass(app_cls, Application):
                        lib.add(app_cls)
                        # inst = app_cls(parent=lib.gui.notebook)
                        # print(f"added app")
                        # gui = inst.gui
                        # n = inst.name
                        # icon = inst.icon
                        # lib.gui.AddToTabs(params=(gui, n, icon))
                        # lib.applications[app_name] = inst
                        # self.applications[app_name] = inst
                        self.gui.add_ui(lib.gui,name,None)
                        pass
                    #add gui
                
        
            pass
        pass
    
    def run(self):
        """Run Main Loop"""
        if self.gui is not None:
            self.gui.mainloop()
            
    def exit(self):
        """Exit the application"""
        if self.gui is not None:
            self.gui.destroy()





