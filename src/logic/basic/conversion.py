"""
Filename: template.py
Date: MM/DD/YYYY
Author: Elena Miller
Desc:

"""
import tkinter as tk
from tkinter import messagebox, ttk
from typing import Literal, Tuple

from gui.basic import BasicConversion as Gui
from logic import Application
from src.lib import conv
from src.lib.conv import Converter

CONVERSIONS = ["Temperature", "Weight", "Volume", "Distance"]

converters = conv.converters

ComboSelection = Tuple[str, str]
class BasicConversion(Application):
    """class description"""
    settings = {}
    title = "Conversion"
    name = "conversion"
    
    #members
    gui: Gui
    _config: dict[str, any]
    """selections from comboboxes"""
    _conversion: tk.StringVar
    """selected conversion"""
    _converter: Converter
    _units: dict
    _input:any
    _output:any  
    def __init__(self,parent):
        
        """
        create instance
        """
        super().__init__(name="basic_conversion", title="Basic Conversion", gui=Gui(master=parent),enabled=True)
        #private members
        
        self._config = {
            "converter": "",
            "unit": {
                
                "keys":[],
                "codes": [],
                "input": "", 
                "output":"", 
            },
            "values": {
                "input": "", 
                "output": "", 
            }
        }
        
        self._vars = {
            "converter" : tk.StringVar(value=""),
            "unit_in"   : tk.StringVar(value=""),
            "unit_out"  : tk.StringVar(value=""),
            "value_in"  : tk.StringVar(value=""),
            "value_out" : tk.StringVar(value=""),
        }
        
        self._converter     = None
        self._units = {}
        self._values = {
            "unit": [],
            "input": "",
            "output": "",
        }
        self.build()
        pass
        
    def build(self):
        #gui
        gui = self.gui
        self._conversion = tk.StringVar(value="")
        conv_list = list(converters.keys())
        # conv_list.insert(0,"Select Conversion")
        gui.converter_input.configure(values=conv_list, textvariable=self._vars["converter"])
        gui.unit_input_combobox.configure(textvariable=self._vars["unit_in"])
        gui.unit_output_combobox.configure(textvariable=self._vars["unit_out"])
        gui.input_value_box.configure(textvariable=self._vars["value_in"])
        gui.output_value_box.configure(textvariable=self._vars["value_out"])
        # gui.value_input_text.configure(v)
        gui.converter_input.set("Select option")
        gui.converter_input.bind("<<ComboboxSelected>>",self._converter_changed)
        gui.conv_btn.configure(command=self._convert)
        pass

    def show_error(self,msg):
        messagebox.showerror("Error", msg)
    def _converter_changed(self, event):
        """Converter Changed Event

        Args:
            event (evt): ComboboxSelected
        """
        # get units
        selected = self._vars["converter"].get()
        self.gui.converter.configure(text=selected)
        
        self._converter = converters[selected]
        self._units = self._converter.units
        
        self._values["unit"] = list(self._units.keys())
        self.gui.unit_input_combobox.configure(values=self._values["unit"])
        self.gui.unit_output_combobox.configure(values=self._values["unit"])
        pass
    def _convert(self):
        """Do Conversion
        

        Args:
            event (_type_): _description_
        """
        conv = self._vars["converter"].get()
        unit_in = self._vars["unit_in"].get()
        unit_out = self._vars["unit_out"].get()
        # validate unit in and unit_out
        if len(conv) <= 0:
            self.show_error("Please select a converter")
        elif len(unit_in) <= 0 or len(unit_out) <= 0:
            self.show_error("please select unit input and output.")
        else:
            try:
                input = self._vars["value_in"].get()
                self._vars["value_out"].set(input)
            except ValueError:
                self.show_error("wrong value type")
            #must not be empty
            # self._vars["value_out"].set(str(input))
        
        pass
    def _variable(self,name, value=None):
        if name in list(self._vars.keys()):
            if value is not None:
                self._vars[name].set(value)
            else:
                return self._vars[name].get()
        pass
    # def configure(self,name, **kwds):
    #     if name in list(self._config.keys()):
    #         if "value" in kwds.keys():
    #             self._config[name] = kwds["value"]
    #             return
    #         else:
    #             # for key, value in kwds.items():
    #             #     if key in self._config.keys():
    #             #         if 
    #             pass
    #     pass
    def config(self,*args,**kwargs):
        """
        Recursive getter/setter for nested config values.

        *args:
            ("unit", "input")               → GET
            ("unit", "input", value="mm")   → SET

        **kwargs:
            unit={"input": "mm"}            → recursive merge
        """

        # Handle recursive dict updates
        if kwargs:
            self._recursive_merge(self._config, kwargs)
            return self._config

        # Handle recursive get/set via *args
        if args:
            return self._recursive_path(self._config, list(args))

        return self._config
        pass
    def _rec_config(self,current,keys,value):
        # GET: last key
        if len(keys) == 1:
            return current[keys[0]]
        pass


    def _recursive_path(self, current, keys):
       # GET: last key
        if len(keys) == 1:
            return current[keys[0]]

        # SET: last key + value provided via kwargs
        if len(keys) == 2 and isinstance(keys[1], dict):
            # keys[1] is a dict like {"value": something}
            current[keys[0]] = keys[1]["value"]
            return keys[1]["value"]

        # SET: last key + explicit value argument
        if len(keys) == 2:
            # keys = ["unit", {"input": "mm"}] is NOT allowed
            # keys = ["unit", "input"] → GET
            # keys = ["unit", "input", value="mm"] → handled in config()
            raise ValueError("Setter must use keyword argument: value=...")
    def _recursive_merge(self, target, updates):
        for key, value in updates.items():
            if isinstance(value, dict) and isinstance(target.get(key), dict):
                self._recursive_merge(target[key], value)
            else:
                target[key] = value
    