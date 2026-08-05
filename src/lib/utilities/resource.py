"""Resource.py
"""
import sys as sys
from collections import UserDict
from enum import Enum
from os import path
from pathlib import Path
from typing import Any, List, Literal

from lib.utils import FilePath, GetPath

from .data import ResourceData

ResourceType = Literal["data","image", "file"]
"""Resource Types"""


# class ResourceFile(UserDict):
#   # filepath: str
#   # filetype: str
#   # filename: str
#   # file_ext: str
#   __slots__ = ["filename", "filetype", "extension","filepath"]
#   def __init__(self, iterable):
#     super().__init__(iterable)

#   def __getitem__(self, key):
#       return super().__getitem__(key)

#   def __setitem__(self, key, item):
#       super().__setitem__(key, item)
    
    
ResourceGetter = Literal["name", "type", "src", "value","data","config"]
ResourceSetter = Literal["name", "type", "src", "value"]
ResourceAccessible = ["name","type","src","value","config"]
class Resource:
  """ Resource Class
  """
  id: int
  """resource id"""
  name: str
  """resource name"""
  type: ResourceType
  """resource type"""
  src: str | List[str]
  """source path"""
  data: ResourceData
  """resource data"""
  value: Any
  """resource value"""
  config: dict
  def __init__(self, id=0, name=None, src=[], type=None, value=None, config={}):
    """
    Create Resource Object
    Args:
      id (int): Resource id
      name (str): Resource Name
      type (ResourceType): Resource type
      src (str | List[str]): Resource source path
      value (Any): Resource Value
      
    """
    self.id = id
    self.name = name
    self.src = src
    self.type = type
    self.value = value
    self.config = {}
    self.data = ResourceData({'id':id,'name':name,'src':src,'type':type,'value':value,'config':config})
    
  def __call__(self, **kwds):
    """
    """
    rsrc = Resource()
    params = kwds.keys
    for param in params:
      value = kwds.get(param)
      if param in ResourceAccessible:
        rsrc.set(param,value=value)
      else:
        if param == "data":
          rsrc.data = value
          pass
    return rsrc
  
  def _update():
    
    pass
  """-------------------- Public Methods --------------------"""
  def get(self, config:ResourceGetter):
    """Get Config of resource

    Args:
        config (ResourceGetter): _description_
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
      case "config":
          return self.config
      case _:
        return self.config[config]
  
  def set(self, config:ResourceSetter|str, value):
    """Set Config

    Args:
        config (ResourceSetter | str): _description_
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


  # def filepath(self) -> str:
  #   """Get Filepath of Resource (If resource is a file)

  #   Returns:
  #       str: resource file path
  #   """
  #   rootpath = False # path.join(sys.path[0],)
  #   if self.src is not None:
  #     rootpath = self.src
  #     # return FilePath()
    
  #   return
  
  """ -------------------- Static Methods --------------------"""
