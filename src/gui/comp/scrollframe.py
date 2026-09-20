"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""
import tkinter as tk
from tkinter import ttk
from typing import Literal

scroll_type = Literal["vertical", "horizontal", "both"]

class ScrollFrame(tk.Frame):
    """
    ScrollFrame
    A scrollable frame widget. Uses Canvas and Scrollbar.
    """
    # member: str
    
    _scroll: scroll_type
    """ type of scroll: vertical, horizontal, or both"""
    _mousewheel_binding: str|None
    canvas:tk.Canvas
    """canvas to hold inner frame"""
    sb_vertical:tk.Scrollbar | None
    """vertical scrollbar"""
    sb_horizontal:tk.Scrollbar | None
    """horizontal scrollbar"""
    inner_frame:tk.Frame
    """
    frame inside canvas to hold widgets.
    
    IMPORTANT:
    DO NOT PACK OR GRID THIS COMPONENT.
    DOING THAT WILL BREAK THE SCROLLING FUNCTION.
    
    """
    
    def __init__(self, master, scrollregion=(0, 0, 100, 100), scroll: scroll_type = "both", **kwds):
        """
        create instance
        """
        super().__init__(master=master, **kwds)
        # private members
        self._scroll = scroll
        
        # gui
        self.canvas = tk.Canvas(self, borderwidth=0, scrollregion=scrollregion)
        
        #scrollbars
        self.sb_horizontal = None
        self.sb_vertical = None
        if self._scroll == "vertical" or self._scroll == "both":
            self.sb_vertical = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.sb_vertical.pack(side="right", fill="y")
            self.canvas.configure(yscrollcommand=self.sb_vertical.set)
        
        if self._scroll == "horizontal" or self._scroll == "both":
            self.sb_horizontal = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
            self.sb_horizontal.pack(side="bottom", fill="x")
            self.canvas.configure(xscrollcommand=self.sb_horizontal.set)
        
        #inner frame (DO NOT PACK)
        self.inner_frame = tk.Frame(master=self.canvas)
        
        self.inner_frame_id = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.canvas.pack(side='left', fill='both', expand=True)
        
        #add bindings
        self.inner_frame.bind("<Configure>", self._on_frame_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        
        # optional bindings
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        pass
    
    def _on_mousewheel(self, event):
        """
        Handle mouse wheel scrolling
        """
           
        if self._scroll == "vertical" or self._scroll == "both":
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        if self._scroll == "horizontal" or self._scroll == "both":
            self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")
            
    def _on_frame_configure(self, event):
        """
        Reset the scroll region to encompass the inner frame
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def _on_canvas_configure(self, event):
        """
        Reset the inner frame's width to fill the canvas
        """
        self.canvas.itemconfig(self.inner_frame, width=event.width)
        
    
    def pack(self, **kwargs):
        """
        pack the scrollframe
        """
        super().pack(**kwargs)
