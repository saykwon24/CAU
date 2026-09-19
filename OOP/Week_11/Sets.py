# Week 11 (2)

"""
Set: container that stores a collection of unique values; i.e. cannot store duplicated element
     elements are not stored in any particular order, but rather the order of elements depends on how they are stored internally
     to display the elements in sorted or alphabetically order, use sorted() function
     elements cannot be accessed by position or index
     you can use len() function, in operator, not in operator, and so on
     
    [syntax] setName = set()
             setName = {element1, element2, ...}
        to create an empty set, you should use set() function with no args, not just curly braces({})
        curly braces mean an empty dictionary, not a set


sorted(iterable, key=None, reverse=False) | return a new sorted list from the items in 'iterable'
    >>> https://docs.python.org/3.14/library/functions.html#sorted
"""

# Create an empty set
cast = set()

# Create a set with elements
cast = {"Luigi", "Gumbys", "Spiny"}    # using curly braces
names = ["Luigi", "Gumbys", "Spiny"]
cast = set(names)    # using set() function


# How to access the elements by using for loop
for character in cast: print(character)

# Display the elements in sorted order
for character in sorted(cast): print(character)



"""
Some method for set: because sets are mutable, you can add or remove elements
    set.add(element)     | add 'element' to 'set' if 'element' is not already contained
                           nothing changes if 'element' exists
    set.discard(element) | remove 'element' from 'set' if 'element' is not already contained
                           nothing changes if 'element' exists
    set.remove(element)  | same as discard() method, except raise an exception if 'element' exists
    set.clear()          | remove all elements of 'set'
    set.issubset(SET)    | return True if 'set' is a subset of 'SET' (i.e. 부분집합)
    set.union(s)         | return a set which contains all of the elements from both 'set' and 's' (i.e. 합집합)
    set.intersection(s)  | return a set which contains all of the elements that are in both 'set' and 's' (i.e. 교집합)
    set.difference(s)    | return a set which contains those elements in 'set' that are not in 's' (i.e. 차집합)
>>> https://www.w3schools.com/python/python_ref_set.asp
"""

cast.add("Arthur")
cast.discard("The Colonel")
#cast.remove("The Colonel")    # raise an exception
cast.clear()


canadian = {"Red", "White"}
british = {"Red", "Blue", "White"}
italian = {"Red", "White", "Green"}
French = {"Red", "White", "Blue"}

# Check subset
if canadian.issubset(british): print("All Canadian flag colors occur in the British flag.")
if not italian.issubset(british): print("At least one of the colors in the Italian flag does not.")
# Check equality
if british == French: print("The British and French flags use the same colors.")


# The order matters with difference() method
print(british.union(italian) == italian.union(british))    # True
print(british.intersection(italian) == italian.intersection(british))    # True
print(british.difference(italian) == italian.difference(british))    # False



"""
Hashing: the order of Python set elements is determined by 'hash table', a special structure
         hash table uses integer values called 'hash code'
         set elements are grouped into smaller into collections having same characteristic
         set operations are much faster than list operations because the operation is performed within the smaller group
         
         to calculate hash codes, you can use hash() function
         possible that there are multiple elements with the same hash code
             >>> https://www.geeksforgeeks.org/python/python-hash-method/
"""
