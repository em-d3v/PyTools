"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""

from gui import AppLibraryUI


class DevLib(AppLibraryUI):
    """Development UI"""
  
    
    def __init__(self):
        """
        create instance
        """
        super().__init__()
        
        self.pack(fill="both", expand=True)
        pass
 