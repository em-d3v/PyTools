"""
rsrc.py
resource
"""

from collections import UserDict
# from importlib import readers
from typing import Any, Final, List, Literal

from .rsrc_data import ResourceData

RESOURCE_DATA_KEYS = Final(["name", "type", "rsrc",
                            "src", "config"])
"""Resource Data keys"""
res_data_keys = Literal["name", "type", "rsrc",
                        "src", "config"]

file_config_keys = Final(["filename", "filetype", "extension", "filepath"])
ResourceType = Literal["object", "data", "file"]


class ResourceData(UserDict):
    """
    Resource Data Dictionary

    Args:
        UserDict (_type_): _description_

    Raises:
        KeyError: Thrown when key is not instance of `str`

    """
    __slots__ = ["id", "name", "type", "resource", "config"]
    config: dict
    """
    Resource Data Configuration.
    For the purpose of keeping the resource configurations separate from data.
    This one will be used for configuring resource object.
    """

    def __init__(self, iterable: dict):
        """Create Resource Data Dictionary

        Args:
            iterable (dict): dictionary

        Raises:
            KeyError: Thrown when key is not instance of `str`
        """
        self.config = {}
        if len(iterable) > 0:
            for key, value in iterable:
                if not isinstance(key, str):
                    raise KeyError(
                        f"Only string keys are allowed. (key:{key})")
                if key in self.__slots__:
                    self.data[key] = value
                else:
                    self.config[key] = value

    def __getitem__(self, key):
        """Set Item"""
        if key in self.__slots__:
            return super().__getitem__(key)

        keys = self.config.keys()
        if key in keys:
            return self.config[key]
        return None

    def __setitem__(self, key, value):
        """
        Set item in Resource Data
        Args:
            key (str): key
            value (Any): value

        Raises:
            KeyError: thrown when `key` is not instance of `str`
        """
        if not isinstance(key, str):
            raise KeyError("Only string keys are allowed")
        key = key.lower()
        if key in self.__slots__:
            super().__setitem__(key, value)
            return
        keys = self.config.keys()
        if key in keys:
            self.config[key] = value
            return

    def __delitem__(self, key):
        if not isinstance(key, str):
            raise KeyError("Only string keys are allowed")
        key = key.lower()
        if key in self.__slots__:
            # cann
            raise SystemError(f"cannot delete attribute: {key}")
            # super().__delitem__(key)
        else:
            if key in self.config.keys():
                self.config.__delitem__(key)
    # def __del__(self, key):
    #     if key in self.__slots__:
    #         return
    #     else:
    #         self.config.
    #     pass


class Resource:
    """
    Resource Class
    """
    
    name: str
    """resource name"""
    type: ResourceType
    """resource type"""
    # src: str | List[str] | None
    _data: ResourceData
    # data: Any
    """resource data"""

    # """source path"""
    resource: Any
    """resource value"""
    config: dict
    """resource configurations"""

    def __init__(self, data: ResourceData = ResourceData({}), ):
        """Create a Resource object

        Args:
            data (ResourceData, optional): _description_. Defaults to ResourceData({}).
        """
        # self.src = None
        self.resource = None
        self.type = "object"
        self.config = {}
        self._data = data
        pass

    def __call__(self, **kwds):
        """ 
        Get a resource
        """
        # src = kwds.get("src")

        resource = None #Resource()

        return resource

    @classmethod
    def _path(self, src: List[str]):
        """Get Path to resource
        Args:
            src (List[str]): source path
        """
        pass
