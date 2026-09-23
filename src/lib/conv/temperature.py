"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""
from typing import Final, Literal, Tuple

from .converter import Converter

conv_unit = Literal["F", "C", "K", "R"]
class Temperature (Converter):
    name = "Temperature"
    """class description"""
    units = {"Celsius": "C","Fahrenheit":"F","Kelvin":"K","Rankine": "R"}  
    
    def __init__(self, unit, value):
        """
        create instance
        """
        super().__init__(unit,value)
        pass
    
    def __call__(self, conv:conv_unit, unit=None, value=None):
        """Conversion Call

        Args:
            conv (str): conversion to (unit)
            unit (any, optional): base unit to conver from. Defaults to None.
            value (any, optional): value to convert from. Defaults to None.
        """
        if unit is not None:
            self.set("unit",unit)
        if value is not None:
            self.set("value", value)
        
        result = 0.0
        match conv:
            case "C":
                result = self._celsius()
            case "F":
                result = self._fahr()
            case "K":
                result = self._kelvin()
            case "R":
                result = self._rankine()        
        return result
    
    
    def _celsius(self):
        """convert to celsius"""
        match self.unit:    # the current unit
            case "K":
                return self.value - 273.15
            case "C":
                return self.value 
            case "F":
                return (self.value-32) * 5/9
            case "R":
                return self.value * 5/9 - 273.15
            case _:
                raise ValueError(f"Unknown unit: {self.unit}")

    def _fahr(self):
        """convert to Fahrenheit"""
        match self.unit:    # current unit
            case "K":
                return (self.value*9/5) - 273.15
            case "C":
                return (self.value * 9/5) + 32
            case "F":
                return self.value 
            case "R":
                return self.value - 459.67
            case _:
                raise ValueError(f"Unknown unit: {self.unit}")

    def _kelvin(self):
        """Convert to Kelvin

        Raises:
            ValueError: _description_

        Returns:
            float: result
        """
        match self.unit:    
            case "K":
                return self.value
            case "C":
                return self.value + 273.15
            case "F":
                return (self.value + 459.67) * 5/9
            case "R":
                return self.value * 5/9
            case _:
                raise ValueError(f"Unknown unit: {self.unit}")
    
    def _rankine(self):
        """Convert to Rankine
        Raises:
            ValueError: _description_

        Returns:
            float: result
        """
        match self.unit:    
            case "K":
                return self.value
            case "C":
                return self.value + 273.15
            case "F":
                return (self.value + 459.67) * 5/9
            case "R":
                return self.value * 5/9
            case _:
                raise ValueError(f"Unknown unit: {self.unit}")
    
