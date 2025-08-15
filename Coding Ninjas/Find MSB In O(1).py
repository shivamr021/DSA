from os import *
from sys import *
from collections import *
from math import *

def findMSB(n):
    # Write your code here.
    return 1 << (n.bit_length() - 1)
