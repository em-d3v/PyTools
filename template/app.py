"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""

from gui import AppUI
from logic import Application


class TemplateApplication(Application):
    """class description"""
    settings = {}
    title = "Template"
    name = "template"
    def __init__(self,name="template",title="Template",gui=None, parent=None):
        """
        create instance
        """
        super().__init__(name=name, title=title, gui=gui, parent=parent)
        pass
    
    def build(self):
        pass