# Week 12 (3)

"""
Class Variable: a variable for a value that properly belongs to a class, not to any object of the class; a variable that only in the class
                class variables are declared at the same indentation level as class methods (not in the methods)
                so every object of the class has instance variables, but there is only a single copy of class variables
                
                should always be private to ensure that methods of other classes do not change their values
                however, class constants can be public, so methods of any class can refer to it
"""

class BankAccount:
    _lastAssignedNumber = 1000    # class variable
    OVERDRAFT_FEE = 29.95    # class constant
    
    def __init__(self):
        self._balance = 0
        BankAccount._lastAssignedNumber += 1    # class variable is referenced like this
        self._accountNumber = BankAccount._lastAssignedNumber
        ...
    ...