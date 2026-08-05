"""
data.py
"""

from collections import UserDict, UserList


class ResourceData(UserDict):
    """Resource Data

    Args:
        UserDict (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
        ValueError: _description_

    Returns:
        resource_data: _description_
    """
    __slots__ = ["name", "id", "type", "value", "config"]

    def __init__(self, iterable):
        super().__init__(iterable)

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError("Only string keys are allowed")
        super().__setitem__(key, value)


class ResourcesList(UserList):
  def __init__(self, iterable):
        super().__init__(iterable)
        
  def __getitem__(self, key):
      return super().__getitem__(key)

  def __setitem__(self, key, item):
    if not isinstance(key, str):
      raise KeyError("Only string keys are allowed")
    super().__setitem__(key, item)