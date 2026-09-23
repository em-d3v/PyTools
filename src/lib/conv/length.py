"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""

from .converter import Converter


class Length(Converter):
    """Length Converter"""
    units = {
        "Millimeter": "mm",
    }
    
    def __init__(self, unit, value):
        """
        create instance
        """
        super().__init__(unit=unit,value=value)
        
        pass
    
    def __call__(self, conv, unit=None, value=None):
        """Convert Length"""
        
        pass