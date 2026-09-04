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


class ResourceLibDict(UserDict):
    """Resources Dictionary

    """

    def __init__(self, iterable: dict):
        """Create Resources Dictionary

        Args:
            iterable (dict): dictionary
        """
        super().__init__(iterable)

    def __getitem__(self, key):
        """Get Resource by key

        Args:
            key (str): Resource name

        Returns:
            Resource: Resource object
        """
        if not isinstance(key, str):
            raise KeyError("Only string keys are allowed")
        key = key.lower()
        return super().__getitem__(key)
    def __setitem__(self, key, value):
        """Set Resource by key

        Args:
            key (str): Resource name
            value (Resource): Resource object
        """
        if not isinstance(value, Resource):
            raise TypeError("Value must be a Resource object.")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        if not isinstance(key, str):
            raise KeyError("Only string keys are allowed")
        key = key.lower()
        super().__delitem__(key)
    pass

class ResourceLibrary:
    """
    Resource Library
    """
    name: str
    """Resource Library Name"""
    _resources: ResourceLibDict
    """Resource Library Resources"""
    def __init__(self, resources: ResourceLibDict = {}):
        self._resources = resources
        pass
    
    @classmethod
    def get(self,key:str):
        """Get Resource
        Args:
            index (int): _description_
            name (str | None, optional): _description_. Defaults to None.
            type (ResourceType | None, optional): _description_. Defaults to None.
        """
        resource = None
        resource = self._resources.get(key)
        return resource
    
    def add(self,key:str,rsrc:Resource):
        """Add Resource

        Args:
            rsrc (Resource): _description_
        """
        self._resources[key] = rsrc
        pass

    def remove(self,key:str):
        if key in self._resources:
            self._resources.__delitem__(key)
