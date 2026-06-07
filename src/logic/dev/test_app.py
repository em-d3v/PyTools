"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""
from gui import AppUI
from gui.dev import TestApp as Gui
from logic import Application


class TestApp(Application):
    """class description"""
    icon = None
    # title = ""
    def __init__(self,name="test_app",title="Test",gui=Gui, parent=None,icon = None):
        """
        create instance
        """
        super().__init__(name=name, title=title, gui=gui, enabled=True)
        self.gui = Gui(master=parent)
        pass
    
    def build(self):
        pass