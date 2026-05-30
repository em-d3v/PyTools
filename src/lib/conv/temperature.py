"""
temperature.py
5/28/2026
Elena Miller
"""
from dataclasses import dataclass
from enum import Enum
from typing import Final, Literal, Tuple

from enums import ConvWay

"""Temperature type"""
t_unit = Literal["F","C","K","R"]
conversion = Literal["conv_to","conv_from"]
valid_units = {"F","C","K","R"}
ABSOLUTE_ZERO_C:Final = -273.15
ABSOLUTE_ZERO_K: Final = 0.0

class TUnit(Enum):
    """Temperature Unit"""
    CELCIUS     = "C"
    FAHRENHEIT  = "F"
    KELVIN      = "K"
    RANKINE     = "R"
    
def Kelvin(unit:t_unit, value):
    """
    Convert temperature to Kelvin
    Args:
        unit(t_unit): temperature unit
        value(float): temperature value
    """
    code:t_unit = "K"
    result:float = 0
    if unit is not code:
        match unit:
            case "F": #
                return (value + 459.67) * 5/9
            case "C":
                value + 273.15
            case "R":
                value * 5/9
            case _: raise KeyError(f"Unit must be one of {valid_units}")
    return result
                
# @dataclass(frozen=True)
class Temperature:
    """
    
    """
    
    __members = Literal["code","value"]
    unit: TUnit #temperatur unit
    value: float #unit value (for backup)
    # value: float #also unit value (current)
    def __init__(self, code:TUnit="C", value:float=0.0):
        """Create Temperature Instance"""
        self.unit = code
        self.value = value
        pass
    def __post_init__(self):
        if self.unit not in valid_units:
            raise ValueError(f"Unit must be one of {valid_units}")
        
    
    def _kelvin(self, c:ConvWay, unit:t_unit|None = None):
        """
        Converts Temperature to/from kelvin
        Args:
            c(ConvWay):    
                FROM_TARGET: convert value from target to kelvin
                TO_TARGET:   convert value from kelvin to target
            unit(t_unit|None):   target unit 
        """
        if unit == None:
            #if unit param is empty use self.unit
            unit = self.unit
        value = self.value #value
        if c == ConvWay.TO_TARGET:
            #convert from kelvin to another type 
            # target is unit parameter
            match unit:
                case TUnit.KELVIN:
                    return value
                case TUnit.CELCIUS:
                    return value - 273.15
                case TUnit.FAHRENHEIT:
                    return value * 9/5 - 459.67
                case TUnit.RANKINE:
                    return value * 9/5
                case _:
                    return value 
            
        elif c == ConvWay.FROM_TARGET:
            #convert from target type to kelvin
            match unit:    # target is the current unit
                case TUnit.KELVIN:
                    return value
                case TUnit.CELCIUS:
                    return value + 273.15
                case TUnit.FAHRENHEIT:
                    return (value + 459.67) * 5/9
                case TUnit.RANKINE:
                    return value * 5/9
                case _:
                    return value
            
        else:
            raise TypeError(f"Unknown conversion way: {c}")
        
        #end
    
    def _kelvi(self, conv:ConvWay, value=None)->float:
        """
        Kelvin Conversion
        conv(ConvWay):
            FROM_TARGET: convert value from target to kelvin
            TO_TARGET: convert value from kelvin to target
        """
        
        if conv == ConvWay.FROM_TARGET:
            #convert from target unit to kelvin
            match self.unit:
                case TUnit.KELVIN:
                    return self.value
                case TUnit.CELCIUS:
                    return self.value + 273.15
                case TUnit.FAHRENHEIT:
                    return (self.value +459.67) * 5/9
                case TUnit.RANKINE:
                    return self.value * 5/9
                case _:
                    return self.value
                
        elif conv == ConvWay.TO_TARGET:
            # convert from kelvin to target
            if value == None:
                value = self.value
            match self.target:
                case TUnit.KELVIN:
                    return value
                case TUnit.CELCIUS:
                    return value - 273.15
                case TUnit.FAHRENHEIT:
                    return value * 9/5 - 459.67
                case TUnit.RANKINE:
                    return value * 9/5
                case _:
                    return value                
        
        return self.value
    
    def kelvin(self, unit:t_unit, v=None):
        """
        converting to kelvin
        """
        if v == None:
            v = self.value
        match unit:
            case "F":
                return (v+459.67)* (5/9)
            case "C":
                return v + 273.15
            case "R":
                return v + 5/9
            case "K": 
                return v
        #end
    def fahr(self, unit:t_unit, v=None):
        pass
            
        
    
    
    
    # --------------------
    # public api
    # ---------------------
    
    def convert(self,unit:TUnit):
        """
        Convert current value in Temperature object to another unit
        """
        
        k = self._kelvin(conv=ConvWay.FROM_TARGET)
        #new value
        n = self._kelvin(conv=ConvWay.TO_TARGET,unit=self.target, value=k)
        self.value = n
        # return Temperature(unit, n)
    def to(self,unit:TUnit):
        """
        Convert current value in Temperature object to another unit
        """
        
        k = self._kelvin(conv=ConvWay.FROM_TARGET)
        #new value
        n = self._kelvin(conv=ConvWay.TO_TARGET,unit=self.target, value=k)
        return Temperature(unit, n)
    
    def to_f(self)->float:
        return self.convert(unit=TUnit.FAHRENHEIT)
 
    def to_c(self)->float:
        return self.convert(unit=TUnit.CELCIUS)
    
    def to_k(self)->float:
        return self.convert(unit=TUnit.KELVIN)
    def to_r(self)->float:
        return self.convert(unit=TUnit.RANKINE)

   
    def config(self, key:str):
        """
        returns configuration
        """
        
        
        