from Exercises import Fraction

"""
## For exercise 1
def main1():
    f1 = Fraction(3, 4)
    f2 = Fraction(4, 10)
    f3 = Fraction(2, -6)
    f4 = Fraction(0, 10)
    f5 = Fraction(-5, -15)
    #f6 = Fraction(3, 0)      # ZeroDivisionError
    #f7 = Fraction(3.0, 4)    # TypeError
    
    print("Fraction 1:", f1)    # 3/4
    print("Fraction 2:", f2)    # 2/5
    print("Fraction 3:", f3)    # -1/3
    print("Fraction 4:", f4)    # 0/1
    print("Fraction 5:", f5)    # 1/3

if __name__ == "__main__":
    main1()
"""


"""
## For exercise 2
def main2():
    f1 = Fraction(3, 4) * Fraction(4, 10)
    f2 = Fraction(2, -6) * Fraction(0, 10)
    f3 = Fraction(-5, -15) * Fraction(-3, 7)
    f4 = Fraction(3, 4) * 5
    f5 = Fraction(2, -6) * 3
    f6 = Fraction(-5, -15) * 0
    #f7 = Fraction(3, 4) * 5.0    # TypeError
    
    print("Fraction 1:", f1)    # 3/10
    print("Fraction 2:", f2)    # 0/1
    print("Fraction 3:", f3)    # -1/7
    print("Fraction 1:", f4)    # 15/4
    print("Fraction 2:", f5)    # -1/1
    print("Fraction 3:", f6)    # 0/1

if __name__ == "__main__":
    main2()
"""


"""
## For exercise 3
def main3():
    f1 = Fraction(3, 4) * 5
    
    print("Fraction 1:", f1)    # 15/4
    print(str(f1))              # 15/4
                                # first find __str__, if not, __repr__ is called
    print(repr(f1))             # Fraction(15, 4)

if __name__ == "__main__":
    main3()
"""