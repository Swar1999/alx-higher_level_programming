#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    del_key = []
    for k, v in a_dictionary.items():
        if key == k:
            del_key.append(k)
    for k in del_key:
        del a_dictionary[k]
    return a_dictionary
