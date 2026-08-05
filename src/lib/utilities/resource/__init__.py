"""
__init__.py
Author: Elena Miller
Date Created: 5/13/2026

Resource Package
contains code for managing resources used by the application.
"""
from .data import ResourceData, ResourcesList
from .enums import ObjectType, ResourceType
from .manager import ResourceManager
from .resource import Resource
from .resourcelib import ResourceLibrary, ResourceLibraryData

__all__ = [
    "Resource",
    "ResourceData",
    "ResourcesList",
    "ResourceType",
    "ObjectType",
    "ResourceManager"
]