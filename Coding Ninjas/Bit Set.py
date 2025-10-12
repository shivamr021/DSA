from sys import *
from collections import *
from math import *

# This function returns the first repeating digit integer value.
def findFirstRepeatingDigit(digitPattern):
    # Write your code here.
    bit_mask = 0

    for ch in digitPattern:
        digit = int(ch)
        bit = 1 << digit
        
        if bit_mask & bit:
            return digit

        bit_mask |= bit
    
    return -1
