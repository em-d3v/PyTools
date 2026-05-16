"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller

"""

class Tool:
    """A base class for tools in the application."""
    def __init__(self, name:str):
        self.name = name
        self.settings = {}
        