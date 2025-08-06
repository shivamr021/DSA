from os import *
from sys import *
from collections import *
from math import *

def stringBreaker(s, n, dictionary):
    # Write your code here.
    word_set = set(dictionary)
    length = len(s)

    dp = [float('inf')] * length

    for i in range(length):
        for j in range(i+1):
            substring = s[j:i+1]
            if substring in word_set:
                if j == 0:
                    dp[i] = 0
                else:
                    dp[i] = min(dp[i], dp[j-1] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1
