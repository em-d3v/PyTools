"""
temperature.py
5/28/2026
Elena Miller
"""
from typing import Literal, Tuple

"""Temperature type"""
UNIT = Literal["F","C","K","R"]

def Kelvin(t:Tuple[UNIT, float]):
    pass
class Temperature:
    """
    
    """
    __members = Literal["code","value"]
    code: str
    value: float
    def __init__(self, code:str, value=0):
        self.code = code
        self.value = 0
        pass
    
    def __call__(self, code):
        """
        Convert current value in Temperature object 
        """
        
        pass
    
    def _kelvin(self,temperature:Tuple[str,float]):
        """
        Converts Temperature to Calvin.
        Args:
            temperature(Tuple[str,float]): 
                string  - temperature to convert to Kelvin
                float   - temperature value
                
        """
        
        pass
    
    
    def config(self, key:str):
        """
        returns configuration
        """
        
        
        