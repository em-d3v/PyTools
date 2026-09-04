""" 
Resource.py

"""
import importlib.resources as res
import sys as sys
import tkinter as tk
from collections import UserDict
from enum import Enum
from os import path
from pathlib import Path
from typing import Any, List, Literal

from lib.utils import FilePath, GetPath

from .constants import Extensions

ResourceTypes = ["file", "image", "text","data"]
""" Resource types
    List 
"""
ResourceType = Literal["image", "text", "file", "data"]
""" ResourceType
"""

DIRECTORY = GetPath(None, ["resources"])

directories = {
    "root": DIRECTORY,
    "image": {
        "root": "img",
        "icon": "icons",
    },
    "text": {"root": "txt"},
    "file": {"root": DIRECTORY},
}

"""Resource Extensions
"""

class ResourceData(UserDict):
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
    __slots__ = ["name", "rsrc","src",
                 "filename","context","filepath",
                 ""
                 ]
    def __init__(self, iterable):
        super().__init__(iterable)
    
    def __getitem__(self, key):
        return super().__getitem__(key)
    def __setitem__(self, key, item):
        return super().__setitem__(key, item)

ResourceConfig = Literal["name", "type", "src","data"]
ResourceAccessMembers = ["name", "type", "src", "value"]
class Resource:
    """ Resource Class
    """
    name: str
    """resource name"""
    src: str | List[str]
    """source path"""

    type: ResourceType
    """resource type"""

    data: ResourceData
    """data"""
    
    value: Any
    """resource value"""
    config:dict
    
    def __init__(self, name="Resource",type="None",data=None, src=None):
        """Create Resource Object
        """
        self.name = name
        self.src = None
        self.type = type
        self.data = data
        self.value = None
        self.config = {}
        pass

    def __call__(self, resType: ResourceType, **kwargs):
        """
        Create a new resource of the specified type
        Args:
            type (ResourceType): Type of resource to create (image, text, file)
            path (List[str]): List of path components for the resource
        Returns:
            Resource object
        """
        # variables
        resource:Resource = Resource()
        resource.type = resType
        root = directories["root"]
        filepath: List[str] = [dir["root"]]
        
        print(f"Resource: getting resource of type: {resType}")
        dir = directories.get(resType, None)
        params = kwargs.keys()
        if len(kwargs) > 0:
            for param in params:
                value = kwargs.get(param)
                if param in ResourceAccessMembers:
                    resource.set(param, value=value)
                pass
        
        if resType not in ResourceTypes:
            raise ValueError(f"Invalid resource type: {resType}")
        # 
        match resType:
            case "image":
                self._image()
                # src = GetPath(root, directories["image"], filepath)
            case "text":
                self._text()
                # src = GetPath(root, directories["text"], filepath)
                pass
            case "file":
                # src = GetPath(root, directories["file"], filepath)
                self._file()
                pass
            case _:
                pass
        return resource

    """-------------------- Public Methods --------------------"""

    def get(self, config: Literal["name", "type", "src", "value"]) -> Any:
        """
        Get Configuration from Resource
        Args:
            config (Literal):
                name: return resource name
                type 

        """
        match config:
            case "name":
                return self.name
            case "type":
                return self.type
            case "src":
                return self.src
            case "value":
                return self.value
            # case "path":
                # filename, file_extension = filepath.splitext(src)
                # print(
                #     f"Resource: filename: {filename}, file_extension: {file_extension}"
                # )
                # return GetPath(directories["root"], self.src)
            case _:
                return self.config[config]
                # raise ValueError(f"Invalid Resource config: {config}")

    def set(self, config: Literal["name", "type", "src", "value"] | str, value):
        """Set Config

        Args:
            config (Literal["name", "type", "src", "value"] | str): config member
            value (Any)
        """
        match config:
            case "name":
                self.name = value
            case "type":
                self.type = value
            case "src":
                self.src = value
            case "value":
                self.value = value
            case  "config":
                self.config = value
            case _:
                self.config[config] = value
    pass
    def path(self)->str:
        root = directories["root"]
        #get path to resource
        src = self.src
        return GetPath(root,src)
    def _image(self,**kwargs):
        """Get Image
        """
        root = FilePath(directories["root"], directories["image"]["root"])
        p = GetPath(root,self.src)
        image = tk.PhotoImage(file=p)
        self.value = image
    def _text(self):
        self.value = ""
        pass
    def _file(self):
        self.value = None
        pass
    def file(self, type: ResourceType, src: str = None, **kwargs):
        """
        Get resource of specified type
        Args:
            type (ResourceType): Type of resource to get (image, text, file)
            src (str): Source path of the resource
        Returns:
            Resource object or None if not found
        """
        pass

    
    """ -------------------- Static Methods --------------------"""
    
    @staticmethod
    def get_type(*args):
        """Get Resource Type
        Returns:
            resourceType: string of resource type
        """
        resourceType = "unknown"
        res_path = GetPath(None, *args)
        # check if filename has an extension

        ext = path.splitext(res_path)[1][1:]
        return resourceType

    @staticmethod
    def get_path(src: str | None = None, *args):
        """
          Get path for resource
          Args:
        """
        if src is not None:
            rpath = src.join(src, *args)
        else:
            rpath = src.join(sys.path[0], "resources", *args)
        return rpath
