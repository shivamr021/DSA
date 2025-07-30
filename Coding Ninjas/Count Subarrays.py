from os import *
from sys import *
from collections import *
from math import *

def numberofSubarrays(arr, n):
    # Write your code here.
    cnt = 0
    i = 0
    
    while i < n:
        curr = arr[i]
        leng = 0

        while i < n and arr[i] == curr:
            leng += 1 
            i+= 1

        cnt += (leng * (leng + 1)) // 2

    return cnt
