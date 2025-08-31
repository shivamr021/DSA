from os import *
from sys import *
from collections import *
from math import *

def groupAllOneTogether(arr, n):
    # Write your code here.
    totalOnes = arr.count(1)
    if totalOnes == 0:
        return -1
    if totalOnes == n:
        return 0
    
    currOnes = sum(arr[:totalOnes])
    maxOnes = currOnes

    for i in range(totalOnes, n):
        currOnes += arr[i] - arr[i-totalOnes]
        maxOnes = max(maxOnes, currOnes)

    return totalOnes - maxOnes
