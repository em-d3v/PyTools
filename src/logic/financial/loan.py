"""
Loan Calculator Module
Author: Elena Miller
Date Created: 5/13/2026

"""

# Loan by Elena Miller

class Loan:
    """ Loan Calculator """
    def __init__(self, a=0.0, r=0.0, t=0):
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error = ""
        if self.isValid():
            self.buildLoan()
            
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
    def buildLoan(self):
        self._bbal = [0] * self._term
        self._intchar = [0] * self._term
        self._ebal = [0] * self._term
        
        self._bbal[0] = self._amt
        self._totInt = 0.0
        morate = self._rate / 12 / 100 #monthly rate in fractional form
        self._mopmt = (morate + (morate / ((((1+morate) ** self._term)-1)))) * self._amt
        for i in range(0, self._term):
            if i > 0:
                self._bbal[i] = self._ebal[i-1]
                
            self._intchar[i] =  self._bbal[i] * morate
            self._ebal[i] = (self._bbal[i] + self._intchar[i] - self._mopmt)
            self._totInt += self._intchar[i]
        
    def getLNMoPmt(self):
        return self._mopmt
    def getLNTotInt(self):
        return self._totInt
    def getIntChg(self, mo):
        return self._intchar[mo-1]
    def getLNBbal(self,mo):
        return self._bbal[mo-1]
    def getLNEbal(self,mo):
        return self._ebal[mo-1]
        
