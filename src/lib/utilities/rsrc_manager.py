"""Resource Manager
"""
import sys as sys
import tkinter as tk
from collections import UserDict
from enum import Enum
from importlib import resources as res
from os import path
from pathlib import Path
from typing import Any, List, Literal

from .rsrc import ResourceType


class PathDict(UserDict):
    """Resource Directory Dictionary

    Args:
        UserDict (_type_): _description_
    """
    root: str
    """path root"""
    filepaths: dict
    """directories"""
    def __init__(self, iterable):
        super().__init__(iterable)
        for key, value in iterable:
            if key == "root":
                self.root = value
            else:
                self.filepaths[key] = value
    
    
    
    def path(self, keylist:List[str]=[], data: dict=None):
        paths = []
        # if root is not None:
        #     paths.append(root)
        x:dict = None
        if data is not None:
            x = data
            paths.append(data["root"])
        else:
            x = self.data
            
        for id in keylist:
            index = keylist.index(id)
            p = x.get(id)
            if p is not None:
               if isinstance(p,str):
                   paths.append(p)
               elif isinstance(p,dict):
                   #
                   knext = keylist
                   knext.pop(index)
                   ps = self.path(keylist=knext)
                   paths.extend(ps)
            pass
        return paths
    def __getitem__(self, key):
        return super().__getitem__(key)
    
    def __setitem__(self, key, item:str|"PathDict"):
        # if isinstance()
        return super().__setitem__(key, item)


class ResourceManager:
    """
    Resource Manager Class
    """
    _dirs: dict
    _paths:dict
    _libs: dict
    def __init__(self, paths:dict={}):
        """Create Resource Manager

        Args:
            root (str, optional): _description_. Defaults to None.
        """
        self._paths = paths
        # self.root = self.paths["root"]
        # if self.root is None:
        #     self.root = sys.path[0]
            
        self._dirs = paths
        pass
    def __call__(self,type:ResourceType,  **kwds):
        """Get a Resource
        Args:
            
        """
        match(type):
            case "data":
                return
            case "file":
                return
            case "object":
                return
            case _:
                return None
        pass

    def data(self,*kwds):
        pass
    def image(self,src,**kwds):
        
        pass
    def file(self,src: List[str]):
        return
    @staticmethod
    def Import(self, src, **kwds):
        return
