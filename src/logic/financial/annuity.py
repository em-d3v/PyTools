"""
Filename: Annuity.py
Date: 05/13/2026
Author: Elena Miller

"""

class Annuity:
    """ Annuity Calculator """
    #Constructor for Class
    
    def __init__(self, amount:float=0.0, rate:float=0.0, term:int=0):
        #create 'private' variables for the class values
        self.setAmt(amount)
        self.setRate(rate)
        self.setTerm(term)
        self._error = ""
        if self.isValid():
            self.buildAnnuity()

    #set and get methods 'encapsulate' data values
    def setAmt(self,value):
        self._amt = value

    def getAmt(self):
        return self._amt
    def setRate(self,value):
        self._rate = value

    def getRate(self):
        return self._rate
    def setTerm(self,value):
        self._term = value

    def getTerm(self):
        return self._term

    def isValid(self):
        valid = True
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
    
    def getError(self):
        return self._error
    def buildAnnuity(self):
        #create all values needed for annuity schedule
        #first: 3 lists to store column values
        
        self._bbal = [0] * self._term
        self._intearn = [0] * self._term
        self._ebal = [0] * self._term

        self._bbal[0] = 0
        morate = self._rate / 12 / 100 #monthly rate in fractional form
        for i in range(0, self._term):
            if i > 0:
                self._bbal[i] = self._ebal[i-1]
                
            self._intearn[i] = (self._bbal[i] + self._amt) * morate
            self._ebal[i] = self._bbal[i] + self._amt + self._intearn[i]

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
    
