"""
Custom Utilities Package

"""


from .functs import FilePath, GetPath
# from .resource.resource import Resource
from .resource import (Resource, ResourceDict, ResourceLibDict,
                       ResourceLibrary, ResourceManager, ResourcesList)

__all__ = [
  "Resource",
  "ResourceLibrary",
  "ResourceDict",
  "ResourceLibDict",
  "ResourcesList",
  "ResourceManager",
  "FilePath",
  "GetPath"
  
]