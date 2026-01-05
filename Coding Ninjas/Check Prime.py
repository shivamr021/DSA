from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def is_prime(n):
    if n < 2:
        return "NO"
    if n == 2 or n == 3:
        return "YES"
    if n % 2 == 0 or n % 3 == 0:
        return "NO"
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return "NO"
    return "YES"

n = int(input())
print(is_prime(n))
