"""
File: rsrc.py
Date: 5/27/26
Author: Elena Miller


"""
import importlib.resources as res
import sys as sys
import tkinter as tk
from os import path
from tkinter import ttk
from typing import Any, List, Literal

DIRECTORY = path.join(sys.path[0], "resources") 
IMG_DIR = DIRECTORY + "img/"
ResourceTypes = ["file", "image", "text"]
ResourceType = Literal["image","text","file"]
ImageType = Literal["icon"]
paths = {
    "root": DIRECTORY,
    "image": {
        "root": "img",
        "icon": "icons",
    },
    "text": "txt",
}
dirs = {
    "root": DIRECTORY,
    "image":"img",
    "text":"txt"
}
extensions = {
    "image": [".png", ".jpg", ".jpeg", ".gif"],
    "text": [".txt", ".md", ".csv"],
    "file": []
}
class Rsource:
    """ Resource Class
    Used for Getting Resources from the resources directory
    """
    def __init__(self):
        """ Create Resource Object
        
        """
        self._value = None
         
        pass
    
    def __call__(self, type:ResourceType, src:str=None, **kwargs):
        """
        call for resource
        Args:
            type(ResourceType): type of resource
            
        """
        resource = None
        print(f"Resource: getting resource of type: {type} with src: {src}")
        
        if type in ResourceTypes:
            match type:
                case "image":
                    #get image
                    gui= kwargs.get("gui",False)
                    return self.image(src=src, gui=gui)
                case "text":
                    #get text (string or string list)
                    string = kwargs.get("string", False)
                    return self.text(src=src,string=string)
                case "file":
                    #get file
                    return self.file(src=src)
                case _: 
                    #check if the resource exists in the resources directory
                    print(f"Resource: Unknown resource type: {type}")
                    
                    pass
        return None
    
    
    """ -------------------- Static Methods --------------------"""
    @staticmethod
    def Path(src:str|None,*args):
        """
        Get path for resource
        Args:
            
        """
        if src is not None:
            resourcePath = path.join(src, *args)
        else:
            resourcePath = path.join(sys.path[0], "resources", *args)
        return resourcePath
    @staticmethod
    def File(*args):
        """ Gets Resource File
        
        """
        
        filepath = Resource.Path(src=None, *args)
        return res.files(filepath)
    @staticmethod
    def Get(type: ResourceType, src:str=None, **kwargs):
        """
        get resource
        Args:
            type(ResourceType): type of resource
            src(str): source path
            kwargs: arguments for resource
        """
        resource = None
        #check if resource
        match type:
            case "image":
                #get args
                img = kwargs.get("src")
                
                img_path = None
                if img is not None:
                    img_path = path.join(sys.path[0], "resources", paths["image"], img)
                    pass
                resource = res.files
            case _:
                print("Unknown resource type")
                resource = None
        return resource
    @staticmethod
    def Text(src:str, string:Literal["single","multi",False]=False):
        pass
    """ -------------------- Public  Methods -------------------- """
    def type(self, src:str):
        """
        get resource type
        Args:
            src(str): source path
        """
        ext = path.splitext(src)[1]
        for type, exts in extensions.items():
            if ext in exts:
                return type
        return "unk"
    def info(self, src: str):
        """
        get resource info
        Args:
            src(str): source path
        """
        info = {
            "src": src,
            "type": "unk"
        }
        p = path.join(sys.path[0], "resources", src)
        return info
    def path(self, src:str=None, *args):
        """
        get path for resource
        checks if the resource can be found in the resources directory and returns the path to it
        Args:
            type(ResourceType): type of resource (Resources are separated into types for organization)
                - image
                - text
                - file
            src(str): source path
        """
        p = None
        # if
        return p
    def file(self, src):
        """
        get file
        Args:
            src(str): source path
        """
        file_path = path.join(sys.path[0], "resources", src)
        return res.files(file_path)
    
    def text(self, src, string:Literal["single","multi",False]=False):
        """
        get text
        Args:
            src(str): source path
            string(bool): 
                        if single return file as single string, 
                        if multi -> return file as list of strings,
                        else returns file
        """
        text_path = path.join(sys.path[0], "resources", paths["text"], src)
        text = None
        if string is not False:
            if string == "single":
                #return single string
                text = ""
                with open(text_path, "r") as f:
                    for line in f:
                        text += line.strip()
            elif string == "multi":
                text = []
                with open(text_path, "r") as f:
                    for line in f:
                        text.append(line.strip())
            return text
        else:
            return res.files(text_path)
        
    
    def get(self, type:ResourceType, **kwargs):
        """
        get resource
        Args:
            type(ResourceType): type of resource
            kwargs: arguments for resource
        """
        resource = None
        match type:
            case "image":
                #get args
                img = kwargs.get("src")
                img_path = None
                if img is not None:
                    img_path = path.join(sys.path[0], "resources", paths["image"], img)
                    pass
                resource = res.files
            case _:
                print("Unknown resource type")
                resource = None
        return resource
    
    def image(self,src, gui=False  ) -> tk.PhotoImage| Any:
        """
        returns an image or the image file
        """
        image = None
        
        if gui==True:
            
            p = path.join(sys.path[0], dirs["root"],dirs["image"], src)
            image = tk.PhotoImage(file=p)
        else:
            image = self.file(path.join(dirs["image"], src))
        return image