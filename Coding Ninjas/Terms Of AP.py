from os import *
from sys import *
from collections import *
from math import *

def termsOfAP(x):

    # Write your code here
    # Return a list of integers
    res = []
    n = 1
    while len(res) < x:
        term = 3 * n + 2
        if term % 4 != 0:
            res.append(term)
        n += 1
    return res
