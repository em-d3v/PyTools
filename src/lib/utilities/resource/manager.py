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

from functs import FilePath, GetPath

from .data import PathDict, ResourceData
from .enums import ResourceType
from .resource import Resource

# from PIL import PIL


class ResourceManager:
    """
    Resource Manager Class
    
    """
    _dirs: dict
    _libs: dict
    _paths: PathDict
    _resources: dict
    def __init__(self, **kwargs):
        """Create Resource Manager

        Args:
            paths (dict): Resource Paths
         """
        self._paths = {}  
        self._dirs = {}
        self._resources = {}
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
    def load_resource(self, src: List[str], **kwds):
        """Load Resource

        Args:
            src (List[str]): file path list
        """
        return

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
