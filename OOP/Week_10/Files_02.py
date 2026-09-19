# Week 10 (3)
"""
Newline character in file: each input line has newline character(\n) at the end
                           also, print() function displays a newline at the end as default value
                           so when you give a file object as an argument of print() function, will be displayed with a blank line between each line (two newline characters)
                           to avoid this situation, you can remove the newline by using string methods

Some string Methods removing white spaces
    str.rstrip(chars=None) | return a copy of string without white spaces of the right side of 'str'
                             if 'chars' is given, characters in 'chars' are removed
    str.lstrip(chars=None) | return a copy of string without white spaces of the left side of 'str'
    str.strip(chars=None)  | return a copy of string without white spaces of the both side of 'str'
>>> https://docs.python.org/3/library/stdtypes.html#str
"""

# remove white spaces
line = "Hello World ?.?!  \t.. \n"
print(line.rstrip())    # Hello World ?.!  \t..

# remove required characters, but don't
line = "Hello World ?.?!  \t.. \n"
print(line.rstrip("?!"))    # Hello World ?.!  \t.. \n

# remove required characters
line = "Hello World ?.?!"
print(line.rstrip("?!"))    # Hello World ?.



"""
Reading individual words: first read the line, and then split it into individual words using split() method
                          if you want to print out the words without punctuation mark or so, use strip() method

    str.split(sep=None, maxsplit=-1)  | return a list containing all individual words of line seperated by spaces (treats consecutive spaces as a single delimiter, but not any other delimiters)
                                        if the delimiter 'sep' is given, 'str' is splitted based on that
                                        if 'maxsplit' is given, at most 'maxsplit' splits are done (i.e. 'maxsplit' + 1 elements)
    str.rsplit(sep=None, maxsplit=-1) | same as split() method, except the splits are made starting from the end of 'str'
    str.splitlines()                  | return a list of the lines in 'str'
    >>> https://docs.python.org/3/library/stdtypes.html#str
"""

string = "Mary had a little lamb,"
print(string.rstrip(",").split())


inputFile = open("lyrics.txt", "r")
for line in inputFile:         # read the lines of text by iterating over the file object
    line = line.rstrip()       # remove the spaces at the end of line
    wordList = line.split()    # split line into individual words
    for word in wordList:
        word = word.rstrip(".,?!")
        print(word)
inputFile.close()


# Difference between split() and rsplit()
string = "a:bc:d"
print(string.split(":", 1))     # "a", "bc:d"
print(string.rsplit(":", 1))    # "a:bc", "d"


# Consecutive delimiter
string = "apples:pears::grapes"
print(string.split(":"))    # "apples", "pears", "", "grapes"

string = "a b  c"
print(string.split(" "))    # "a", "b", "", "c"