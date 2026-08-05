"""
rsrc.py
resource
"""
from typing import Any, Final, List, Literal

from .enums import ResourceType


class Resource:
    """Resource Class
    """
    
    name:str
    """resource name"""
    type: ResourceType
    """resource type"""
    _data: Any
    """resource data"""
    value: Any
    """resource value"""
    active: bool
    """is resource active"""
    def __init__(self, name:str):
        self.name = name
        self.type = "object"
        self._data = None
        self.active = False
    
    