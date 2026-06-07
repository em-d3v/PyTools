"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""


from gui import AppLibraryUI


class DevLib(AppLibraryUI):
    """Development UI"""
  
    
    def __init__(self, master, **kwargs):
        """
        create instance
        """
        super().__init__(master=master,**kwargs)
        
        self.pack(fill="both", expand=True)
        pass
 