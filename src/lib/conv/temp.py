from dataclasses import dataclass
from enum import Enum
from typing import Final, Literal, Tuple

from enums import ConvWay

t_unit = Literal["F","C","K","R"]

class Temperature:
    """Temperature class"""
    unit: t_unit
    value: float
    
    def _kelvin(self, c:ConvWay, unit:t_unit|None = None, value=None):
        """
        Converts Temperature to/from kelvin
        Args:
            c(ConvWay):    
                FROM_TARGET: convert value from target to kelvin
                TO_TARGET:   convert value from kelvin to target
            unit(t_unit|None):   target unit 
            value(float):          value
        """
        if unit == None:
            #if unit param is empty use self.unit
            unit = self.unit
        if value == None:
            value = self.value #value
        if c == ConvWay.TO_TARGET:
            #convert from kelvin to another type 
            # target is unit parameter
            match unit:
                case "K":
                    return value
                case "C":
                    return value - 273.15
                case "F":
                    return value * 9/5 - 459.67
                case "R":
                    return value * 9/5
                case _:
                    raise ValueError(f"Unknown unit: {unit}") 
            
        elif c == ConvWay.FROM_TARGET:
            #convert from target type to kelvin
            match unit:    # target is the current unit
                case "K":
                    return value
                case "C":
                    return value + 273.15
                case "F":
                    return (value + 459.67) * 5/9
                case "R":
                    return value * 5/9
                case _:
                    raise ValueError(f"Unknown unit: {unit}")

            
        else:
            raise TypeError(f"Unknown conversion way: {c}")
        
        #end
    def __init__(self, unit:t_unit="C", value:float=0.0):
        """
        Create Temperature Instance
        Args:
            unit(t_unit): temperature unit
            value(float): temperature value
        """
        self.unit = unit
        self.value = value
        pass
    
    """Public Methods"""
    def to(self, unit:t_unit )->"Temperature":
        kelvin = self._kelvin(c=ConvWay.FROM_TARGET)
        new_value = self._kelvin(c=ConvWay.TO_TARGET,unit=unit,value=kelvin)
        return Temperature(unit=unit,value=new_value)
    
    def convert(self,unit:t_unit)->None:
        kelvin = self._kelvin(c=ConvWay.FROM_TARGET)
        new_value = self._kelvin(c=ConvWay.TO_TARGET,unit=unit,value=kelvin)
        self.unit = unit
        self.value = new_value
    
    def to_f(self):
        """
        Convert from unit to fahrenheit
        """
        return self.to(unit="F")
    def to_c(self):
        """
        Convert from unit to fahrenheit
        """
        return self.to(unit="C")
    def to_k(self):
        """
        Convert from unit to fahrenheit
        """
        return self.to(unit="K")
    def to_r(self):
        """
        Convert from unit to fahrenheit
        """
        return self.to(unit="R")
    