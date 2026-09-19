# Week 12 (2)

"""
Constructor: defines and initializes all of the instance variables of an object
             is automatically called whenever an objct is created
             returns a reference to the newly created and initialized object
             first parameter of every constructor must be 'self'
             Python uses the special name '__init__' for constructor, and allows to define only one constructor per class
             
             you can define constructor with default argument values
             after an object has been constructed, you should not directly call the constructor on that object again
             instead, create a new object
             in general, you should never call a Python method that starts with a double underscore(__)
             
             Python does not prevent you from creating instance variables in any method of a class
             constructor is invoked before any method can be called, so any instance variables that were created in the constructor are sure to be available in all methods
             thus, it is better or recommended to create all instance variables in the constructor
             
    [syntax] class ClassName:
                 def __init__(self, param1, param2, ...):
                     [constructor body]


Named Argument: pass arguments in any order by using the parameter's name
                you don't have to name every argument, only for parameter variables that are specified out of order
"""

## A simulated cash register that tracks the item count and the total amount due
#
class CashRegister:
    ## Constructs a cash register with cleared item count and total
    #
    def __init__(self):    # constructor
        self._itemCount = 0
        self._totalPrice = 0.0
    
    ## Adds an item to this cash register
    # @param price the price of this item
    #
    def addItem(self, price):    # self parameter should be listed first
        self._itemCount += 1
        self._totalPrice += price
    
    ## Adds multiple instances of the same item
    # @param quantity 
    # @param price the price of this item
    #
    def addItems(self, quantity, price):
        for _ in range(quantity):
            self.addItem(price)    # should invoke addItem method on the self parameter
                                   # addItem method is invoked on the object referenced by self
    
    ## Gets the price of all items in the current sale
    # @return the total price
    #
    def getTotal(self):
        return self._totalPrice

    ## Gets the number of items in the current sale
    # @return the item count
    #
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0


register1 = CashRegister()
register1.addItem(2.95)    # a reference to the object on which the method was invoked
                           # _itemCount of register1 is incremented, not that of some other CashRegister object
register1.addItems(6, 0.95)
