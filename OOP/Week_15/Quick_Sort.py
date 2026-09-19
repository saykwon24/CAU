# Week 15 (3)

"""
Quick Sort: divide a sequence into two partitions based on a 'pivot' which is a boundary or standard element
            a simplest way is to set the first element as the pivot (there are several variations)
            i.e. elements of first partition < pivot, elements of second partition >= pivot
            compare the elemnts of each partition with the pivot
            sort each partition by recursively applying the same algorithm, and then merge the partitions into a single sorted sequence
            
            like merge sort, based on the strategy of divide and conquer
            unlike merge sort, may divide the sequence into partitions unequally and merge the partial results
            
            on average, quick sort algorithm is an O(n log(n)) algorithm
            its worst-case run-time behavior is O(n^2)
            if the pivot element is chosen as the first element of the region, that worst-case behavior occurs when the input set is already sorted
"""

def quickSort(values, start, to):
    if start >= to: return
    
    # Index of pivot
    p = partition(values, start, to)
    
    # Sort each partition recursively
    quickSort(values, start, p)
    quickSort(values, p+1, to)


def partition(values, start, to):
    # Set the first element of values as pivot
    pivot = values[start]
    i = start - 1
    j = to + 1
    
    while i < j:
        # Compare elements of first partition with pivot by keeping incrementing i
        i += 1
        while values[i] < pivot:
            i += 1
        
        # Compare elements of second partition with pivot, by keeping decrementing j
        j -= 1
        while values[j] > pivot:
            j -= 1
        
        # When the element of first partition is larger than that of second, swap two elements
        if i < j:
            temp = values[i]
            values[i] = values[j]
            values[j] = temp
        
    # Return the index of pivot
    return j
    