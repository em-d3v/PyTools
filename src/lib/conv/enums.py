"""
enums.py
5/28/26
Elena Miller
Contains Enum classes
"""
from enum import Enum


class ConvWay(Enum):
    """Dictates which way conversion is conducted"""
    
    FROM_TARGET = 0 #convert from target
    TO_TARGET   = 1