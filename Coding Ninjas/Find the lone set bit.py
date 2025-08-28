from os import *
from sys import *
from collections import *
from math import *

def findSetBit(N):   
    # Write your code here
    if N == 0 or (N & (N - 1)) != 0:
        return -1

    return int(log2(N)) + 1
