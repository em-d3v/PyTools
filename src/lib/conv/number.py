"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""

from .converter import Converter


class NumberConversion(Converter):
    """Weight Converter"""
    units = {
        "Binary": "bin",
        "Decimal": "dec",
        "Octal": "oct",
        "Hexadecimal": "hex",
        "ASCII": "ascii",
    }
    
    def __init__(self, unit, value):
        """
        create instance
        """
        super().__init__(unit=unit,value=value)
        
        pass
    
    def __call__(self, conv, unit=None, value=None):
        """Convert number"""
        if unit is not None:
            self.set("unit", unit)
        if value is not None:
            self.set("value", value)

        pass
