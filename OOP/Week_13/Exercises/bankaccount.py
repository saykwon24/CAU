##
# This module defines a class that models a bank account
#
## A bank account has a balance that can be changed by deposits and withdrawals
#
class BankAccount:
    ## Constructs a bank account with a given balance
    # @param initialBalance the initial account balance (default = 0.0)
    #
    def __init__(self, initialBalance=0.0):
        self._balance = initialBalance
    
    
    ## Deposits money into this account
    # @param amount the amount to deposit
    #
    def deposit(self, amount):
        self._balance += amount
    
    
    ## Makes a withdrawal from this account, or charges a penalty if sufficient funds are not available
    # @param amount the amount of the withdrawal
    #
    def withdraw(self, amount):
        if self._balance < amount:
            self._balance -= 10
        else:
            self._balance -= amount
    
    
    ## Adds interest to this account
    # @param rate the interest rate in percent
    #
    def addInterest(self, rate):
        self._balance *= 1 + (rate * 0.01)
    
    
    ## Gets the current balance of this account
    # @return the current balance
    #
    def getBalance(self):
        return self._balance