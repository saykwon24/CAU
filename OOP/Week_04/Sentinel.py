# Week_04 (1)
"""
Sentinel value: serves as a signal for termination of loop, or indicates the end of a data set
                usually use -1 or negative value as the sentinel

Priming read: input operation before a loop
              allows the user to input the first value, so the user can input the first value as the sentinel
Modification read: input operation that modifies a variable inside a loop
                   this is the last statement to be executed before the next iteration of the loop
>>> these are used to read 'sentinel-terminated sequence of values'

a Loop and a Half: the actual test for termination is located in the middle of the loop
"""

# Sentinel by using -1
salary = float(input("Enter a salary or -1 to finish: "))    # priming read, the sentinel is -1
while salary >= 0.0:
    total += salary
    count += 1
    salary = float(input("Enter a salary or -1 to finish: "))    # modification read


# a loop and a half (using boolean variables)
done = False
while not done:
    value = float(input("Enter a salary or -1 to finish: "))
    if value < 0.0:    # actual test for termination
        done = True
        #break
    else:
        continue
