#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a dictionary.values():
        for key, word in a_dictionary.items():
            if word == value:
                del a_dictionary[key]
                break
    return a_dictionary
