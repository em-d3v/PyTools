"""
T Module
Author: 
Date Created: 5/13/2026

Conv Package
for conversion calculations
"""
from .converter import Converter
from .enums import ConvWay
from .length import Length
from .number import NumberConversion
from .temperature import Temperature
from .volume import Volume
from .weight import Weight

converters: dict[str, Converter] = {
    "Temperature": Temperature,
    "Length": Length,
    "Weight": Weight,
    "Volume": Volume,
    "Number": NumberConversion
}
"""Converter Classes"""

__all__ = [
    ConvWay, Converter, converters,
    Length, Temperature, NumberConversion, Volume, Weight,
]
