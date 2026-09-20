"""
data.py
"""

from collections import UserDict, UserList


class PathDict(UserDict):
    """Resource Directory Dictionary
    Args:
        UserDict (_type_): _description_
    """
    root: str
    """path root"""
    filepaths: dict
    """directories"""

    def __init__(self, iterable):
        super().__init__(iterable)
        for key, value in iterable:
            if key == "root":
                self.root = value
            else:
                self.filepaths[key] = value

    def path(self, key_list: list[str] = [], data: dict = None):
        paths = []
        # if root is not None:
        #     paths.append(root)
        x: dict = None
        if data is not None:
            x = data
            paths.append(data["root"])
        else:
            x = self.data

        for id in key_list:
            index = key_list.index(id)
            p = x.get(id)
            if p is not None:
               if isinstance(p, str):
                   paths.append(p)
               elif isinstance(p, dict):
                   #
                   next_key = key_list
                   next_key.pop(index)
                   ps = self.path(key_list=next_key)
                   paths.extend(ps)
            pass
        return paths

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, item: str):
        # if isinstance()
        return super().__setitem__(key, item)



class ResourceDict(UserDict):
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
    __slots__ = ["name", "type", "value", "config"]

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


