#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    big_int = my_list[0]
    for i in my_list:
        if i > big_int:
            big_int = i
    return big_int
