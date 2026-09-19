## Defines an immutable rational number with common arithmetic operations.
#
class Fraction :
    ## Constructs a rational number initialized to zero or a user specified value.
    # @param numerator the numerator of the fraction (default is 0)
    # @param denominator the denominator of the fraction (cannot be 0)
    #
    def __init__(self, numerator = 0, denominator = 1) :
        # The numerator and denominator must be integers.
        if (not isinstance(numerator, int)) or (not isinstance(denominator, int)):
            raise TypeError("Numerator and denominator must be integers.")
        
        # The denominator cannot be zero.
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        # If the rational number is zero, set the denominator to 1.
        if numerator == 0:
            self._numerator = 0
            self._denominator = 1
        
        # Otherwise, store the rational number in reduced form.
        else:
            # Determine the sign.
            if (numerator * denominator < 0):
                sign = -1
            else:
                sign = 1
            
            # Reduce to smallest form.
            a = abs(numerator)
            b = abs(denominator)
            while (a % b != 0):
                tempA = a
                tempB = b
                a = tempB
                b = tempA % tempB
            
            self._numerator = abs(numerator) // b * sign
            self._denominator = abs(denominator) // b
        
    
    # Multiplies this fraction by the given value.
    # @param rhsValue the value to multiply by (an int or Fraction)
    # @return the product as a Fraction
    #
    def __mul__(self, rhsValue):
        # Check whether the right side value is int or Fraction
        if isinstance(rhsValue, int):
            rhsValue = Fraction(rhsValue, 1)    # rhsValue/1
        elif not isinstance(rhsValue, Fraction):
            raise TypeError("Can only multiply by int or Fraction")
        
        num = self._numerator * rhsValue._numerator
        den = self._denominator * rhsValue._denominator
        
        return Fraction(num, den)    # becasue the reduction is in the constructor of Fraction class
    
    
    ## Gets a string representation of the fraction.
    # @return a string in the format #/#
    #
    """
    def __str__(self):
        return str(self._numerator) + "/" + str(self._denominator)
    """
    
    # Returns an unambiguous string representation of this fraction.
    def __repr__(self):
        return "Fraction(%d, %d)" % (int(self._numerator), int(self._denominator))
        #return f"Fraction({self._numerator}, {self._denominator})"
