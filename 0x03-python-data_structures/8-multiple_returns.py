#!/usr/bin/python3
def multiple_returns(sentence):
    tup = ()
    if len(sentence) == 0:
        tup = (len(sentence), None)
    else:
        tup = (len(sentence), sentence[:1])
    return tup
