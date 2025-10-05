from sys import *
from collections import *
from math import *

from typing import *

def stringMania(n : int, m : int, str1 : str, str2 : str) -> int:
    # Write your code here.
    if str1 > str2:
        return 1
    elif str1 < str2:
        return -1
    else:
        return 0
