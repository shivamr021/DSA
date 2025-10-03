from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    #   Write your code here
    i = 0
    while i < len(arr) and arr[i] == 0:
        i += 1
    arr = arr[i:] if i < len(arr) else [0]

    n = len(arr)
    carry = 1
    for j in range(n - 1, -1, -1):
        arr[j] += carry
        if arr[j] < 10:
            carry = 0
            break
        else:
            arr[j] = 0
            carry = 1

    if carry:
        arr.insert(0, 1)

    return arr
