from os import *
from sys import *
from collections import *
from math import *

def findNonRepeating(str):
    # Write your code here
    # Return a single character
    frq = {}
    for ch in str:
        frq[ch] = frq.get(ch, 0) + 1
    
    for ch in str:
        if frq[ch] == 1:
            return ch
    return "#"
