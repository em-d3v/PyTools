"""
Filename: currency.py
Date: 05/13/2026
Author: Elena Miller

"""

class Currency:
    """
    Currency
    members:
    - name: str
    - symbol: str
    - code: str
    - value: float
    """
    
    
    def __init__(self, name: str, symbol: str, code: str, value: float):
        """Initialize a Currency object."""
        self.name = name
        self.symbol = symbol
        self.code = code
        self.value = value
        
