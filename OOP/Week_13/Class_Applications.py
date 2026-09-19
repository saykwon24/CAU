# Week 13 (2)

"""
Special methods: can define and implement methods that will be called automatically when a standard Python operator(+,-,*,/,...) is applied to an instance of a class
                 their names begine and end with two underscores (i.e. __name__)
                 should not directly call them, but instead use the corresponding operator or function
                 should only define operators when the operator has a meaningful purpose
      <Expression>   |              <Method Name>            |<returns>|         <Description>
    x + y            | __add__(self, y)                      | object  | Addition
    x - y            | __sub__(self, y)                      | object  | Subtraction
    x * y            | __mul__(self, y)                      | object  | Multiplication
    x / y            | __truediv__(self, y)                  | object  | Real division
    x // y           | __floordiv__(self, y)                 | object  | Floor division
    x % y            | __mod__(self, y)                      | object  | Modulus
    x ** y           | __pow__(self, y)                      | object  | Exponentiation
    x == y           | __eq__(self, y)                       | Boolean | Equal
    x != y           | __ne__(self, y)                       | Boolean | Not equal
    x < y            | __lt__(self, y)                       | Boolean | Less than
    x <= y           | __le__(self, y)                       | Boolean | Less than or equal
    x > y            | __gt__(self, y)                       | Boolean | Greater than
    x >= y           | __ge__(self, y)                       | Boolean | Greater than or equal
    -x               | __neg__(self)                         | object  | Unary minus
    abs(x)           | __abs__(self)                         | object  | Absolute value
    float(x)         | __float__(self)                       | float   | Convert to a floating-point value
    int(x)           | __int__(self)                         | integer | Convert to an integer value 
    str(x), print(x) | __str__(self) and then __repr__(self) | string  | Convert to a readable string
    repr(x)          | __repr__(self)                        | string  | Convert to a readable string
    x = className()  | __init__(self)                        | object  | Constructor
    


Object types and instances: you can check the type of object referenced by a variable by using 'isinstance' function
                            also allow for different actions depending on the type

[syntax] isinstance(object, type) | return True if the object referenced by 'object' is an instance of the data type indicated by 'type'
                                    'type' can be any built-in type or the name of user-defined class
>>> https://docs.python.org/3/library/functions.html#isinstance


ex) computers cannot store some real numbers precisely, you can use rational numbers to store exact values
    rational number is a ratio of two integers, numerator and denominator
"""

class Fraction:
    ## Constructs a rational number initialized to zero or a user specified value
    # @param numerator the numerator of the fraction (default is 0)
    # @param denominator the denominator of the fraction (cannot be zero, default is 1)
    #
    def __init__(self, numerator=0, denominator=1):
        # Check the type of numerator and denominator whether is integer or not
        if (not isinstance(numerator, int)) or (not isinstance(denominator, int)):
            raise TypeError("The numerator and denominator must be integers.")
        
        # The denominator cannot be zero
        if denominator == 0: raise ZeroDivisionError("Denominator cannot be zero.")
        
        # If the rational number is zero, set the denominator to 1
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        # Otherwise, store the rational number in reduced form
        else:
            # Determine the sign
            if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
                sign = -1
            else: 
                sign = 1
        
            # Reduce to smallest form
            a = abs(numerator)
            b = abs(denominator)
            while (a % b != 0):
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            
            self._numerator = abs(numerator) // b * sign
            self._denominator = abs(denominator) // b
    
    
    "** Special Methods **"
    ## Adds a fraction to this fraction
    # @param rhsValue the right-hand side fraction
    # @return a new Fraction object resulting from the addition
    #
    def __add__(self, rhsValue):
        # Check the type of argument which is on the left side of '+' operator 
        if isinstance(rhsValue, int):
            rhsFrac = Fraction(rhsValue, 1)
        elif isinstance(rhsValue, Fraction):
            rhsFrac = rhsValue
        else:
            raise TypeError("Argument must be an int or Fraction object.")
        
        # Reduction to common denomination
        num = (self._numerator * rhsFrac._denominator + self._denominator * rhsFrac._numerator)
        den = self._denominator * rhsFrac._denominator
        
        return Fraction(num, den)
    
    
    ## Subtracts a fraction from this fraction
    # @param rhsValue the right-hand side fraction
    # @return a new Fraction object resulting from the subtraction
    #
    def __sub__(self, rhsValue):
        # Reduction to common denomination
        num = (self._numerator * rhsValue._denominator - self._denominator * rhsValue._numerator)
        den = self._denominator * rhsValue._denominator
        return Fraction(num, den)
    
    
    ## Some other special methods
    def __eq__(self, rhsValue):    # ==
        return(self._numerator == rhsValue._numerator and self._denominator == rhsValue._denominator)
    
    def __float__(self):    # convert to float
        return self._numerator / self._denominator
    
    def __repr__(self):    # convert to string
        return str(self._numerator) + "/" + str(self._denominator)
    
    def __lt__(self, rhsValue):    # <
        return (self._numerator * rhsValue._denominator < self._denominator * rhsValue._numerator)
    
    ...


## Create objects
frac1 = Fraction(1, 8)      # 1/8
frac2 = Fraction(-2, -4)    # 1/2
frac3 = Fraction(-2, 4)     # -1/2
frac4 = Fraction(3, -7)     # -3/7
frac5 = Fraction(0, 15)     # 0
#frac6 = Fraction(8, 0)      # ZeroDivisionError


## Special Methods
if frac1 == frac2:    # <=> frac1.__eq__(frac2)
    print("The fractions are equal.")
print(float(frac1))    # <=> frac1.__float__()
print(str(frac1))    # <=> frac1.__repr__()


## Arithmetic Operations
newFrac = frac1 + frac2    # <=> frac1.__add__(frac2)


## Object types and Instances: isinstance() function
frac = Fraction(2, 3)
newFrac = frac + 5    # <=> frac1.__add__(5)
print(newFrac)