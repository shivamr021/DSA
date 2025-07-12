from os import *
from sys import *
from collections import *
from math import *

def decrypt(message, operations):
    # Write your code here.
    n = len(message)
    net_rot = 0

    for dirt, cnt in operations:
        if dirt == -1:
            net_rot += cnt
        elif dirt == 1:
            net_rot -= cnt
    
    net_rot %= n

    return message[net_rot:] + message[:net_rot]
