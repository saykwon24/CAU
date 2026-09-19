# Week_07 (4)
"""
List Methods
    list.append(element)               | append 'element' at the end of 'list'
    list.insert(index, element)        | insert 'element' in 'list' at 'index'th position
                                        'index' must be in valid range
                                        and following elements are move down by 1 and length of list is incremented by 1
    list.index(element, [start, end])  | return the index of 'element' in 'list' from 'start' to 'end'
    list.pop([index])                  | remove 'index'th element and return the list
                                         if no argument is passed, the last element is removed
                                         'index' must be in valid range
    list.remove(element)               | remove the first 'element' and return the list
                                         if there is no 'element' in list, raise ValueError
    list.sort()                        | sort elements of 'list' alphabetically or in ascending order
        >>> https://docs.python.org/3/tutorial/datastructures.html
"""

# index method
friends = ["Harry", "Ron", "Hermione", "Harry", "Emily"]
n1 = friends.index("Harry")
n2 = friends.index("Harry", n1 + 1)
print(n1, n2)    # 0 3



"""
Concatenate and Replicate lists
    1) two or more lists can be concatenated by using '+' operator
    2) same list can be replicated by using '*' operator
       often use to initialize a list with a fixed value

Test lists
    equality: use '==' or '!=' operator
    ....: use 'in' operator


Mathematical functions
    >>> https://docs.python.org/3/library/functions.html
"""

sum([1, 4, 9, 16])    # 30
min("Fred", "Ann", "Sue")    # Ann
max("Fred", "Ann", "Sue")    # Sue



"""
Copying List: by using list() function, can modify either without affecting the other reference of same list
    list(sequence) | return a new 'list' containing all elements of 'sequence'
                     can be used for copying elements of list
                     if 'sequence' is string, elements of 'list' is characters of string
"""

characters = list("Hello")    # ["H", "e", "l", "l", "o"]



"""
Slicing: by using ':' operator, slices work with all sequences
    list[[i]:[j]] | return 'i'th element to 'j - 1'th element of 'list'
                    'i' and 'j' are optional
"""

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
third_quarter = list[6:9]    # [7, 8, 9]
first_half = list[:6]    # [1, 2, 3, 4, 5, 6]
second_half = list[6:]    # [7, 8, 9, 10, 11, 12]

months[:2] = [10, 20, 30]
print(months)    # [10, 20, 30, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                 # size of slice and the replacement do not have to be same
