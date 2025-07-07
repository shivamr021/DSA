from os import *
from sys import *
from collections import *
from math import *

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def totalPrime(S, E):
    count = 0
    for num in range(S, E + 1):
        if is_prime(num):
            count += 1
    return count

S, E = map(int, input().split(' '))
print(totalPrime(S, E))
