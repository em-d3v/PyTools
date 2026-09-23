"""
Filename: converter.py
Date: 9/23/2026
Author: Elena Miller
Desc:
base class
"""
from typing import Final, Literal, Tuple


class Converter:
    """
    Conversion Base Class
    """
    name: str
    """conversion name"""
    units: list[str]|dict
    """
    Conversion Units List or Dictionary
    
    """
    unit: any
    """base unit"""
  
    value: any
    """value"""
    
    def __init__(self, unit, value):
        """
        create instance
        """
        self.unit = unit
        self.value = value
        
        pass
    
    def __call__(self, conv, unit=None, value=None):
        """Conversion Call

        Args:
            conv (str): conversion to (unit)
            unit (any, optional): base unit to conver from. Defaults to None.
            value (any, optional): value to convert from. Defaults to None.
        """
        
        pass
    
    
    def set(self, member:Literal["unit","value"], value):
        """Set Member
        Args:
            member (Literal["unit","value"]): member id
            value (any): member value
        """
        match member:
            case "unit":
                self.unit = value;
                return;
            case "value":
                self.value = value;
                return;
            case _:
                return;
        pass