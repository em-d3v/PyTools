"""
Filename: csettings.py
Date: 05/13/2026
Author: Elena Miller

"""
from typing import List

class Settings:
    """
    Settings Class
    base class for all settings (Gui, App, etc)
    """
    def __init__(self):
        self._data :List[(str, object)] = []
        
    def get(self, id:str):
        """
        Get setting value by id
        """
        for item in self._data:
            if item[0] == id:
                return item[1]
        return None
    def set(self, id:str, value:object):
        """ 
        Set setting value by id
        """
        for i, item in enumerate(self._data):
            if item[0] == id:
                self._data[i] = (id, value)
                return
        self._data.append((id, value))
        #end
        
    def delete(self, id:str):
        """
        Delete setting by id
        """
        self._data = [item for item in self._data if item[0] != id]
        #end
    def all(self):
        """
        Get all settings
        """
        return self._data
    