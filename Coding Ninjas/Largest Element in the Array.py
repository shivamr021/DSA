from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.
    max_ele = arr[0]
    for num in arr:
        if num > max_ele:
            max_ele = num
    return max_ele
