from os import *
from sys import *
from collections import *
from math import *

def titleToNumber(stringStr):
    # Write your code here
    res = 0
    for ch in stringStr:
        res = res * 26 + (ord(ch) - ord('A') + 1)
    # Return number
    return res
