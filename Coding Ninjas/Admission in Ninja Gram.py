from os import *
from sys import *
from collections import *
from math import *

def ninjaGram(s):
    # Write your Code Here.
    s = s.lower()
    letters = set()
    for ch in s:
        if 'a' <= ch <= 'z':
            letters.add(ch)
    # Return a boolean variable 'True' or 'False' denoting the answer
    return len(letters) == 26
