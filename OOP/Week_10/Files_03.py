# Week 10 (4)

## Reading Characters: can read individual characters with the read() method
inputFile = open("lyrics.txt", "r")
char = inputFile.read(1)
while char != "":
    char = inputFile.read(1)
inputFile.close()


"""
ord(c) | return the ordinal value or Unicode value for 'c'
         for example, uppercase letters in sequential letter, from 65 for "A" through 90 for "Z"
"""
letterCounts = [0] * 26
inputFile = open("lyrics.txt", "r")
char = inputFile.read(1)
while char != "":
    char = char.upper()    # convert lowercase to uppercase
    if char >= "A" and char <= "Z":    # make sure the character is a letter
        code = ord(char) - ord("A")    # obtain index to the list 'letterCounts'
        letterCounts[code] += 1
inputFile.close()


## Reading Records: text file can contain a collection of data records
#1) each data record on a multiple line 
# assume each record consists of two fields: the name of a country and its population
"""
ex) China
    1330044605
    India
    1147995898
    United States
    303824646
"""
line = inputFile.readline()        # read the first field of the first record
while line != "":
    countryName = line.rstrip()    # remove the newline character
    line = inputFile.readline()    # read the second field
    population = int(line)
    line = inputFile.readline()    # read the first field of the next record

#2) each data record on a single line and the fields are seperated by a specific delimiter
"""
ex) China:1330044605
    India:1147995898
    United States:303824646
"""
for line in inputFile:
    fields = line.split(":")
    countryName = fields[0]
    population = int(fields[1])

#3) each data record on a single line and the fields are seperated by space delimiter
"""
ex) China 1330044605
    India 1147995898
    United States 303824646
"""
i = 0
char = line[0]
while not line[i].isdigit(): i += 1    # method1: search for the first digit
countryName = line[:i-1]
population = int(line[i:])

fields = line.rsplit(" ", 1)    # method2: split two parts using rsplit() method
                                # splitted parts are stored in the list in the order in which they occur in the string


"""
Reading the entire file: should avoid for large files
    1) using read() method: if no argument is passed, the method returns a string with all characters in the file
    2) using readlines() method: reads the entire contents of a text file into a list
"""
