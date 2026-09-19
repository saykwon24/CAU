# Week_05 (2)
"""
Function: a block of instructions
    we can 'call' a function to execute its instructions
    when we call a function, we can 'pass' arguments or not(zero argument)
    the output that a function computes is 'return value'
    functions can receive multiple arguments, but only one return value
    return value of a function is returned to the point where the function was called
    
    [syntax] def funcName(param1, param2, ...):    [function header]
                 statements                        [function body]
                 return returnValue -> [optional]
        function body should be indented to the same level
        return | a keyword that terminates a function call immediately and yields the function result


Producing program output: 'side effect', such as using print() function
                          not same as returning value


round(number, ndigits=None) | return 'number' rounded to 'ndigits' precision after the decimal point
                              if 'ndigits' is omitted or is None, return the nearest integer to its input
"""

# implementing a function
def cubeVolume(sideLength):
    return sideLength ** 3

# testing the funciton
result1 = cubeVolume(2)
result2 = cubeVolume(10)
print("A cube with side length 2 has volume", result1)
print("A cube with side length 10 has volume", result2)



"""
Programs that contain functions: it is good to place all statements into main() function
                                 the function's name we conventionally use is 'main'
                                 it is also good to use 'comments' that explain a behavior of the statements
                                 >>> c.f. https://www.doxygen.org
"""

def main():    # caller
    result = cubeVolume(2)    # jump to cubeVolume() function
    print("A cube with side length 2 has volume", result)

def cubeVolume(sideLength):    # callee
    "Computes the volume of a cube"    # docstring
    return sideLength ** 3

# now, compiler knows main() and cubeVolume() functions

main()    # call main() function



"""
Argument(Actual Parameter): values that are supplied to a function that is called
Parameter(Formal Parameter): variables that hold the arguments supplied when a function is called
                             can modify the values of the parameter variable, but we don't
                             instead, introduce a separate variables

>>> each parameter variable is initialized with the corresponding argument
    actually, the variable passed into function is 'copied' value
"""

# Parameter Passing
result1 = cubeVolume(2)
    #1) new parameter variable 'sideLength' is created when the function is called
    #2) the parameter variable is initialized with argument '2'
    #3) the function computes the expressions
    #4) the function returns return value, and all of its values are removed
    #5) return value is transferred to the caller
    #6) the caller puts the return value in the variable 'result1'


# Common Error: Trying to modify arguments
def addTax(price, rate):
    tax = price * rate / 100
    price += tax    # no effect outside the function because the arguments are copied value
    return tax
