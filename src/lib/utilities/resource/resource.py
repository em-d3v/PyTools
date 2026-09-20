"""
rsrc.py
resource
"""
from collections import UserDict
from typing import Any, Final, List, Literal

from .enums import ObjectType, ResourceType


class ResourceDict(UserDict):
    """Resource Data

    Args:
        UserDict (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        resource_data: _description_
    """
    __slots__ = ["name", "type","source","value","config"]

    def __init__(self, iterable):
        super().__init__(iterable)

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError("Only string keys are allowed")
        super().__setitem__(key, value)

class Resource:
    """Resource Class
    """
    
    name:str
    """resource name"""
    type: ResourceType|ObjectType
    """resource type"""
    source: str | List[str]
    """resource source (for example, a file path or URL)"""
    data: Any
    """resource data (stored in memory)"""
    value: Any
    """resource value (class instance or object)"""
    active: bool    
    """is resource active"""
    _config: dict
    """resource configurations (just in case)"""
    
    # def __init__(self, name: str, type: ResourceType = "object", data: Any = None, source: str = None, config: dict = {}):
    #     """Create Resource Object

    #     Args:
    #         name (str): Resource Name
    #         type (ResourceType): resource type
    #         source (str): resource source (for example, a file path or URL)
    #     """
    #     self.name = name
    #     self.type = type
    #     self.data = data
    #     self.source = source
    #     self.active = False
    #     self._config = config

    def __init__(self, data:ResourceDict= ResourceDict({
        "name": "Resource",
        "type": "object",
        "source": None,
        "value": None,
        "config": {}
    })):
        """Create Resource Object

        Args:
            name (str): Resource Name
            type (ResourceType): resource type
            source (str): resource source (for example, a file path or URL)
        """
        self.name = data.get("name")
        self.type = data.get("type")
        self.data = data
        self.source = data.get("source")
        self.value = data.get("value")
        self.active = False
        self._config = data.get("config")

    
    def object(self):
        """Get Resource Object
        """
        
        return self.data
    