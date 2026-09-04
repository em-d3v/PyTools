"""
__init__.py
Author: Elena Miller
Date Created: 5/13/2026

Resource Package
contains code for managing resources used by the application.
"""
from .data import ResourcesList
from .enums import ObjectType, ResourceType
from .manager import ResourceManager
from .resource import Resource, ResourceDict
from .resourcelib import ResourceLibDict, ResourceLibrary

__all__ = [
    "Resource",
    "ResourceDict",
    "ResourcesList",
    "ResourceType",
    "ObjectType",
    "ResourceLibrary",
    "ResourceLibDict",
    "ResourceManager"
]