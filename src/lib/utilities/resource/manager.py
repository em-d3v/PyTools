"""Resource Manager
"""
import sys as sys
import tkinter as tk
from collections import UserDict
from enum import Enum
from importlib import resources as res
from os import path
from pathlib import Path
from typing import Any, Dict, List, Literal

from functs import FilePath, GetPath

from .data import PathDict, ResourceDict
from .enums import ResourceType
from .resource import Resource
from .resourcelib import ResourceLibDict, ResourceLibrary


class ResourceManager:
    """
    Resource Manager Class
    
    """
    _dirs: dict
    _libraries: Dict[str, ResourceLibrary]
    _paths: PathDict
    _resources: dict
    def __init__(self, resources: dict = {}, libraries: dict = {}):
        """Create Resource Manager

        Args:
            paths (dict): Resource Paths
         """
        self._paths = {}  
        self._dirs = {}
        
        self._libraries = libraries
        self._resources = resources
        pass
    # def __call__(self,type:ResourceType,  **kwds):
    #     """Get a Resource
    #     Args:
            
    #     """
    #     match(type):
    #         case "data":
                
    #             return
    #         case "file":
    #             return
    #         case "object":
    #             return
    #         case _:
    #             return None
    #     pass
    @classmethod
    def load_resource(self,key:str, **kwds):
        """Load Resource

        Args:
            key (str): Resource key
            src (List[str]): file path list
        """
        return
    def import_resource(self,key: str, src: List[str], **kwds):
        """Import Resource

        Args:
            src (List[str]): file path list
        """
        rsrc = Resource()
        return

    def get_resource(self, lib_key: str, res_key: str):
        """Get Resource

        Args:
            lib_key (str): Library key
            res_key (str): Resource key
        """
        if lib_key in self._libraries:
            library = self._libraries[lib_key]
            resource = library.get(res_key)
            return resource
        return None
    def get(self,lib_key:str, res_key:str, **kwds):
        """Get Resource

        Args:
            lib_key (str): Library key
            res_key (str): Resource key
        """
        rsrc = self.get_resource(lib_key, res_key)
        if rsrc is None:
            print(f"Resource '{res_key}' not found in library '{lib_key}'")
            return None
        
    @classmethod
    def data(self,*kwds):
        pass
    @classmethod
    def object(self,id:str,**kwds):
        
        pass
    @classmethod
    def file(self,src: List[str]):
        """Get Resource File

        Args:
            src (List[str]): file path list
        """
        return
    @staticmethod
    def Import(self, src, **kwds):
        return
    
    
