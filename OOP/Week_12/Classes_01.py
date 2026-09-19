# Week 12 (1)

"""
Object-Oriented Programming: a programming style in which tasks are solved by collaborating 'objects'
                             each object has its own set of data and set of methods (ex. string, list, and file object)
                             can create your own objects, then you must supply methods for these objects


Class: describes a set of objects with the same behavior
       specifies which methods can be used and how the methods are implemented; defines a specific set of methods
       every class has a 'public interface': a collection of methods through which the objects can be manipulated, together with a description of their behavior
       so all you need to know is which methods you can apply and what these methods do
       when designing a class, start by specifying its public interface (write pseudocodes using comments)
       'encapsulation' makes this possible


Encapsulation: the act of providing a public interface and hiding the implementation of your class
               enables changes in the implementation without affecting users of a class
               so all the user of class need to know is the public interface


Instance Variable: stores the data required for executing the object's methods; i.e. an object stores its data in instance variables (storage location)
                   by convention, its name starts with a single or double underscore(_ or __) to indicate 'private'
                   it is part of implementation details, so should be hidden from the user of the class
                   all instance variables are private, and should be only manipulated or accessed by the methods of its own class
                   unlike other object-oriented languages, Python does not provide a mechanism to explicitly hide or protect private members from outside access
                   so the users do not touch it, and programmers must trust that the class user will not attempt to access them
                   
                   "Make ALL instance vaiables Private, MOST methods Public" - this is an essential part of encapsulation
                   sometimes you have a 'helper method' of other methods, should make it private using underscore(_ or __)


Class Methods: very similar to defining a function with these exceptions:
                    1) method is defined as part of a class definition
                    2) first parameter variable of a method is called 'self'; instance variables must be referenced within a method using the self
               the self parameter variable refers to the objects on which the method was invoked
               no argument can be provided to the method even though the definition includes the self
               
               useful to classify class methods as two types:
                    1) Mutator methods  | changes or modifies the object on which it operates
                    2) Accessor methods | queries the object for some information without changing it, simply returns a value
               
               when implementing a class, you have to determine which data each object needs to store
               it is good idea to start with the accessor methods; go through all methods and consider their data requirements
               for each accessor method, an object must either store the result or the data necessary to compute result
               be sure that your data representation supports method calls in any order
"""

## Models a tally counter whose value can be incremented, viewed, or reset
#
class Counter:
     ## Gets the current value of this counter (accessor)
     # @return the current value
     #
     def getValue(self):    # the self should be passed to class method
          return self._value
     
     ## Advances the value of this counter by 1 (mutator)
     #
     def click(self):
          self._value += 1    # instance variable must be referenced using the self
     
     ## Resets the value of this counter to 0 (mutator)
     #
     def reset(self):
          self._value = 0


tally = Counter()    # create an object of the Counter class
tally.reset()
tally.click()
tally.click()

result = tally.getValue()
print("Value:", result)    # 2

tally.click()
result = tally.getValue()
print("Value:", result)    # 3