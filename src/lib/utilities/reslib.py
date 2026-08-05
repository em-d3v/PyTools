"""ResourceLib.py  
7/6/2026
"""
from typing import List

from .data import ResourcesList
from .resource import Resource, ResourceData


class ResLib:
  """
  Resource Library Class
  """
  name:str
  """Resource Library Name"""
  resources: List[Resource]
  """Resources"""
  _items: ResourcesList
  def __init__(self, name="ResourceLibrary", resources:List[Resource]|List[ResourceData]=[]):
    self.name = name
    
    self.resources = []
    # if isinstance(resources,List):
    #   for rsrc in resources:
    #     if isinstance(rsrc, ResourceData):
          
  def add(self):
    pass
  