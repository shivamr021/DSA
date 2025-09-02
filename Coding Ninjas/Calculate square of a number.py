from os import *
from sys import *
from collections import *
from math import *

def multiply(a, b):
    res = 0 
    x, y = abs(a), abs(b)
    while y > 0:
        if y & 1:
            res += x
        x <<= 1
        y >>= 1
    return res if (a >= 0) == (b >= 0) else -res

def calculateSquare(n):
    #Write your code here
    return multiply(n, n)
