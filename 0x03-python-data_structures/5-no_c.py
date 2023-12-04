#!/usr/bin/env python3
def no_c(my_string):
    chars = []
    for i in my_string:
        if i.lower() != 'c':
            chars.append(i)
    new_string = ''.join(chars)
    return new_string
