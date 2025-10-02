from os import *
from sys import *
from collections import *
from math import *

def isValidIPv4(ipAddress):
    # Write your code here.
    parts = ipAddress.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False

        num = int(part)

        if num < 0 or num > 255:
            return False

    return True
