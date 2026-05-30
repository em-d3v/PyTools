"""
Filename: template.py
Date: 05/13/2026
Author: Elena Miller
Desc:

"""

from typing import List


class Annuity:
    """Annuity class"""
    _amt    :float
    _rate   :float
    _term   :float
    _error  :str
    _config :dict
    # lists
    
    _bbal   :List[float]
    _intr   :List[float]
    _ebal   :List[float]
    
    def __init__(self, amount:float=0.0,rate=0.0,term=0.0):
        """
        create instance of Annuity
        Args:
            amount
        """
        self.amount(amount)
        self.rate(rate)
        self.term(term)
        pass
    
    def amount(self, value:float|None = None)->float|None:
        """
        Getter/Setter Method
        value(float|None): 
            if value is empty => Return value
            if value is not Empty => set value to member
        """
        if value == None:
            return self._amt
        else:
            self._amt = value
            pass
    
    def rate(self, value:float|None = None)->None|float:
        """
        Getter/Setter Method for rate
        value(float|None): 
            if value is empty => Return value
            if value is not Empty => set value to member
        """
        if value == None:
            return self._rate
        else:
            self._rate = value
            pass
    
    def term(self, value:float|None = None)->None|float:
        """
        Getter/Setter Method
        value(float|None): 
            if value is empty => Return value
            if value is not Empty => set value to member
        """
        if value == None:
            return self._amt
        else:
            self._amt = value
            pass
    def error(self):
        return self._error
    
    
    
    
    def valid(self):
        """
        checks validity of members
        """
        
        if self._amt <= 0:
            self._error = "Amount must be positive"
            valid = False
        if self._rate <= 1 or self._rate > 25:
            self._error = "Rate is out of bounds: 1 to 25 only"
            valid = False
        if self._term <= 0:
            self._error = "Term must be positive"
            valid = False
        return valid
    
    def getFVA(self):
        return self._ebal[self._term-1]
    def getFVATotInt(self):
        return self._ebal[self._term-1] - (self._amt * self._term)
    def getFVAInt(self, mo):
        return self._intearn[mo-1] 
    def getFVABbal(self,mo):
        #month requested is assumed to be 1 to (including) term
        return self._bbal[mo-1]
    def getFVAEbal(self,mo):
        return self._ebal[mo-1]
    
    def build(self):
        #create all values needed for annuity schedule
        #first: 3 lists to store column values
        
        self._bbal = [0] * self._term
        self._intr = [0] * self._term
        self._ebal = [0] * self._term
        
        self._bbal[0] = 0
        morate = self._rate / 12 / 100 #monthly rate in fractional form
        for i in range(0, self._term):
            if i > 0:
                self._bbal[i] = self._ebal[i-1]
                
            self._intearn[i] = (self._bbal[i] + self._amt) * morate
            self._ebal[i] = self._bbal[i] + self._amt + self._intearn[i]
    