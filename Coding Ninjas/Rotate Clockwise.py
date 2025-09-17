from os import *
from sys import *
from collections import *
from math import *

def rotateClockwise(n, nums):
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            nums[i][j], nums[j][i] = nums[j][i], nums[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        nums[i].reverse()

    return nums
