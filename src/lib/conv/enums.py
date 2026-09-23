"""
enums.py
5/28/26
Elena Miller
Contains Enum classes
"""
from enum import Enum
from typing import Literal


# class Conversions(Enum):
#     TEMPERATURE = "Temperature"
#     WEIGHT = "Weight"
#     VOLUME = "Volume"
class ConvWay(Enum):
    """Dictates which way conversion is conducted"""
    
    FROM_TARGET = 0 #convert from target
    TO_TARGET   = 1