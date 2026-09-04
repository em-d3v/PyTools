"""ResourceFile.py
7/6/2026

"""
from enum import Enum
from resource import Resource
from typing import List, Literal

from .constants import ResourceType

ImageFile = Literal["png", "jpg", "jpeg", "gif"]

class ResourceType(Enum):
    """ FileType Enum
    """
    # "text": ["txt", "md", "csv"],
    # "database": ["db", "sqlite", "sqlite3"],

    IMAGE = "png"
    TEXT = "text"
    FILE = "file"
    DATA = "data"
    UNK = "unknown"




class FileResource:
    """ ResourceFile Class
    """
    resource:str
    """resource type"""
    src:str
    """source type"""
    filepath: str
    """source path"""
    filename: str
    """File name"""
    extension:str
    """file extension"""
    name:str
    def __init__(self):
      """Create Resource File
      
      """
    #   self.filename = "resource"
    #   self.type = 
    #   self.filepath =
