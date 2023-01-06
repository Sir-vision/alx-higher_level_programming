#!/usr/bin/python3

"""Define a function text_indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters
    Args:
        ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    while (i < len(text)):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print('\n')
            i += 1
        i += 1
