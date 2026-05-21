"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller

"""
import sys
class Logger:
    """A simple logger class that writes log messages to a file."""
    def __init__(self, log_file:str):
        self.filepath = log_file
        self.options = {
            'append': True
        }
    
    def log(self, message:str):
        """Write a log message to the file."""
        with open(self.filepath, 'a') as f:
            f.write(message + '\n')