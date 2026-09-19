# Week 14 (2)

"""
Selection Sort: repeatedly finding the smallest element of the unsorted 'tail' region and moving it to the front
                to measure the running time of this algorithm, use time() function of time module
                this function returns the elapsed time since midnight at the start of January 1, 1970
"""

from random import randint
from time import time


## Sorts a list, using selection sort
# @param values the list to sort
#
def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values, i)
        
        # Swap the two elements
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp


## Finds the smallest element in a tail range of the list
# @param values the list to sort
# @param start the first position in values to compare
# @return the position of the smallest element in the range values[start], ..., values[len(values) - 1]
#
def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] < values[minPos]:
            minPos = i
        
    return minPos


## Unit test
def test():
    n = 20
    values = []
    for _ in range(n): values.append(randint(1, 100))
    
    # Before sorted
    print(values)
    selectionSort(values)
    # After sorted
    print(values)

test()
print()


## Measuring the running time of selection sort algorithm
def measure():
    n = int(input("Enter list size: "))
    
    values = []
    for _ in range(n): values.append(randint(1, 100))
    
    # Measure the start time
    startTime = time()
    selectionSort(values)
    # Measure the end time
    endTime = time()
    
    print("Elapsed time: %.3f seconds" % (endTime - startTime))

measure()



"""
Analyzing the performance of selection sort algorithm
    for simplicity, simply count how often a list element is visited
    assume that the number of list element is 'n'
    for each i-th iteration(visit), two elements(smallest and i-th element) are always visited
    n, n-1, n-2, ..., 2 elements are visited as the step is increased
    so the total number of visits is as follows:
        {n + (n-1) + ... + 2} + (n-1)*2 = 0.5n^2 + 2.5n - 3
    as n is increased, the 1st order and constant term can be ignored
    as a result, the number of comparisons increases fourfold when the list size 'n' is doubled
    this is indicated as 'big-Oh' notation: 'O(n^2)'

    selection sort is O(n^2) algorithm
    doubling the data set means a fourfold increase in processing time
"""