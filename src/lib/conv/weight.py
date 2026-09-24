"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""

from .converter import Converter


class Weight(Converter):
    """Weight Converter"""
    units = {
        "Microgram": "µg",
        "Milligram": "mg",
        "Gram": "g",
        "Kilogram": "kg",
        "Ounce": "oz",
        "Pound": "lb",
        "Ton": "t"
    }
    
    def __init__(self, unit, value):
        """
        create instance
        """
        super().__init__(unit=unit,value=value)
        
        pass
    
    def __call__(self, conv, unit=None, value=None):
        """Convert Weight"""
        if unit is not None:
            self.set("unit", unit)
        if value is not None:
            self.set("value", value)

        pass
