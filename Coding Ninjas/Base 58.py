from sys import *
from collections import *
from math import *

alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def encodeBase58(n):
    # Write your code here
    if n == 0:
        return alphabet[0]

    res = []
    while n > 0:
        n, rem = divmod(n, 58)
        res.append(alphabet[rem])

    return ''.join(reversed(res))
