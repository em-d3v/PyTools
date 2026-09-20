"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""
from gui import AppUI
from logic import AppLibrary, Application


class TemplateAppLib(AppLibrary):
    """class description"""
    
    def __init__(self,name="template",title="Template",gui=None, parent=None):
        """
        create instance
        """
        super().__init__(name=name, title=title, gui=gui, parent=parent)
        pass
    
    def build(self):
        pass