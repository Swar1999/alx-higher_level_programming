#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    else:
        num_1 = sum(map(lambda x: x[0] * x[1], my_list))
        num_2 = sum(map(lambda x: x[1], my_list))
    return num_1 / num_2
