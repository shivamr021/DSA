from os import *
from sys import *
from collections import *
from math import *

def numberofSubarrays(arr, n):
    # Write your code here.
    total = 0
    cnt = 1
    
    for i in range(1, n):
        if arr[i] == arr[i-1]:
            cnt += 1
        else:
            total += cnt * (cnt + 1) // 2
            cnt = 1
    
    total += cnt * (cnt + 1) // 2

    return total
