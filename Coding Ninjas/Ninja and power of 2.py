from os import *
from sys import *
from collections import *
from math import *

def numberPattern(n):
    # Write your Code Here.
    # Return a 2 - d list of integers
    res = []
    curr = 1
    for i in range(1, n+1):
        row = []
        cnt = 2 ** (i - 1)

        for _ in range(cnt):
            row.append(curr)
            curr += 1
            if curr == 10:
                curr = 1

        res.append(row)
    
    return res
