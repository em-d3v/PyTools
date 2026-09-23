"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""

from .template_class import TemplateBaseClass


class TemplateSubClass(TemplateBaseClass):
    """sub class description"""
    
    
    def __init__(self):
        """
        create instance
        """
        super().__init__()
        
        pass
    
    def __call__(self, *args, **kwds):
        """call desc"""
        pass