"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""

from .converter import Converter


class Volume(Converter):
    """Length Converter"""
    
    units = {
        "Millimeter": "mm", "Centimeter": "cm",
        "Meter": "m", "Kilometer": "km",
        "Inch": "in", "Foot": "ft",
        "Yard": "yd", "Mile": "mi"
        }
    
    def __init__(self, unit, value):
        """
        create instance
        """
        super().__init__(unit=unit,value=value)
        
        pass
    
    def __call__(self, conv, unit=None, value=None):
        """Convert Volume"""
        if unit is not None:
            self.set("unit", unit)
        if value is not None:
            self.set("value", value)

        pass
