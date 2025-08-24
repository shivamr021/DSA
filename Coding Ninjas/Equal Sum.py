from os import *
from sys import *
from collections import *
from math import *

def equalSum(token):

    # Write your code Here.
    # Return an integer denoting the answer.
    total_sum = sum(token)
    left_sum = 0

    for i in range(len(token)):
        right_sum = total_sum - left_sum - token[i]

        if left_sum == right_sum:
            return i
        
        left_sum += token[i]

    return -1
