from os import *
from sys import *
from collections import *
from math import *

def swapAdjacentBits(n):
    # Write your code here.
    odd = n &  0xAAAAAAAA
    even = n & 0x55555555

    odd >>= 1
    even <<= 1

    return odd | even
