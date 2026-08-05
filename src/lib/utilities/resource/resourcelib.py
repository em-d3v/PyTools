"""rsrclib.py
7/9/2026
Resource Library 
"""
import importlib.resources as res
import sys as sys
import tkinter as tk
from collections import UserDict, UserList
from enum import Enum
from os import path
from pathlib import Path
from typing import List

from .resource import Resource, ResourceData, ResourceType


class ResourceLibraryData(UserDict):
    
    pass

class ResourceLibrary:
    """
    Resource Library
    """
    name: str
    """Resource Library Name"""
    
    resources: List[Resource]    
    def __init__(self, root=sys.path[0], resources: List[Resource] = []):
        self.root = root
        self.resources = resources
        
        pass
    
    @classmethod
    def resource(self,index:int):
        """Get Resource

        Args:
            index (int): _description_
            name (str | None, optional): _description_. Defaults to None.
            type (ResourceType | None, optional): _description_. Defaults to None.
        """
        if len(self.resources) > 0 and len(self.resources) > index:
            return self.resources[index]
        return None
    
    def add(self,rsrc:Resource):
        """Add Resource

        Args:
            rsrc (Resource): _description_
        """
        self.resources.append(rsrc)
        pass
    def remove(self,index: int):
        if len(self.resources) > 0 and len(self.resources) > index:
            resource = self.resources[index]
            self.resources.remove(resource)
