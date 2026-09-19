# Week 10 (2)
"""
File I/O: you can open a file using open() function
          [syntax] open(filename, mode, encoding="utf-8", newline="")
              first, give the file name(when located in same directory) or that preceded by the directory path(when located in different directory)
              in latter case, you should enter backslash twice(\\) to indicate backslash of the directory path
              when a file is opened, 'input marker' is positioned at the beginning of the file
              then specify the file mode; "r" for read, "w" for (over)write, "x" for exclusive file creation, "a" for appending to the end of file
              most popular encoding is UTF-8, so generally use this encoding format
              then returns a 'file object' through which all operations for accessing a file are made
              if the file already exists, it is emptied before writing
              if the file doesn't exist, an empty file is created
              when your work are done, the file must be closed using close() method

Some Methods for File I/O
    fileObject.close()          | save and close the file associated with 'fileObject'
    fileObject.read()           | read entire text of the file, and then return in one string
                                  can take a single argument that specifies the number of characters to read
    fileObject.readline()       | read a line of text from the file, starting at the current position where the input maker is located
                                  input marker is moved to the next line, then return the text including newline character(\n) as a string
    fileObject.readlines()      | read the file and return a list containing the entire contents of a text file
                                  each element of the list is a single line of the file
    fileObject.write(str)       | write 'str'(single string) immediately, the string is appended to the end of the file
                                  can also write formatted string
    fileObject.writelines(list) | write 'list' of lines at the file
>>> https://docs.python.org/3/library/io.html#i-o-base-classes


File vs. Container: once the file has been read, cannot iterate over the file again without first closing and reopening
                    you can iterate or re-read the file using seek() function; fileObject.seek(0)
                    >>> https://docs.python.org/3/library/io.html#io.IOBase.seek
"""

## Open a file with read mode
infile = open("input.txt", "r")

# read the file line by line
line = infile.readline()
while line != "":    # sentinel value is an empty string
    line = infile.readline()

# close the file
infile.close()


## Open a file with write mode
outfile = open("output.txt", "w")

# write the file
outfile.write("Hello, World!\n")    # must explicitly write newline character
print("Hello, World!", file=outfile)    # alternatively, can write with print() function
                                        # give the file object as an argument
outfile.write("Number of entries: %d\nTotal: %8.2f\n" % (10, 100))    # can write formatted string

# close the file
outfile.close()