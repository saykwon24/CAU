# Week 15 (2)

"""
Merge Sort: sorts a sequence by cutting it in half, recursively sorting each half, and then merging the sorted halves
            merge the two sorted lists into one sorted list, by taking a new element from either the first or the second sublist, and choosing the smaller of the elements each time
            carries out dramatically fewer steps than the selection sort, so more efficient algorithm than selection sort


Analyzing Merge Sort
    1) consider the merge process
        assume the size of the list is 'n' and first and second half have been sorted
        each step in the merge process appends one more element to the list
        we can count 3 visits(one for first half, one for second half, and one for the list) per element, or '3n' visits total
        moreover, at the beginning, had to copy from the list to first and second half, resulting another '2n' visits
        thus, total number of visits is '5n'
    
    2) consider the sort process
        assume T(n) == the number of visits required to sort a range of n elements, and n == 2^m (it turns out that this does not affect the result)
        T(n) == T(n/2) + T(n/2) + 5n
        T(n/2) == T(n/4) + T(n/4) + 5n/2 --> T(n) == 2*2*T(n/4) + 2*5n
        T(n/4) == T(n/8) + T(n/8) + 5n/4 --> T(n) == 2*2*2*T(n/8) + 3*5n
        ...
        T(n/(2^k)) == 2*T(n/(2^k+1)) + 5n/(2^k) --> T(n) == (2^k)*T(n/(2^k)) + 5nk = n + 5log2(n)
    
    therefore, merge sort is an O(n log(n)) algorithm and n log(n) function grows much more slowly than n^2
    so merge sort is efficient algorithm than selection sort
"""

## Sorts a list, using merge sort
# @param values the list to sort
# 
def mergeSort(values):
    if len(values) <= 1: return
    
    mid = len(values) // 2
    first = values[:mid]
    second = values[mid:]
    
    mergeSort(first)
    mergeSort(second)
    mergeLists(first, second, values)


## Merges two sorted lists into a third list
# @param first the first sorted list
# @param second the second sorted list
# @param values the list into which to merge first and second
# 
def mergeLists(first, second, values):
    iFirst = 0     # Next element to consider in the first list
    iSecond = 0    # Next element to consider in the second list
    j = 0          # Next open position in values
    
    # As long as neither iFirst nor iSecond is past the end, move the smaller element into values
    while (iFirst < len(first)) and (iSecond < len(second)):
        if first[iFirst] < second[iSecond]:
            values[j] = first[iFirst]
            iFirst += 1
        else:
            values[j] = second[iSecond]
            iSecond += 1
        j += 1
    
    # Note that only one of the two loops below copies entries
    # Copy any remaining entries of the first list
    while iFirst < len(first):
        values[j] = first[iFirst]
        iFirst += 1
        j += 1
    
    # Copy any remaining entries of the second list
    while iSecond < len(second):
        values[j] = second[iSecond]
        iSecond += 1
        j += 1
