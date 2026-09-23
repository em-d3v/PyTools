"""
T Module
Author: 
Date Created: 5/13/2026

Conv Package
for conversion calculations
"""
from .converter import Converter
from .enums import ConvWay
from .temperature import Temperature

conversions = {
    "Temperature": Temperature
}
__all__ = [
    Temperature, ConvWay, Converter
    ]