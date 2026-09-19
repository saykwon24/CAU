# Week 11 (3)

"""
Dictionary: container that contains key-value pairs or items; i.e. maps a unique key to value (keys are unique)
            curly braces({}) mean a dictionary, not a set
            key-value pairs are seperated by a colon
            you can access the items by subscript operator([]), but cannot by index or position
            value can be accessed using its associated key
            if an invalid key is supplied, 'KeyError' will be raised
            but instead, you can get a default value using get() method
            like a set, dictionary uses a hash table, so its items are stored in an order for efficiency

    [syntax] 
    emtpy dictionary | dictName = {}
                     | dictName = dict()
"""

# Create an empty dictionary
contacts = {}
contacts = dict()


# Access key-value pair using subscript operator
contacts = {"Fred": 12345, "Mary": 13579, "Bob": 24680, "Sarah": 98765}
print("Fred's number is", contacts["Fred"])


# To create a duplicate copy of dictionary, use dict() function
new_contacts = dict(contacts)    # 'new_contacts' is duplicated copy of 'contacts'
new_contacts = contacts          # two variables share address of the dictionary (same address)
    # they are not same



"""
Some method for dictionary: because dictionaries are mutable, you can add or remove items
    dict.get(key, v=None) | return a value of 'key' or return 'v' if 'key' does not exist
    dict.pop(key)         | return a value associated with 'key' and remove the value from 'dict'
                            if 'key' is not in 'dict', raise KeyError exception
    dict.keys()           | return a list of keys
    dict.values()         | return a list of values
    dict.items()          | return a sequence of tuples containing keys and values
                            the first slot of tuple is key, the second is value
>>> https://www.w3schools.com/python/python_ref_dictionary.asp
"""

# Return a value instead of raising an exception
number = contacts.get("David", 411)    # default value == 411
print(number)


# Add, change and remove an item
contacts["John"] = 33333
contacts["John"] = 22222
John_number = contacts.pop("John")



"""
Traversing a dictionary: can access individual keys or values
"""
#1) iterate over the individual keys
for key in contacts: print(key)


#2) access the values using subscript operator
for key in contacts: print("%-10s %d" % (key, contacts[key]))
# iterate through the keys in sorted order using sorted() function
for key in sorted(contacts): print("%-10s %d" % (key, contacts[key]))


#3) iterate over the individual values using values() method
phone_nums = []
for number in contacts.values(): phone_nums.append(number)
#phone_nums = list(contacts.values())    # another method


#4) iterate over the items using items() method
for item in contacts.items(): print(item[0], item[1])
#for (key, value) in contacts.items(): print(key, value)    # another method