"""
File: rsrc.py
Date: 5/27/26
Author: Elena Miller


"""
import sys as sys
from os import path
import tkinter as tk
DIRECTORY = sys.path[0] + "/resources/"
IMG_DIR = DIRECTORY + "img/"

class Resource:
    _dirs = {
        "image": "img"
    }
    def __init__(self):
        pass
    
    def __call__(self, resType:str, **kwargs):
        """
        call for resource
        """
        if resType in self._dirs:
            match resType:
                case "image":
                    #get image
                    return self._get_image(**kwargs)
                case _: 
                    print("Unknown resource type")
            pass
        pass

    def _get_image(self, **kwargs):
        """
        returns an image
        """
        name = kwargs.get("name")
        p = path.join(sys.path[0], "resources",self._dirs["image"],name)
        image = tk.PhotoImage(file=p)
        return image