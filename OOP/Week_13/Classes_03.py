# Week 13 (1)

"""
Unit test: test your code in isolation before integrating it to a complete program
           use an environment for interactive testing (on simple code) or write a tester program to execute test (on complex code)
           when you use the latter method, need to import the class you are testing into the tester program
           tester program typically carries out the following steps:
               1) Construct objects that is being tested
               2) Invoke methods
               3) Print out results
               4) Print the expected results
"""

class CashRegister:
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
        
    def addItem(self, price):
        self._itemCount += 1
        self._totalPrice += price
    
    def addItems(self, quantity, price):
        for _ in range(quantity):
            self.addItem(price)

    def getTotal(self):
        return self._totalPrice

    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0


## Unit test for above class
# Import the calss you are testing
"""from cashregister import CashRegister"""
# Construct an object
reg1 = CashRegister()
# Invoke the methods
reg1.addItem(1.95)
reg1.addItem(0.95)
reg1.addItem(2.50)
# Print out the result
print(reg1.getTotal())
# Print the expected result
print("Expected: 5.40")



"""
Object reference: a variable does not hold an object, but hold the 'memory location' of it
                  constructor returns a reference to the new object, and that reference is stored in the variable

1) Shared reference: multiple object variables can contain references to the same object
                     e.g. by assigning or copying one to the other
                     variables that refer to the same object are known as 'aliases'
                     you can easily test whether two variables are alises using 'is' operator
                     is operator checks whether the variables are alises or not

2) None reference: if object reference refers to no object at all, it has the special value 'None'
                   it is an error to invoke a method on a None reference (AttributeError)

3) Self reference: every method has a reference to the object on which the method was invoked, stored in the self parameter variable
                   self refers to the same object as the object variable, so it is initialized with the reference
                   self reference is used to access instance variables of the object
                   can also invoke a method on self, and sometimes pass self to another method


The Lifetime of objects: when you construct an object with a constructor, the object is created, and the self variable of the constructor is set to the memory location of the object
                         initially, object contains no instance variables
                         constructor executes adding instance variables to the object and exit
                         when the constructor exits, it returns a reference to the object
                         the object stays alive as long as there is at least one reference to it
                         when it is no longer referenced, it is removed by a part of the virtual machine called 'garbage collector'
"""

## Shared reference
reg2 = reg1
if reg1 is reg2: print("The variables are aliases")
if reg1 is not reg2: print("The variables refer to different objects")

## None reference
reg = None
print(reg.getTotal())    # Error
