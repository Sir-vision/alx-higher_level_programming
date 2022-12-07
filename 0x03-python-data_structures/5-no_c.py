#!/usr/bin/python3
def no_c(my_string):
    string_copy = []
    for char in my_string:
        if (char != 'c') and (char != 'C'):
            string_copy.append(char)
    return "".join(string_copy)
