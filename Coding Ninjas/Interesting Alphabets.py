from os import *
from sys import *
from collections import *
from math import *

def interestingPattern(n):
    result = []
    for i in range(n):
        start = n - i - 1  # index of starting char
        row = ""
        for j in range(start, n):
            row += chr(ord('A') + j)
        result.append(row)
    return result
