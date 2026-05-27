"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller

"""

class Tool:
    
    """A base class for tools in the application."""
    
    
    SINGLE = "single" # tool is a single function
    MULTI = "multi"   # tool is a collection of functions
    def __init__(self, name:str):
        self.name = name
        self.settings = {}
        