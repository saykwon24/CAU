# Week 15 (1)

"""
Big-Oh Notation: describe the growth behavior of a function
    T(n): represents the processing time of an algorithm for a given input of size 'n'
    f(n): is usually chosen to be a simple function (e.g. n^k, log(n), and so on)
    if T(n) grows at a rate that is bounded by f(n), "T(n) = O(f(n))"
    
    
    some notations which describe the growth behavior of a function:
        1) T(n) = O(f(n))
            T grows no faster than f
            formally, for all 'n' larger than some threshold, the ratio "T(n)/f(n) <= C" for some constant C
            e.g. T(n) = n^2 + 5n - 3 can be O(n^3), O(n^10), or so on
        
        2) T(n) = Ω(f(n))
            T grows at least as fast as f
            formally, for all 'n' larger than some threshold, the ratio "T(n)/f(n) >= C" for some constant C
            e.g. T(n) = n^2 + 5n - 3 can be Ω(n^2) or Ω(n)
        
        3) T(n) = Θ(f(n))
            T and f grow at the same rate, this is the most precise description
            both 'T(n) = O(f(n))' and 'T(n) = Ω(f(n))' hold
            e.g. T(n) = n^2 + 5n - 3 is Θ(n^2), but not Θ(n), Θ(n^3), or so on
    
    
    conventionally, it is common to stick with big-Oh
    a table below shows common big-Oh expressions, sorted by increasing growth
    Big-Oh Expression | Name
        O(1)          | Constant
        O(log(n))     | Logarithmic
        O(n)          | Linear
        O(n log(n))   | Log-Linear
        O(n^2)        | Quadratic
        O(n^3)        | Cubic
        O(2^n)        | Exponential
        O(n!)         | Factorial
"""



"""
Insertion Sort: enlarge the initial sequence by inserting the next list element at the proper location
                i.e. append a new element in the sequence and compare the value with other element
                
                assume the size of the list is 'n'
                in this algorithm, we carry out 'n-1' iterations
                in the k-th iteration, 'k' element is already sorted, and need to insert a new element into the sequence
                for each iteration, need to visit the elements of the initial sequence until we have found the location, so 'k+1' elements are visitied
                thus, total number of visits == 2 + 3 + ... + n = n(n-1)/2 - 1
                insertion sort is an O(n^2) algorithm
"""

## Sorts a list, using insertion sort
# @param values the list to sort
#
def insertionSort(values):
    for i in range(1, len(values)):
        next = values[i]
        
        # Move all larger elements up
        j = i
        while j > 0 and values[j - 1] > next:
            values[j] = values[j - 1]
            j -= 1
        
        # Insert the element
        values[j] = next
