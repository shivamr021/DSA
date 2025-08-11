from os import *
from sys import *
from collections import *
from math import *

def matrixGame(mat):
    # Write your Code Here.
    n = len(mat)

    prod = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += mat[i][k] * mat[k][j]
            prod[i][j] = s

    for i in range(n):
        for j in range(n):
            if prod[i][j] != mat[i][j]:
                return False
    # Return a boolean variable 'True' or 'False'
    return True
    
