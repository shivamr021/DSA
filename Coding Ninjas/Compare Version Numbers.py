from os import *
from sys import *
from collections import *
from math import *

def compareVersions(a, b):
    #Write your code here
    i, j = 0, 0
    n, m = len(a), len(b)

    while i < n or j < m:
        num1, num2 = 0, 0

        while i < n and a[i] != '.':
            num1 = num1 * 10 + int(a[i])
            i += 1
        i += 1

        while j < m and b[j] != '.':
            num2 = num2 * 10 + int(b[j])
            j += 1
        j += 1

        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1

    return 0
