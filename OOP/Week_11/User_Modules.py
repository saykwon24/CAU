# Week 11 (5)

"""
When programs get larger or you work in a team, it is better to split your code into seperate source files
there are 2 reasons:
    1) the larger the program is, the more difficult to manage and debug the source file
    2) it would be difficult to edit a single source file simultaneously
so, distribute the functions over serveral source files and group related functions together
also, each seperated files can be reused in another program

large Python programs typically consist of 2 type of modules:
    1) driver module       | contain main function or first executable statement
    2) supplemental module | contain supporting functions and constant variables

to call a function or use a constant variable that is defined in a user module, import the module
    1) from funcName import moduleName
    2) import moduleName
"""
