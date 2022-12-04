#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for item in my_string:
        if item not in "Cc":
            new_string += item
    return new_string
