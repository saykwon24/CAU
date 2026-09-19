# Week 11 (1)

"""
Command Line Arguments(CLAs): different methods of starting a program by typing its name and additional information in the command line
                              it is customary to interpret strings starting with a hyphen(-) as program options
                              it has major advantage; easy to automate
                              by using batch files or shell scripts, can automatically call program many times with different CLAs

sys module: a module that provides access to some variable used or maintained by the interpreter and functions that interact strongly with the interpreter
            programs starting from the command line receive the CLAs in the argv list defined in the sys module
    sys.argv        | the list of CLAs
    sys.exit([str]) | raise a SystemExit exception, signaling an intention to exit the interpreter
>>> https://docs.python.org/3/library/sys.html
"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
else:
    print("hello, my name is", sys.argv[1])





## for reference
"""
switch(or flag): keywords that do a specific behavior when you type CLAs
                 'dash + one character' or 'dash dash + one word'
    -n N or --number N | number of times('N' times)
    -h or --help       | show help message

argparse library: a library that reads and processes switches in CLAs, i.e. argument parser
>>> https://docs.python.org/3/library/argparse.html


import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")    # instantiate an object of class 'ArgumentParser'
                                                                   # print the string when type '-h(--help)'
parser.add_argument("-n", default=1, help="number of times to meow", type=int)    # add an argument that will be used as switch
                                                                                  # by default N == 1 and 'N' should be integer
                                                                                  # print the string when type '-h(--help)'
args = parser.parse_args()    # an object of 'parser.parse_args'
                              # automatically look at 'sys.argv'
                              # parsed all of the CLAs by 'parser'

for _ in range(args.n):    # 'n' is property in the object, access to it
    print("meow")
"""