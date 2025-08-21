from os import *
from sys import *
from collections import *
from math import *

def hotelBookings(queries):
    # Write your code here.
    coins = 0
    for q in queries:
        if q and q[0] == "+":
            coins += 1
    return coins
