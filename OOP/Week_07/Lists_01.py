# Week_07 (3)
"""
List: a container that stores a collection of elements that is in 'linear' or sequantial order
      [syntax]
          empty list | variable_name = []
          indexing   | list_name[index]
    
    to initialize, use square bracket
    can access to an element by using subsctipt operator '[]' and list indices start at 0
    'IndexError' (or out-of-range error) when the index is in invalid range
    to avoid IndexError, generally use len() function
    reverse subscript: access to the element in reverse order
                       reverse index == forward index - length of list
                       the range of reverse subscript is between -1 and length of list


string: sequence of characters, immutable(i.e. cannot change characters in sequence)
list:   sequence of any type of values including str, int, float, ... and mutable
        but conventionally, the elements of list are the same type
"""

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[4] == a[-6])    # True
print(a[-11])    # IndexError



"""
Traversing List: visit all elements of list
    1) loop over the 'index'
    2) loop over the 'element'
"""

values = [10, 20, 30, 40, 50]

# loop over the index
for i in range(len(values)):
    print(i, values[i])

# loop over the element
for value in values:
    print(value)



"""
List Reference: location or address of list in memory, specifies the location of list
                copying the reference yields a second reference 'alias' for the first to the same list
                so the value of element can be updated whether using original reference or alias
"""

scores = [10, 9, 7, 4, 5]
values = scores    # copying list reference

values[3] = 10
print(scores[3])    # 10
